from django.db import models

# Model to store some popular actors that star in movies
class Actor(models.Model):
    # Keep names separate in case we want to query against just part of the name
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Short description bio about the actor
    bio = models.TextField(null=True)

# Model to store movie objects
class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    # This is meant to be running time in minutes
    running_time = models.IntegerField()
    # TextField to hold showtimes, nullable in case we create a movie record for a film that isn't out yet
    showtimes = models.TextField(null=True)
    # Many to many relationship with actors, since we could add actor records for multiple actors in a movie
    main_actors = models.ManyToManyField(Actor)