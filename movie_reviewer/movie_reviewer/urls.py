"""movie_reviewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from reviewer_app.views import welcome, MovieListCreateAPIView, MovieDetailAPIView, \
                            ReviewerListCreateAPIView, ReviewerDetailAPIView, ReviewListCreateAPIView, \
                            ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('movies/', MovieListCreateAPIView.as_view()),
    path('movies/<int:pk>', MovieDetailAPIView.as_view()),
    path('reviewers/', ReviewerListCreateAPIView.as_view()),
    path('reviewers/<int:pk>', ReviewerDetailAPIView.as_view()),
    path('reviews/', ReviewListCreateAPIView.as_view()),
    path('reviews/<int:pk>', ReviewRetrieveUpdateDestroyAPIView.as_view()),

]
