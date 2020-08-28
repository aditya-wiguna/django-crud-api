from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    marital_status = models.CharField(max_length=50, blank=False, default='')
    identity_number = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=191, blank=False, default='')
    parent_name = models.CharField(max_length=191, blank=False, default='')
    is_active = models.BooleanField(default=False)
