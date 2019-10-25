from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import *


def index(request):
    return render(request, 'mirillis/index.html', {})

def projects(request):
    return render(request, 'mirillis/projects.html', {})

def all_articles(request):
    articles = (Article.objects.values())
    # ctx = [{"title":article.description, "text":article.text} for article in articles]
    return render(request, 'mirillis/blog.html', {'articles':articles})

def view_article_content(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    return render(request, 'mirillis/view_article_content.html',  {'article':article})
