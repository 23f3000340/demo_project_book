from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/download/', views.download_book, name='download_book'),
    path('book/<int:pk>/request/', views.request_access, name='request_access'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('register/', views.register_view, name='register'),
]
