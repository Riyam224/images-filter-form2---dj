from django.contrib import admin
from django.utils import regex_helper

# Register your models here.
from .models import Product

admin.site.register(Product)