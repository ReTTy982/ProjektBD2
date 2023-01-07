from django.db import models

# Create your models here.

class Book(models.Model):
    BookID = models.IntegerField(primary_key=True)
    BookTitle = models.CharField(max_length=200)
    PublisherName = models.ForeignKey("publisher",on_delete=models.CASCADE)
    AuthorID = models.ForeignKey("author",on_delete=models.CASCADE)
    Category = models.CharField(max_length=100)
    class Meta:
        db_table = ''

class Author(models.Model):
    AuthorID = models.IntegerField(primary_key=True)
    AuthorName = models.CharField(max_length=255)


class Publisher(models.Model):
    PublisherName = models.CharField(max_length=100,primary_key=True)
    PhoneNumber = models.CharField(max_length=30)