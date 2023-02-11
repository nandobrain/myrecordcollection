from django.db import models
from django.urls import reverse



# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('venue_detail', kwargs={'pk': self.id})



class Artist(models.Model):
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    venue = models.ManyToManyField(Venue)
    
    


    def __str__(self):
        return self.artist

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'artist_id': self.id})


class Album(models.Model):
    album = models.CharField(max_length=100)
    releaseDate = models.IntegerField()

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('album_detail', kwargs={'album_id': self.id})