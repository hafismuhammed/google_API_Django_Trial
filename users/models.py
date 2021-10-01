from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='user_info')
    address = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    post_code = models.CharField(max_length=10)
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    captcha_score = models.FloatField(default=0.0)
    has_profile = models.PositiveSmallIntegerField(default=0)
    status = models.PositiveSmallIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


