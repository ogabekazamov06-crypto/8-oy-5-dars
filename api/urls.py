from django.urls import path
from .views import (
    CarBrandListCreateView, CarBrandRetrieveUpdateDestroyView,
    CarListCreateView, CarRetrieveUpdateDestroyView,
    CommentListCreateView, CommentRetrieveUpdateDestroyView
)

urlpatterns = [
    path('api/brands/', CarBrandListCreateView.as_view(), name='brand_list_create'),
    path('api/brands/<int:pk>/', CarBrandRetrieveUpdateDestroyView.as_view(), name='brand_detail'),

    path('api/cars/', CarListCreateView.as_view(), name='car_list_create'),
    path('api/cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car_detail'),

    path('api/comments/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('api/comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment_detail'),
]