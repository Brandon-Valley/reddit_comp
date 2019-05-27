from moviepy.editor import VideoFileClip, concatenate_videoclips

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
    
    
    
def compile_vids():
    vid_filenames_to_compile = [f for f in listdir(VIDS_TO_COMPILE_FOLDER_PATH) if isfile(join(VIDS_TO_COMPILE_FOLDER_PATH, f))]
     
    # build concat txt file
    line_list = []
    for vid_filename in vid_filenames_to_compile:
        vid_file_path = VIDS_TO_COMPILE_FOLDER_PATH + '/' + vid_filename 
        line_list.append('file ' + vid_file_path)
        print(line_list)#``````````````````````````````````````````````````````````````````````````````````````````````````````````````
    write_text_file(VID_CONCAT_FILE_PATH, line_list)
        
    
    # concat the files in the txt file
    cmd = 'ffmpeg -f concat -i ' + VID_CONCAT_FILE_PATH + ' -c copy ' + OUTPUT_VID_FILE_PATH + ' -y'
    subprocess.call(cmd, shell=True)
    
    # #get list of video files in dir
    # video_filesnames_to_compile = [f for f in listdir(VIDS_TO_COMPILE_FOLDER_PATH) if isfile(join(VIDS_TO_COMPILE_FOLDER_PATH, f))]
    # 
    # 
    # video_file_clips_to_compile = []
    # for video_filename in video_file_clips_to_compile:
    #     video_file_clips_to_compile.append(VideoFileClip( VIDS_TO_COMPILE_FOLDER_PATH + '/' + video_filename ))
    # 
    # 
    # 
    # clip1 = VideoFileClip(VIDS_TO_COMPILE_FOLDER_PATH + '/' + 'Oof.mp4')
    # clip2 = VideoFileClip(VIDS_TO_COMPILE_FOLDER_PATH + '/' + 'This kid is going places.mp4')#.subclip(50,60)
    # # clip3 = VideoFileClip("myvideo3.mp4")
    # final_clip = concatenate_videoclips([clip1, clip2])
    # final_clip.write_videofile("my_concatenation.mp4")
    
    
    
    
compile_vids()