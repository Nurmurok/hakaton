from django.urls import path

from .views import (
ProductListApiView, GetCartAPIView,ProductCreateAPIView,CategoryListApiView
)


urlpatterns = [
    path('list/', ProductListApiView.as_view(), name='list'),
    path('cat_list/', CategoryListApiView.as_view(), name='list'),
    path('cart/<int:id>', GetCartAPIView.as_view(), name='cart'),
    path('create/', ProductCreateAPIView.as_view(), name='create')

]