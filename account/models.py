from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    CHOICES=(
        ("vendor", "vendor"),
        ("customer", "customer")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    second_name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    is_vendor = models.CharField(max_length=255,choices=CHOICES,default="customer", null=True, blank=True)


    def __str__(self):
        return f'{self.user}'
