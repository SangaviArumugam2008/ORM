
from django.db import models
from django.contrib import admin
class Details(models.Model):
    Name=models.CharField(max_length=10)
    Mobile_No=models.IntegerField(primary_key=True)
    Email=models.EmailField()
    Address=models.TextField()
    pin_code=models.IntegerField()
    DOB=models.DateField()
    Payment_method=models.CharField(max_length=10)
class DetailsAdmin(admin.ModelAdmin):
    list_display=["Name","Mobile_No","Email","Address","pin_code","DOB","Payment_method"]

