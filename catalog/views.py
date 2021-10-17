from django.shortcuts import render

# Create your views here.

from .models import Type, Recipe, Author
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User

def index(request):
    num_recipes=Recipe.objects.filter(status__exact='a').count()
    num_authors = Author.objects.filter(status__exact='a').count()
    return render(
        request,
        'index.html',
        context={'num_recipes':num_recipes, 'num_authors':num_authors},
    )

class RecipeListView(generic.ListView):
    model = Recipe
    template_name = "catalog/templates/catalog/recipe_list.html"
    pagination_by = 10
    

class RecipeDetailView(generic.DetailView):
    model = Recipe

from django.contrib.auth.mixins import LoginRequiredMixin

class AuthorListView(generic.ListView):
    model = Author
    template_name = "catalog/templates/catalog/author_list.html"
    pagination_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author
    pagination_by = 10

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Recipe

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['author', 'pub_date', 'title', 'summary', 'cooking_steps', 'type', 'photo', 'hashtag']

class AuthorMarkBlocked(UpdateView):
    model = Author
    fields = ['status']

class RecipeMarkBlocked(UpdateView):
    model = Recipe
    fields = ['status']
    