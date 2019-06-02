from moviepy.editor import VideoFileClip, concatenate_videoclips

import os
from os import listdir
from os.path import isfile, join

import subprocess

VIDS_TO_COMPILE_FOLDER_PATH = 'vids_to_compile'

VID_CONCAT_FILE_PATH = 'concat_filepaths.txt'
OUTPUT_VID_FILE_PATH = 'output.mp4'



def write_text_file(file_path, line_list):
    f = open(file_path, 'w', encoding='utf-8')
    # write to file
    for line in line_list:
        f.write(line + '\n')
    # cleanup
    f.close()
    
# make sure everyone ends with .mp4
def clean_up_vid_extentions():
    vid_filename_list = os.listdir(VIDS_TO_COMPILE_FOLDER_PATH)
    
    for vid_filename in vid_filename_list:
        split_vid_filename = vid_filename.split('.')
        if split_vid_filename[-1] != 'mp4':
            new_vid_filename = split_vid_filename[0] + '.mp4'
            os.rename(VIDS_TO_COMPILE_FOLDER_PATH + '/' + vid_filename, VIDS_TO_COMPILE_FOLDER_PATH + '/' + new_vid_filename)
    
    
    
def compile_vids():
    clean_up_vid_extentions()
    
    vid_filenames_to_compile = [f for f in listdir(VIDS_TO_COMPILE_FOLDER_PATH) if isfile(join(VIDS_TO_COMPILE_FOLDER_PATH, f))]
      
#     # build concat txt file
#     line_list = []
#     for vid_filename in vid_filenames_to_compile:
#         vid_file_path = VIDS_TO_COMPILE_FOLDER_PATH + '/' + vid_filename 
#         line_list.append('file ' + vid_file_path)
# #         print(line_list)#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
#     write_text_file(VID_CONCAT_FILE_PATH, line_list)
#         
#     
#     # concat the files in the txt file
#     cmd = 'ffmpeg -f concat -i ' + VID_CONCAT_FILE_PATH + ' -c copy ' + OUTPUT_VID_FILE_PATH + ' -y'
#     subprocess.call(cmd, shell=True)

    clip_list = []
    for vid_filename in vid_filenames_to_compile:
        clip_list.append(VideoFileClip(VIDS_TO_COMPILE_FOLDER_PATH + '/' + vid_filename))
    
    final_clip = concatenate_videoclips(clip_list, method='compose')
    final_clip.write_videofile(OUTPUT_VID_FILE_PATH) 

    print('done with compile')
    
    
    
    
compile_vids()