import uploads
from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField

# Create your models here.



class Product(models.Model):
    name = models.CharField( max_length=50)
    desc = TextField()
    image = ImageField(blank=True , null=True , upload_to="products")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name