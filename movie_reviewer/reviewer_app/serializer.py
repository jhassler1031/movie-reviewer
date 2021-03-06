from rest_framework import serializers
from reviewer_app.models import Movie, Reviewer, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "imdb_link", "director", "release_year", "genre"]

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ["id", "age", "occupation", "postal_code"]

class ReviewSerializer(serializers.ModelSerializer):

    movie_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ["id", "stars", "review_text", "movie", "reviewer", "movie_name"]
        # depth = 1

    def get_movie_name(self, obj):
        return obj.movie.title
