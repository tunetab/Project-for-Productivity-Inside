from django.urls import include
from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recipes/$', views.RecipeListView.as_view(), name='recipes'),
    url(r'^recipes/(?P<pk>\d+)$', views.RecipeDetailView.as_view(), name='recipe-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^authors/(?P<pk>[-\w]+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^recipes/create/$', views.RecipeCreate.as_view(), name='recipe_create'),
    url(r'^authors/(?P<pk>[-\w]+)/status/$', views.AuthorMarkBlocked.as_view(), name='author_update'),
    url(r'^recipes/(?P<pk>\d+)/status/$', views.RecipeMarkBlocked.as_view(), name='recipe_update'),
]