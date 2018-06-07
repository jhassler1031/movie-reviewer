from django.contrib import admin

from reviewer_app.models import Movie, Reviewer, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Reviewer)
admin.site.register(Review)
