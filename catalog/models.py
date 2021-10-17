from django.db import models
from django.urls import reverse

# Create your models here.

class Type(models.Model):
    """
    Model representing a type of dish (e.g. salad, soup, dessert)
    """
    # Fields
    name = models.CharField(max_length = 200, help_text="Enter a type of dish (e.g. salad, soup, dessert etc.)")

    # Metadata
    class Meta:
        ordering = ["name"]

    # Methods
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])

from django.contrib.auth.models import User
import uuid

class Author(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for each author")
    nickname = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    USER_STATUS = (
        ('a', 'Active'),
        ('b', 'Blocked'),
    )
    status = models.CharField(max_length=1, choices=USER_STATUS, blank=True, default='a')
    #likes = models.OneToManyFields('Recipe', on_delete=models.CASCADE, null=True)

    class Meta:
        permissions = (("can_mark_blocked", "Set recipe or author as blocked"),)
            
    def __str__(self):
        return '%s, (%s)' % (self.nickname, self.id)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

import datetime

class Recipe(models.Model):
    """
    Model representing a pecipe of the dish
    """
    # Fields
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateField(default=datetime.date.today)
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500, help_text="Enter a brief description of the dish")
    cooking_steps = models.TextField(max_length=1500, help_text="Enter cooking steps")
    type = models.ManyToManyField(Type, help_text="Select a type of the dish")
    photo = models.ImageField(upload_to='images/')
    hashtag = models.CharField(max_length = 100, help_text="Enter a set of hashtags")

    RECIPE_STATUS = (
        ('a', 'Active'),
        ('b', 'Blocked'),
    )
    status = models.CharField(max_length=1, choices=RECIPE_STATUS, blank=True, default='a', help_text='Recipe availability')

    # Metadata
    class Meta:
        ordering = ["-pub_date"]
        permissions = (("can_mark_blocked", "Set recipe or author as blocked"),)

    # Methods
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.id)])

    def display_type(self):
        return ', '.join([type.name for type in self.type.all()[:3]])

    display_type.short_description = 'Type'
