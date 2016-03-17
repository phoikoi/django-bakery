from django.shortcuts import render
from .models import Article
from bakery.views import BuildableArchiveIndexView


class MyIndexView(BuildableArchiveIndexView):
    model = Article
    date_field = 'pub_date'
