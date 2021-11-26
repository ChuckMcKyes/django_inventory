from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/<str:ordering>', views.ItemListView.as_view(), name='item_list'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('item/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/<int:pk>/update/', views.ItemUpdateView.as_view(), name='item_update'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
    path('api/list/', views.InventoryListAPI.as_view(), name='list'),
    path('api/list', views.InventoryListAPI.as_view(), name='list'),
    path('api/categories/', views.CategoryListAPI.as_view(), name='categories'),
    path('api/categories', views.CategoryListAPI.as_view(), name='categories'),
    path('api/<int:pk>/', views.InventoryDetailsAPI.as_view(), name='detail'),
]
