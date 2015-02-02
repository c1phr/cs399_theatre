from django.db import models

# Model to store some popular actors that star in movies
class Actor(models.Model):
    # Keep names separate in case we want to query against just part of the name
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Short description bio about the actor
    bio = models.CharField(max_length=5000)

# Model to store movie objects
class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    # This is meant to be running time in minutes
    running_time = models.IntegerField()
    # Many to many relationship with actors, since we could add actor records for multiple actors in a movie
    main_actors = models.ManyToManyField(Actor)