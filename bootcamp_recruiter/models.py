from django.db import models
from django.utils import timezone

class Company(models.Model):
    industry_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_url = models.URLField()
    bootcamp_grad_hired = models.IntegerField()
    contact = models.EmailField()
    notes = models.TextField()
    twitter_handle = models.CharField(max_length=100); 

    created_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.company_name

# Create your models here.
