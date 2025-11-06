from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse, Http404
from django.db.models import Q
from .models import Book, Category, AccessRequest
from .forms import RegisterForm, AccessRequestForm
import os


def book_list(request):
    """Homepage: list books with search and filters"""
    q = request.GET.get('q', '')
    access_filter = request.GET.get('access', '')
    category_filter = request.GET.get('category', '')
    
    qs = Book.objects.select_related('category').all()
    
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(author__icontains=q) | Q(description__icontains=q))
    
    if access_filter in ['free', 'restricted']:
        qs = qs.filter(access_type=access_filter)
    
    if category_filter:
        qs = qs.filter(category__slug=category_filter)
    
    categories = Category.objects.all()
    paginator = Paginator(qs, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'store/book_list.html', {
        'page_obj': page_obj,
        'q': q,
        'access_filter': access_filter,
        'category_filter': category_filter,
        'categories': categories,
    })


def book_detail(request, pk):
    """Book detail page with download/request button"""
    book = get_object_or_404(Book, pk=pk)
    
    # Check if user has access
    can_download = False
    existing_request = None
    
    if request.user.is_authenticated:
        if book.access_type == 'free':
            can_download = True
        elif book.access_type == 'restricted':
            # Check if user has approved access
            approved = AccessRequest.objects.filter(
                user=request.user,
                book=book,
                status='approved'
            ).exists()
            can_download = approved
            
            # Check existing request
            existing_request = AccessRequest.objects.filter(
                user=request.user,
                book=book
            ).first()
    
    return render(request, 'store/book_detail.html', {
        'book': book,
        'can_download': can_download,
        'existing_request': existing_request,
    })


@login_required
def download_book(request, pk):
    """Secure download view - checks permissions before serving file"""
    book = get_object_or_404(Book, pk=pk)
    
    # Check access
    can_download = False
    
    if book.access_type == 'free':
        can_download = True
    elif book.access_type == 'restricted':
        # Check if user has approved access
        can_download = AccessRequest.objects.filter(
            user=request.user,
            book=book,
            status='approved'
        ).exists()
    
    if not can_download:
        messages.error(request, "You don't have permission to download this book.")
        return redirect('book_detail', pk=pk)
    
    # Serve file
    file_path = book.pdf.path if book.pdf else (book.file.path if book.file else None)
    
    if not file_path or not os.path.exists(file_path):
        messages.error(request, "File not found.")
        return redirect('book_detail', pk=pk)
    
    # Increment download counter
    book.downloads += 1
    book.save(update_fields=['downloads'])
    
    # Stream file
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=f"{book.title}.pdf")
    return response


@login_required
def request_access(request, pk):
    """User requests access to a restricted book"""
    book = get_object_or_404(Book, pk=pk)
    
    if book.access_type != 'restricted':
        messages.info(request, "This book is free to download.")
        return redirect('book_detail', pk=pk)
    
    # Check if request already exists
    existing = AccessRequest.objects.filter(user=request.user, book=book).first()
    if existing:
        messages.info(request, f"You already have a {existing.status} request for this book.")
        return redirect('book_detail', pk=pk)
    
    if request.method == 'POST':
        form = AccessRequestForm(request.POST)
        if form.is_valid():
            access_req = form.save(commit=False)
            access_req.user = request.user
            access_req.book = book
            access_req.save()
            messages.success(request, "Access request submitted successfully!")
            return redirect('book_detail', pk=pk)
    else:
        form = AccessRequestForm()
    
    return render(request, 'store/request_access.html', {'form': form, 'book': book})


@login_required
def user_dashboard(request):
    """User's dashboard showing their access requests and downloads"""
    access_requests = AccessRequest.objects.filter(user=request.user).select_related('book')
    
    # Books user can download (free + approved restricted)
    approved_books = Book.objects.filter(
        Q(access_type='free') |
        Q(access_requests__user=request.user, access_requests__status='approved')
    ).distinct()
    
    return render(request, 'store/user_dashboard.html', {
        'access_requests': access_requests,
        'approved_books': approved_books,
    })


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('book_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
