from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    imdb_link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class Reviewer(models.Model):
    name = models.CharField(max_length=255)
