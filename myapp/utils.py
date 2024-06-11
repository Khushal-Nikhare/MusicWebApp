import functools
import pytube
import os
from django.conf import settings
from django.templatetags.static import static

import requests
from ytmusicapi import YTMusic
ytmusic = YTMusic() 

media_path=r'myapp\static\\'
# media_path=static()

def search(name):
    # print(filter)
    # if filter:
    #     search_results = ytmusic.search(name,filter[0])
    # else:
    search_results = ytmusic.search(name, 'songs')
    return search_results



def video_ID(search_results):
    print("call video_ID " + search_results[0]['category'])
    videoid=[]
    for cate in search_results:
        if cate['category'] == 'Songs':
            # print(cate)
            videoid.append(cate['videoId'])
    
    print(videoid)
    return videoid

def download(ids):
    print(static(ids + '.mp3'))
    print("call download ")
    paths = []
    songin=ytmusic.get_song(ids)
    result = search_file(media_path , ids +'.mp3')
    if result:
        paths.append(result[0])
    else:
        
        video_url="https://www.youtube.com/watch?v="+ ids
        video = pytube.YouTube(video_url).streams.filter(only_audio=True).first().download(media_path)
        base,ext = os.path.splitext(video)
        new_file = media_path + ids + '.mp3'
        os.rename(video, new_file)
        paths.append(new_file)
        
    print(songin)
    return songin
            

def search_file(folder_path, file_name):
    print("call search_file")
    found_files = []

    for root, dirs, files in os.walk(folder_path):
        if file_name in files:
            found_files.append(os.path.join(root, file_name))

    if found_files:
        return found_files


# import ytmusicapi
# print(ytmusicapi.setup(filepath="browser.json", headers_raw="<headers copied above>"))
