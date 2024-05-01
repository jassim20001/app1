from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=3000)
    date=models.DateField()
    desc=models.CharField(max_length=3000)
    img=models.ImageField(upload_to='photo')
class Comment(models.Model):
    name=models.CharField(max_length=3000)
    date=models.DateField()
    comment=models.TextField(max_length=3000)
    email=models.CharField(max_length=3000)


class Conect(models.Model):
    name=models.CharField(max_length=3000)
    email=models.CharField(max_length=3000)
    subject=models.TextField(max_length=3000)