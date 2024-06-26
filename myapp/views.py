from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import search,video_ID,download
from ytmusicapi import YTMusic

ytmusic = YTMusic()


def index(request):

    ytmusic = YTMusic()

    trending_songs = ytmusic.get_charts(country='IN')['trending']['items']
    # trending_songs = ytmusic.get_charts(country='ZZ')['videos']['items']
    trending_artists = ytmusic.get_charts(country='ZZ')['artists']['items']
    mood_categories = ytmusic.get_mood_categories()['Moods & moments']
    home = ytmusic.get_home(5)
    # print(trending_songs)
    video_ID(trending_songs)
    return render(request,'MUSIC-PAYER-CODING-NINJA-PROJECT-main/index.html',{'trending_songs': trending_songs,'trending_artists':trending_artists,'mood_categories':mood_categories,'home':home})

def get_song(request):
    if request.method == 'GET':
        if request.GET.get('song_id', ''):
            video_id = request.GET.get('song_id', '')
            songin = download(video_id)
            # print("getsong path:")
            # print(video_id)
            url0 = songin['videoDetails']['thumbnail']['thumbnails'][0]['url']
            videoDetail = songin['videoDetails']

            return JsonResponse({'url0': url0 , 'videoDetail':videoDetail},safe=False)
        
        elif request.GET.get('name', ''):
            name = request.GET.get('name')
            search_results = search(name)
            # url0 ,'url0': url0
            return JsonResponse({'search_results': search_results }, safe=False)
        else:    
             return JsonResponse([],safe=False)
         
def artist(request, artist):
    artists = ytmusic.get_artist(artist)
    # print(artists)
    return render(request,'MUSIC-PAYER-CODING-NINJA-PROJECT-main/artist.html', {'artist': artists })

def playlist(request, playlist):
    # print(playlist)
    playlists =  ytmusic.get_playlist(playlist)
    trending_songs = ytmusic.get_charts(country='IN')['trending']['items']
    # print(playlists)
    return render(request,'MUSIC-PAYER-CODING-NINJA-PROJECT-main/Playlist.html', {'playlist': playlists ,'trending_songs':trending_songs})
