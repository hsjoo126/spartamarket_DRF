from django.urls import path
from . import views
urlpatterns = [
    path("", views.ProductListAPIView.as_view(), name="product_list"), 
    path("<int:productsID>", views.ProductDetailAPIView.as_view()), 
    path("<int:productsID>/like", views.LikeAPIView.as_view()), 
]
