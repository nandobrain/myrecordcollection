from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Artist, Album, Venue

artist = [
    {'artist': 'Judas Priest', 'genre': 'Metal'},
    {'artist': 'Television', 'genre': 'post-punk'},
]


# Create your views here.



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def artist_index(request):
    artist = Artist.objects.all()
    return render(request, 'artist/index.html', {
        'artist': artist
    })

def artist_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    
    albums = Album.objects.filter(artist=artist_id)
    return render(request, 'artist/detail.html', { 'artist': artist, 'albums': albums })

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'album/detail.html', { 'album': album })

class ArtistCreate(CreateView):
    model = Artist
    fields = ['artist', 'genre']

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['genre']

class ArtistDelete(DeleteView):
    model = Artist
    success_url = '/artist'

class AlbumCreate(CreateView):
    model = Album
    fields = ['album', 'releaseDate']
    def form_valid(self, form):
        form.instance.artist_id = self.kwargs['artist_id']
        return super().form_valid(form)

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album', 'releaseDate']

class AlbumDelete(DeleteView):
    model = Album
    success_url = '/album'

class VenueList(ListView):
  model = Venue

class VenueDetail(DetailView):
  model = Venue

class VenueCreate(CreateView):
  model = Venue
  fields = '__all__'

class VenueUpdate(UpdateView):
  model = Venue
  fields = ['name', 'city']

class VenueDelete(DeleteView):
  model = Venue
  success_url = '/venue'