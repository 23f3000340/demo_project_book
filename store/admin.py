from django.contrib import admin
from django.utils import timezone
from .models import Book, Category, AccessRequest


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'access_type', 'downloads', 'created_at')
    list_filter = ('access_type', 'category', 'created_at')
    search_fields = ('title', 'author')
    list_per_page = 20


@admin.register(AccessRequest)
class AccessRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status', 'created_at', 'reviewed_by')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'book__title')
    actions = ['approve_requests', 'deny_requests']

    def approve_requests(self, request, queryset):
        queryset.update(status='approved', reviewed_at=timezone.now(), reviewed_by=request.user)
        self.message_user(request, f"{queryset.count()} request(s) approved.")
    approve_requests.short_description = "Approve selected requests"

    def deny_requests(self, request, queryset):
        queryset.update(status='denied', reviewed_at=timezone.now(), reviewed_by=request.user)
        self.message_user(request, f"{queryset.count()} request(s) denied.")
    deny_requests.short_description = "Deny selected requests"
