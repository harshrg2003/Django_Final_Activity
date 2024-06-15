from django.db import models

# Create your models here
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    addr=models.CharField(max_length=50)
    city=models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=10)

    def __str__(self):
        return self.first_name+" "+self.last_name
class Book(models.Model):
    title=models.CharField(max_length=10)
    author=models.CharField(max_length=10)        
    def __str__(self):
        return self.title