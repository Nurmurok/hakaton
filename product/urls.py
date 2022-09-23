from django.urls import path

from .views import (
ProductListApiView, GetCartAPIView
)


urlpatterns = [
    path('list/', ProductListApiView.as_view(), name='list'),
    path('cart/<int:id>', GetCartAPIView.as_view(), name='cart')

]