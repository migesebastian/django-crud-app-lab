from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.id})
    
class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(max_length=500)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review {self.id}: {self.rating} Stars"
    
    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.id})

