from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import *
from app.serializers import *
from app.tasks import deactivate_product

deactivate_product()


class ListCreateProductApi(ListCreateAPIView):
    queryset = Products.objects.filter(is_active=True).order_by("-id")
    serializer_class = ProductSerializer


class ProductIdApi(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductDetailAPI(RetrieveAPIView):
    queryset = Products.objects.filter(is_active=True)
    serializer_class = ProductSerializer


class ListCreateCommentApi(ListCreateAPIView):
    queryset = Comment.objects.all().order_by("-id")
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs["pk"]
        return Comment.objects.filter(prod_id=product_id)
