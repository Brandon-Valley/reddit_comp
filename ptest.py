import subprocess
cmd = "ffmpeg -i C:/Users/Brandon/Documents/Personal_Projects/reddit_comp//vids_to_compile/f_10/post_0010.fhls-955.mp4 -i 'C:/Users/Brandon/Documents/Personal_Projects/reddit_comp/vids_to_compile/f_10/post_0010.fdash-AUDIO-1.m4a' -c copy out.mp4"
subprocess.call(cmd, shell=True)