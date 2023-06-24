from django.urls import path

from .views import IndexView,  CategoryCreateView,CategoryView, ProductView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # +
    path("category/create", CategoryCreateView.as_view(), name="categories_create"),
    path("category/<pk>", CategoryView.as_view(), name="catalog"),
    path("product/<pk>", ProductView.as_view(), name="product"),
]
