from django.shortcuts import render
from django.http.response import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from reviewer_app.models import Movie, Reviewer, Review
from reviewer_app.serializer import MovieSerializer, ReviewerSerializer, ReviewSerializer

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Movie Review App")

#Views for the Movie Model =================================================
class MovieListCreateAPIView(APIView):
    def get(self, request):
        all_movies = Movie.objects.all()
        serialized_movies = MovieSerializer(all_movies, many=True)
        return Response(serialized_movies.data, 200)

    def post(self, request):
        title = request.POST["title"]
        imdb_link = request.POST["imdb_link"]
        director = request.POST["director"]
        release_year = request.POST["release_year"]
        genre = request.POST["genre"]
        new_movie = Movie.objects.create(title=title, imdb_link=imdb_link, director=director, release_year=release_year, genre=genre)
        serialized_movie = MovieSerializer(new_movie)
        return Response(serialized_movie.data, 201)

class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)
        serialized_movie = MovieSerializer(movie)
        return Response(serialized_movie.data, 200)

    def put(self, request, pk):
        movie = Movie.objects.get(id=pk)
        movie.title = request.POST["title"]
        movie.imdb_link = request.POST["imdb_link"]
        movie.director = request.POST["director"]
        movie.release_year = request.POST["release_year"]
        movie.genre = request.POST["genre"]
        movie.save()
        serialized_movie = MovieSerializer(movie)
        return Response(serialized_movie.data, 200)

    def delete(self, request, pk):
        movie = Movie.objects.get(id=pk)
        movie.delete()
        return Response("", 204)

#Views for the Reviewer Model ==================================================
class ReviewerListCreateAPIView(APIView):
    def get(self, request):
        all_reviewers = Reviewer.objects.all()
        serialized_reviewers = ReviewerSerializer(all_reviewers, many=True)
        return Response(serialized_reviewers.data, 200)

    def post(self, request):
        age = request.POST["age"]
        occupation = request.POST["occupation"]
        postal_code = request.POST["postal_code"]
        new_reviewer = Reviewer.objects.create(age=age, occupation=occupation, postal_code=postal_code)
        serialized_reviewer = ReviewerSerializer(new_reviewer)
        return Response(serialized_reviewer.data, 201)

class ReviewerDetailAPIView(APIView):
    def get(self, request, pk):
        reviewer = Reviewer.objects.get(id=pk)
        serialized_reviewer = ReviewerSerializer(reviewer)
        return Response(serialized_reviewer.data, 200)

    def put(self, request, pk):
        reviewer = Reviewer.objects.get(id=pk)
        reviewer.age = request.POST["age"]
        reviewer.occupation = request.POST["occupation"]
        reviewer.postal_code = request.POST["postal_code"]
        reviewer.save()
        serialized_reviewer = ReviewerSerializer(reviewer)
        return Response(serialized_reviewer.data, 200)

    def delete(self, request, pk):
        reviewer = Reviewer.objects.get(id=pk)
        reviewer.delete()
        return Response("", 204)

#Views for the Review Model - using generics
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
