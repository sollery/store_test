from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import  ProductListView, CategoryListView, SearchResultsListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:id>/', views.show_category_detail, name='category_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    ]