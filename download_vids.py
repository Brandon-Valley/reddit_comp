import praw,requests,re
import os
import youtube_dl
import subprocess

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



reddit = praw.Reddit(client_id     ='0MND-O3qUZg0gw',
                     client_secret ='XuwpmqtersoJVnbukddVFOgKXl4', 
                     password      ='Barkbark1',
                     user_agent    ='PrawTut', 
                     username      ='goddard0001')


subreddit = reddit.subreddit('videomemes')    
 
submissions = subreddit.hot(limit=20)



for item_num, item in enumerate(submissions):
    
    # test to see if you can tell how long the vidoe will be before
    # you start trying to download it, if you can tell, compare it 
    # to the MAX_CLIP_DURATION to see if it makes it in
#     vid_duration = get_vid_duration(driver)
    
    
    item_title = item.title.replace(" ", "_") # cant have spaces in the filenames
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
           


    
    