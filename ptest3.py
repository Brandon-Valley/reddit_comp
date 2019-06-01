from moviepy.editor import VideoFileClip, concatenate_videoclips


from moviepy.editor import VideoFileClip, concatenate_videoclips

import os
from os import listdir
from os.path import isfile, join


VIDS_TO_COMPILE_FOLDER_PATH = 'vids_to_compile'
VID_CONCAT_FILE_PATH = 'concat_filepaths.txt'
OUTPUT_VID_FILE_PATH = 'output.mp4'
vid_filenames_to_compile = [f for f in listdir(VIDS_TO_COMPILE_FOLDER_PATH) if isfile(join(VIDS_TO_COMPILE_FOLDER_PATH, f))]

clip_list = []
for vid_filename in vid_filenames_to_compile:
    clip_list.append(VideoFileClip(VIDS_TO_COMPILE_FOLDER_PATH + '/' + vid_filename))

final_clip = concatenate_videoclips(clip_list)
final_clip.write_videofile("my_concatenation.mp4")