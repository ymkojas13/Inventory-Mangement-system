from django.db import models

# Create your models here.
class usermodel(models.Model):
    Name=models.CharField(max_length=60)