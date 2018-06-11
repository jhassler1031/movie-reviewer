from django.db import models

# Create your models here.

#Movie Model ===============================================
class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    imdb_link = models.CharField(max_length=255, null=True)
    director = models.CharField(max_length=255, null=True)
    release_year = models.CharField(max_length=4, null=True)
    genre = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

#Reviewer Model ============================================
class Reviewer(models.Model):
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length=255, null=True)
    postal_code = models.IntegerField(null=True)

    def __str__(self):
        return f"""
Reviewer age {self.age}
occupation {self.occupation}
in {self.postal_code}
"""

#Review Model ===============================================
class Review(models.Model):
    stars = models.IntegerField(null=True)
    review_text = models.TextField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Review of {self.movie.title}")
