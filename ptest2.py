# import subprocess
# #HLSPlaylist.m3u8
# cmd = 'ffmpeg -i "C:/Users/Brandon/Documents/Personal_Projects/reddit_comp/in.m3u8" -acodec copy -vcodec copy out.mp4'
# subprocess.call(cmd, shell=True)
# 
# # cmd = 'ffmpeg -y -i Audio.wav  -r 30 -i Video.h264  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
# # subprocess.call(cmd, shell=True)                                     # "Muxing Done
# # print('Muxing Done')
import praw,requests,re
import os
import youtube_dl
import subprocess

# from selenium import webdriver

import requests
import time
from pytube import YouTube
from moviepy.editor import VideoFileClip


import file_system_utils
from wx.lib.agw.flatmenu import GetMRUEntryLabel

from moviepy.editor import VideoFileClip, concatenate_videoclips

import os
from os import listdir
from os.path import isfile, join

import subprocess
# vid_filenames_to_compile = [f for f in listdir() if isfile(join( f))]
# print(vid_filenames_to_compile)
# 
# 
# cmd = 'ffmpeg -i %s -i %s -c:v copy -c:a aac -strict experimental %s' % ('in.mp4', 'in.mpd', 'out.mp4')
# subprocess.call(cmd, shell=True)
VIDS_TO_COMPILE_FOLDER_PATH = 'vids_to_compile'



def download_reddit_vid(video_url, save_dir_path, post_title):

   # see options at https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L89
    ydl_opts = {'outtmpl': save_dir_path + '/' + post_title + '.%(ext)s',
                'socket-timeout': 20}
#                 'format':'137'} <------------------------------------------------------------------- this is what is making stuff fail, need to find a way to always use the highest resolution available
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url, ])
       

            
            
download_reddit_vid('https://v.redd.it/761apywe26131/DASH_1080', 'vids_to_compile', 'out')



