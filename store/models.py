from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Book(models.Model):
    ACCESS_CHOICES = [
        ('free', 'Free'),
        ('restricted', 'Restricted'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    
    # Cover and PDF file
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    pdf = models.FileField(upload_to='books/pdfs/', null=True, blank=True, help_text='Upload PDF file')
    
    # Access control
    access_type = models.CharField(max_length=20, choices=ACCESS_CHOICES, default='free')
    
    # Analytics
    downloads = models.PositiveIntegerField(default=0)
    
    # Legacy fields (keep for backward compatibility, can remove if not needed)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to='books/files/', null=True, blank=True)  # old field, use pdf now
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = ['-created_at']


class AccessRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='access_requests')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='access_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_requests')
    
    message = models.TextField(blank=True, help_text='Optional message from user')

    class Meta:
        unique_together = ['user', 'book']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} → {self.book.title} ({self.status})"
