from django.urls import path

from .views import (
RegisterAPIView,
MyObtainPairView
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', MyObtainPairView.as_view(), name='login'),
]