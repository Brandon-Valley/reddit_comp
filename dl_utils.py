import praw,requests,re
import os
import shutil
import youtube_dl
import subprocess

# from selenium import webdriver

import requests
import time
from pytube import YouTube
from moviepy.editor import VideoFileClip
from wx.lib.agw.flatmenu import GetMRUEntryLabel

import file_system_utils
import credentials

# 
# def get_text_from_url(url):
#     time.sleep(10)
#     response = requests.get(url)
#     return response.text

def get_vid_length(filename):
#     result = subprocess.Popen(["ffprobe", filename],
#     stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
#     print(stdout)#211111``````````````````````````````````````````````````````````````````````````````````````````````
#     return [x for x in result.stdout.readlines() if "Duration" in x]

    clip = VideoFileClip(filename)
    duration = clip.duration 
    clip.reader.close()
    clip.audio.reader.close_proc()
    return(duration)


# '1:36' -->  96
def time_str_to_total_seconds(time_str):
    time_str = duration_str.split(':')
    seconds = int( duration_split_str[1])
    minutes = int( duration_split_str[0])
    
    total_seconds = seconds + (minutes * 60)
    return total_seconds
    

def get_vid_duration__reddit(post_id):
        post = credentials.reddit.submission(id=post_id, url=None)
#         print('                                                        POST>MEDIA:  ', post.media)#````````````````````````````````````````````````````````````````````````````````````````````````
#         duration = int(post.media['reddit_video']['duration'])
        if post.media == None:
            return False
        return int(post.media['reddit_video']['duration'])

 
def get_vid_duration__youtube(post_info_d):
        myVideo = YouTube(post_info_d['postURL'])
        return myVideo.length 
 

# # trys to return length of video in seconds, returns false if it cant tell
# def get_vid_duration(post_info_d):
#     
#     # youtube
#     if   post_info_d['postType'] == None:
#         myVideo = YouTube(post_info_d['postURL'])
#         return myVideo.length 
#     # reddit embedded 
#     elif post_info_d['postType'] == 'direct':
#         post = credentials.reddit.submission(id=post_info_d['postId'], url=None)
#         return post.media['reddit_video']['duration']
#     else:
#         raise ValueError('ERROR:  Dont know how to get duration of this --> post_info_d:  ', post_info_d)

        
        
def make_vid_save_name(post_num):
    num_zeros_to_add = 4 - len(str(post_num))
    return 'post_' + ('0' * num_zeros_to_add) + str(post_num)
        
        
def correct_failed_vid_audio_combine(save_dir_path, vid_save_title):
    print('in correct_failed_vid_audio_combine !!!!!!!!!!!!!!!!!!!!!!!!!!!!! ')#```````````````````````````````````````````
    full_vid_temp_save_path = save_dir_path + '/temp/' + vid_save_title + '.mp4'
    
    #check if it downloaded correctly by checking if correct file exists,
    #if it does, move it to correct folder, if not, combine, then move
#     if os.path.isfile(full_vid_temp_save_path) == False:
    vid_file_path    = save_dir_path + '/temp/' + vid_save_title + '.fhls-955.mp4'
    audio_file_path  = save_dir_path + '/temp/' + vid_save_title + '.fdash-AUDIO-1.m4a'
    output_file_path = save_dir_path + '/'      + vid_save_title + '.mp4'

    cmd = "ffmpeg -i " + vid_file_path + " -i " + audio_file_path + " -c copy " + output_file_path
    subprocess.call(cmd, shell=True)
        
    # move final video file to correct dir and delete temp folder
#     os.rename(full_vid_temp_save_path, save_dir_path + '/' + vid_save_title + '.mp4')
    shutil.rmtree(save_dir_path + '/temp')

# downloads yt vid at highest resolution
def download_youtube_vid(videourl, path, save_title):
 
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
     
    # rename saved video
    newest_file_path = file_system_utils.get_newest_file_path(path)
    os.rename(newest_file_path, path + '//' + save_title + '.mp4')
# downloadYouTube('https://www.youtube.com/watch?v=zNyYDHCg06c', './videos/FindingNemo1')


def download_reddit_vid(video_url, save_dir_path, vid_save_title):

   # see options at https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L89
    ydl_opts = {'outtmpl': save_dir_path + '/temp/' + vid_save_title + '.%(ext)s',
                'socket-timeout': 20,
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'}
#                 'format':'137'} <------------------------------------------------------------------- this is what is making stuff fail, need to find a way to always use the highest resolution available
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url, ])
    

    try:
        # move final video file to correct dir and delete temp folder
        full_vid_temp_save_path = save_dir_path + '/temp/' + vid_save_title + '.mp4'
        os.rename(full_vid_temp_save_path, save_dir_path + '/' + vid_save_title + '.mp4')
        os.rmdir(save_dir_path + '/temp')
    except OSError:
        correct_failed_vid_audio_combine(save_dir_path, vid_save_title)
    
    

        
        
            
            
import download_vids
if __name__ == '__main__':
#     download_vids.download_vids(50, ['dankvideos'])
#     download_reddit_vid('https://v.redd.it/hmngsw5agv131/DASH_360', 'test', 'test_vid')
    correct_failed_vid_audio_combine('vids_to_compile','post_0001' )
#     print(get_vid_duration__reddit("bvtsbd"))






