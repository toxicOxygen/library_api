from django.db import models
# from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    authour = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return "Title: {}".format(self.title)
    
    # def get_absolute_url(self):
    #     return reverse()
