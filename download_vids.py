import praw,requests,re
import os
import youtube_dl
import subprocess

from selenium import webdriver

import requests
import time
from pytube import YouTube


import file_system_utils
import get_post_info_dl

PHANTOM_JS_PATH = 'C:/Users/Brandon/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe' ## SET YOU PATH TO phantomjs

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


def download_reddit_vid(video_url, save_dir_path, post_info_d_title):
    #     post_titles.append(post_info_d.title)
   # see options at https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L89
    ydl_opts = {'outtmpl': save_dir_path + '.%(ext)s',
                'socket-timeout': 20}
#                 'format':'137'} <------------------------------------------------------------------- this is what is making stuff fail, need to find a way to always use the highest resolution available
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         dictMeta = ydl.extract_info(post_info_d['postURL'], download=False)
#         print(dictMeta)

#         cmd = 'youtube-dl -o C:/Users/Brandon/Documents/Personal_Projects/reddit_comp/vids_to_compile/'+ post_info_d_title + ' ' + post_info_d['postURL'] + ' -c --socket-timeout 20'
#         subprocess.call(cmd, shell=True)
        try:
                
            ydl.download([video_url, ])
           
            # #join formats
            path_to_vid   = VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title + '.mp4'
            path_to_audio = VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title + '.m4a'
            out_path      = VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title + '_final_' + '.mp4'
            cmd = 'ffmpeg -i %s -i %s -c:v copy -c:a aac -strict experimental %s' % (path_to_vid, path_to_audio, out_path)
            subprocess.call(cmd, shell=True)
            
            
            #remove vid file that gets left in root dir
    #         os.remove(post_info_d_title + '.mp4')
        except:
            print ("FAIL!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



def download_vids(num_posts, subreddit_list):
    print(  'getting post_info_dl...')
    post_info_dl = get_post_info_dl.get_post_info_dl(num_posts, subreddit_list)



# reddit = praw.Reddit(client_id     ='0MND-O3qUZg0gw',
#                      client_secret ='XuwpmqtersoJVnbukddVFOgKXl4', 
#                      password      ='Barkbark1',
#                      user_agent    ='PrawTut', 
#                      username      ='goddard0001')
# 
# 
# subreddit = reddit.subreddit('videomemes')    
#  
# submissions = subreddit.hot(limit=5)


    # set up browser
    print('  setting up phanomJS browser (needed for some vid duration stuff)...')
    driver = webdriver.PhantomJS(PHANTOM_JS_PATH)


    for post_num, post_info_d in enumerate(post_info_dl):
        print("  checking duration of post_info_d #:  %s ..." %(post_num))
        
        # test to see if you can tell how long the vidoe will be before
        # you start trying to download it, if you can tell, compare it 
        # to the MAX_CLIP_DURATION to see if it makes it in
        driver.get(post_info_d['postURL'])
        vid_duration = get_vid_duration(driver)
        if vid_duration != False and vid_duration > MAX_CLIP_DURATION:
            continue
        
        
        post_info_d_title = 'post_' + str(post_num)#post_info_d.title.replace(" ", "_") # cant have spaces in the filenames
        
        
#         print(post_info_d['postURL'])
        
        download_youtube_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH, post_info_d_title)
        
        
    #     # check url to use the right downloader
    #     if post_info_d['postURL'].startswith('https://www.you'):
    #         download_youtube_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title, post_info_d_title)
    #     else:
    # #         download_reddit_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title)
    #         pass
        
        

           
if __name__ == '__main__':
    download_vids(4, ['videomemes', 'pics'])
    
    