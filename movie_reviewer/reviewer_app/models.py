from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    imdb_link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class Reviewer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Review(models.Model):
    review_text = models.TextField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Review of {self.movie.title}")
