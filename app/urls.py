from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListCreateProductApi.as_view()),
    path("product_detail/<int:pk>", views.ProductDetailAPI.as_view()),
    path("product_detail/<int:pk>/comments", views.ListCreateCommentApi.as_view()),
    path("products/<int:pk>/", views.ProductIdApi.as_view()),
]
