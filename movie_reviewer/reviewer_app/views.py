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
