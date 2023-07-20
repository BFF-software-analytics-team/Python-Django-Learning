from django.db import models

# Create your models here.
class APITable(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()