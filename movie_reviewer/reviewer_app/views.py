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
