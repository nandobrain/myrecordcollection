from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('artist/', views.artist_index, name='index'),
    path('artist/<int:artist_id>', views.artist_detail, name='artist_detail'),
    path('artist/create/', views.ArtistCreate.as_view(), name='artist_create'),
    path('artist/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
    path('album/<int:artist_id>/create/', views.AlbumCreate.as_view(), name='album_create'),
    path('album/<int:pk>/update.', views.AlbumUpdate.as_view(), name='album_upgrade'),
    path('album/<int:pk>/delete.', views.AlbumDelete.as_view(), name='album_delete'),
    path('album/<int:album_id>', views.album_detail, name='album_detail'),
]