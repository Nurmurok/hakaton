from django.urls import path

from .views import (
ProductListApiView, GetCartAPIView
)


urlpatterns = [
    path('', ProductListApiView.as_view(), name='list'),
    path('cart/<int:id>', GetCartAPIView.as_view(), name='cart'),
    # path('addtocart/', AddToCartAPIView.as_view(), name='cart'),
]