from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album
from django.http import Http404
# Create your views here.


def index(request):
    html = ''
    albums = Album.objects.all()
    context = {
        'all_albums': albums
    }

    return render(request, 'music/index.html',context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    
    return render(request, 'music/detail.html', {'album':album})