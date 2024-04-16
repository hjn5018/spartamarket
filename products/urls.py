from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
