from django.urls import path
from . import views
urlpatterns = [
    #클래스 자체를 넘기는 것이 아니라 as_view()메서드를 사용해서 호출 가능한 함수로 변환해요!
    #목록이니까~
    path("", views.ProductListAPIView.as_view(), name="product_list"), 
]
