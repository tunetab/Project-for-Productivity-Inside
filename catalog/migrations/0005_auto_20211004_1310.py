# Generated by Django 3.2.7 on 2021-10-04 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_author_nickname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('can_mark_blocked', 'Set recipe or author as blocked'),)},
        ),
        migrations.RemoveField(
            model_name='author',
            name='num_recipes',
        ),
    ]
