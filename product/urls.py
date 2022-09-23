from django.urls import path

from .views import (
ProductListApiView, GetCartAPIView,CartUpdateApiView
)


urlpatterns = [
    path('', ProductListApiView.as_view(), name='list'),
    path('cart/<int:id>', GetCartAPIView.as_view(), name='cart'),
    path('addtocart/<int:id>', CartUpdateApiView.as_view(), name='update'),
]