from __future__ import unicode_literals
from django.contrib.auth.models import models, User


class signupform(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    father_name = models.TextField(max_length=50, blank=True)
    current_address = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    permanent_address = models.CharField(max_length=30, blank=True)
    aadhar_card_number = models.CharField(max_length=30, blank=True)
