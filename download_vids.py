import praw,requests,re
import os
import youtube_dl
import subprocess

from selenium import webdriver

import requests
# import urllib.request
import time
# from bs4 import BeautifulSoup

VIDS_TO_COMPILE_FOLDER_PATH = 'vids_to_compile'

MAX_CLIP_DURATION = 45 # seconds



# 
# def get_text_from_url(url):
#     time.sleep(10)
#     response = requests.get(url)
#     return response.text

def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x]


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
def get_vid_duration(driver):
    try:
        total_seconds = get_vid_duration__reddit_embedded(driver)
        return total_seconds
    except:
        try:
            total_seconds = get_vid_duration__youtube(driver)
            return total_seconds
        except:
            return False


reddit = praw.Reddit(client_id     ='0MND-O3qUZg0gw',
                     client_secret ='XuwpmqtersoJVnbukddVFOgKXl4', 
                     password      ='Barkbark1',
                     user_agent    ='PrawTut', 
                     username      ='goddard0001')


subreddit = reddit.subreddit('videomemes')    
 
submissions = subreddit.hot(limit=50)


# set up browser
PATH = 'C:/Users/Brandon/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe' ## SET YOU PATH TO phantomjs
driver = webdriver.PhantomJS(PATH)


for item_num, item in enumerate(submissions):
    print("  checking duration of item #:  %s ..." %(item_num))
    
    # test to see if you can tell how long the vidoe will be before
    # you start trying to download it, if you can tell, compare it 
    # to the MAX_CLIP_DURATION to see if it makes it in
    driver.get(item.url)
    vid_duration = get_vid_duration(driver)
    if vid_duration != False and vid_duration > MAX_CLIP_DURATION:
        continue
    
    
    item_title = 'post_' + str(item_num)#item.title.replace(" ", "_") # cant have spaces in the filenames
#     post_titles.append(item.title)
   # see options at https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L89
    ydl_opts = {'outtmpl': VIDS_TO_COMPILE_FOLDER_PATH + '/' + item_title + '.%(ext)s',
                'socket-timeout': 20}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         dictMeta = ydl.extract_info(item.url, download=False)
#         print(dictMeta)

#         cmd = 'youtube-dl -o C:/Users/Brandon/Documents/Personal_Projects/reddit_comp/vids_to_compile/'+ item_title + ' ' + item.url + ' -c --socket-timeout 20'
#         subprocess.call(cmd, shell=True)
        try:
                
            ydl.download([item.url, ])
           
            # #join formats
            path_to_vid   = VIDS_TO_COMPILE_FOLDER_PATH + '/' + item_title + '.mp4'
            path_to_audio = VIDS_TO_COMPILE_FOLDER_PATH + '/' + item_title + '.m4a'
            out_path      = VIDS_TO_COMPILE_FOLDER_PATH + '/' + item_title + '_final_' + '.mp4'
            cmd = 'ffmpeg -i %s -i %s -c:v copy -c:a aac -strict experimental %s' % (path_to_vid, path_to_audio, out_path)
            subprocess.call(cmd, shell=True)
            
            
            #remove vid file that gets left in root dir
    #         os.remove(item_title + '.mp4')
        except:
            print ("FAIL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
           


    
    