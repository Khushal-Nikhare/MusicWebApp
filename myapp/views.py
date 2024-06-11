from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .utils import search,video_ID,download
from ytmusicapi import YTMusic

ytmusic = YTMusic()

# def fetch_trending_songs(request):
#     if request.method == 'GET':
#         ytmusic = YTMusic()
#         trending_songs = ytmusic.get_charts(country='IN')['trending']['items']
#         print(trending_songs)
        
#         return JsonResponse({'trending_songs': trending_songs})
#     return JsonResponse({'error': 'Invalid request'}, status=400)

def index(request):

    ytmusic = YTMusic()

    trending_songs = ytmusic.get_charts(country='IN')['trending']['items']
    trending_artists = ytmusic.get_charts(country='IN')['artists']['items']
    mood_categories = ytmusic.get_mood_categories()['Moods & moments']
    home = ytmusic.get_home(5)
    # print(home)
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
        #     ytmusic = YTMusic()
        #     trending_songs = ytmusic.get_charts(country='IN')['trending']['items']
            
        #     clean_trending_songs = []
        #     for song in trending_songs:
                
        #         thumbnail_url = song['thumbnails'][0]['url'] if song.get('thumbnails') else ''
        #         clean_song = {
        #             'title': song.get('title'),
        #             'artists': [{'name': artist.get('name')} for artist in song.get('artists', [])],
        #             'videoId': song.get('videoId'),
        #             'thumbnail': thumbnail_url
        #         }
        #         clean_trending_songs.append(clean_song)
        #     # print(test)
        #     return JsonResponse({'trending_songs': clean_trending_songs})
    
    # if request.method == 'POST':
    #     # selected_options = request.POST.getlist('filter')
    #     name = request.POST.get('name')
    #     search_results = search(name)
    #     # vids = video_ID(search_results)
    #     # print(selected_options)
        # {% url 'playlist' trending_artist.artists.0.id %}
    #     return render(request, 'MUSIC-PAYER-CODING-NINJA-PROJECT-main\\index.html',{'results' : search_results })
    # return render(request, 'MUSIC-PAYER-CODING-NINJA-PROJECT-main\\index.html')

def artist(request, artist):
    artists = ytmusic.get_artist(artist)
    # print(artists)
    return render(request,'MUSIC-PAYER-CODING-NINJA-PROJECT-main/Playlist.html', {'artist': artists })

def playlist(request, playlist):
    playlists =  ytmusic.get_playlist(playlist)
    print(playlists)
    return render(request,'MUSIC-PAYER-CODING-NINJA-PROJECT-main/Playlist.html', {'playlist': playlists })

