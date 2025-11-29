from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.store, name='store'),
    path('shop/<slug:category_slug>/', views.store, name='products_by_category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]
