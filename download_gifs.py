import praw,requests,re
import os
import youtube_dl
import subprocess

VIDS_TO_COMPILE_FOLDER_PATH = 'vids_to_compile'

reddit = praw.Reddit(client_id='0MND-O3qUZg0gw',
                     client_secret='XuwpmqtersoJVnbukddVFOgKXl4', 
                     password='Barkbark1',
                     user_agent='PrawTut', 
                     username='goddard0001')


subreddit = reddit.subreddit('videomemes')    
 
submissions = subreddit.hot(limit=3)



for item_num, item in enumerate(submissions):
    item_title = item.title.replace(" ", "_") # cant have spaces in the filenames
#     post_titles.append(item.title)
   # see options at https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L89
    ydl_opts = {'outtmpl': VIDS_TO_COMPILE_FOLDER_PATH + '/' + item_title + '.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([item.url, ])
       
        # #join formats
        path_to_vid   = VIDS_TO_COMPILE_FOLDER_PATH + '/' + item_title + '.mp4'
        path_to_audio = VIDS_TO_COMPILE_FOLDER_PATH + '/' + item_title + '.m4a'
        out_path      = VIDS_TO_COMPILE_FOLDER_PATH + '/' + item_title + '_final_' + '.mp4'
        cmd = 'ffmpeg -i %s -i %s -c:v copy -c:a aac -strict experimental %s' % (path_to_vid, path_to_audio, out_path)
        subprocess.call(cmd, shell=True)
       


    
    