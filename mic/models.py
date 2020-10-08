from django.db import models
from django.urls import reverse

class album(models.Model):
    artist = models.CharField(max_length=250)
    album_tittle = models.CharField(max_length=500)
    album_logo = models.CharField(max_length=2500)
    genre = models.CharField(max_length=250)
    def get_absolute_url(self):
        return reverse('mic:detail',kwargs={'pk':self.pk})


    def __str__(self):
        return self.artist


class song(models.Model):
    album=models.ForeignKey(album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=250)
    song_tittle = models.CharField(max_length=250)
    def __str__(self):
        return self.song_tittle
