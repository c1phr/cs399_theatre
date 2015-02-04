# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.db import migrations

from theatre_project.models import Movie


def add_showtimes(app, schema_editor):
    times = [ "10:30am", "12:00pm", "1:00pm", "12:45pm", "1:30pm", "2:30pm", "3:00pm", "4:00pm", "5:15pm", "6:00pm",
             "7:30pm", "8:00pm", "8:15pm", "9:45pm", "10:00pm"]
    for movie in Movie.objects.all():
        movie_times = ""
        for num_times in range(random.randint(0, 8)):
            movie_times += times[random.randint(0, len(times))] + ", "
        movie.showtimes = movie_times
        movie.save()


class Migration(migrations.Migration):
    dependencies = [
        ('theatre', '0003_auto_20150203_0308'),
    ]

    operations = [
        migrations.RunPython(add_showtimes),
    ]
