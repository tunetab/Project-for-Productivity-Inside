# Generated by Django 3.2.7 on 2021-10-02 13:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for each author', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('a', 'Active'), ('b', 'Blocked')], default='a', max_length=1)),
                ('nickname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'permissions': (('can_mark_blocked', 'Set recipe or author as blocked'),),
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a type of dish (e.g. salad, soup, dessert etc.)', max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the dish', max_length=500)),
                ('cooking_steps', models.TextField(help_text='Enter cooking steps', max_length=1500)),
                ('photo', models.ImageField(upload_to='images/')),
                ('hashtag', models.CharField(help_text='Enter a set of hashtags', max_length=100)),
                ('status', models.CharField(blank=True, choices=[('a', 'Active'), ('b', 'Blocked')], default='a', help_text='Recipe availability', max_length=1)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author')),
                ('type', models.ManyToManyField(help_text='Select a type of the dish', to='catalog.Type')),
            ],
            options={
                'ordering': ['-pub_date'],
                'permissions': (('can_mark_blocked', 'Set recipe or author as blocked'),),
            },
        ),
    ]