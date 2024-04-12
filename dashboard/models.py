
from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields if needed

    def __str__(self):
        return self.user.username

    

class Email(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    text = models.TextField()

    def __str__(self):
        return self.subject


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Products/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
        



