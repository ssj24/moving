# Generated by Django 2.2.7 on 2019-11-22 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='movie_genres', to='movies.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
    ]