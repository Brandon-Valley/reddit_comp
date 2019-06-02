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
    return( clip.duration )


# '1:36' -->  96
def time_str_to_total_seconds(time_str):
    time_str = duration_str.split(':')
    seconds = int( duration_split_str[1])
    minutes = int( duration_split_str[0])
    
    total_seconds = seconds + (minutes * 60)
    return total_seconds
    

def get_vid_duration__reddit_embedded(driver):
    sp1 = driver.page_source.split('class="portrait"></video><span class="seek-bar-time"></span></div></div><span class="time-label" data-control-type="text" data-action="totalTime">')
    duration_str = sp1[1].split('<')[0]
    
    return(time_str_to_total_seconds(duration_str))

 
def get_vid_duration__youtube(driver):
    duration_str = driver.find_element_by_class_name('ytp-time-duration')
    return time_str_to_total_seconds(duration_str)
 

# trys to return length of video in seconds, returns false if it cant tell
def get_vid_duration(driver, vid_url):
    try:
        myVideo = YouTube(vid_url)
        return myVideo.length 
    except:
        try:
            total_seconds = get_vid_duration__reddit_embedded(driver)
            return total_seconds
        except:
#             try:
#                 total_seconds = get_vid_duration__youtube(driver)
#                 return total_seconds
#             except:
            return False
        
        
def make_vid_save_name(post_num):
    num_zeros_to_add = 4 - len(str(post_num))
    return 'post_' + ('0' * num_zeros_to_add) + str(post_num)
        

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
    ydl_opts = {'outtmpl': save_dir_path + '/' + vid_save_title + '.%(ext)s',
                'socket-timeout': 20}
#                 'format':'137'} <------------------------------------------------------------------- this is what is making stuff fail, need to find a way to always use the highest resolution available
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url, ])
            
            
import download_vids
if __name__ == '__main__':
    download_vids.download_vids(20, ['dankvideos'])