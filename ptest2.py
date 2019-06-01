# import subprocess
# #HLSPlaylist.m3u8
# cmd = 'ffmpeg -i "C:/Users/Brandon/Documents/Personal_Projects/reddit_comp/in.m3u8" -acodec copy -vcodec copy out.mp4'
# subprocess.call(cmd, shell=True)
# 
# # cmd = 'ffmpeg -y -i Audio.wav  -r 30 -i Video.h264  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
# # subprocess.call(cmd, shell=True)                                     # "Muxing Done
# # print('Muxing Done')


from moviepy.editor import VideoFileClip, concatenate_videoclips

import os
from os import listdir
from os.path import isfile, join

import subprocess
vid_filenames_to_compile = [f for f in listdir() if isfile(join( f))]
print(vid_filenames_to_compile)