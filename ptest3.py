# from pytube import YouTube
# YouTube('https://www.youtube.com/watch?v=mbkAYTg_fhw&feature=share').streams.first().download('folder')



# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=n06H7OcPd-g")
# yt = yt.get('mp4', '720p')
# yt.download('test')




from pytube import YouTube
import os
#  
# # downloads yt vid at highest resolution
# def download_youtube_vid(videourl, path):
#  
#     yt = YouTube(videourl)
#     yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#     if not os.path.exists(path):
#         os.makedirs(path)
#     yt.download(path)
#  
# download_youtube_vid('https://www.youtube.com/watch?v=mbkAYTg_fhw&feature=share', './videos/FindingNemo1')

import subprocess
import file_system_utils

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


download_youtube_vid('https://v.redd.it/cc4ybss0w6131/DASH_720', 'folder', 'post_1')

print ('done!')
# import glob
# import os
#  
# list_of_files = glob.glob('./videos/FindingNemo1/*') # * means all if need specific format then *.csv
# latest_file = max(list_of_files, key=os.path.getctime)
# print (latest_file)


# import urllib
# 
# 
# 
# 
# 
# url = ''.join(('https://www.reddit.com/r/videomemes/comments/btf8ne/when_your_mom_finds_you_playing_video_games_at_3/','.json')) #add .json to end of url input for python to extract video url
# 
# with urllib.request.urlopen(url) as url: #python open url as http request
#             data = json.loads(url.read().decode()) #read the json url
#             file = data[0]['data']['children'][0]['data']['secure_media']['reddit_video']['fallback_url'] #navigate the json to the url that has the mp4 (fallback_url)
# 
#             #debug
#             print('file') #print if url is read
#             time.sleep(4) #reddit has a request limit per minute (see below)
# #             wget.download(file,'C:/Users/x/Downloads/') #use wget to download the file, hopefully in .mp4, but doesn't work
#             
#             urllib.request.urlretrieve(file, "download.mp4")








