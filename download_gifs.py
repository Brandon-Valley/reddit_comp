import praw,requests,re
import os
import youtube_dl

reddit = praw.Reddit(client_id='0MND-O3qUZg0gw',
                     client_secret='XuwpmqtersoJVnbukddVFOgKXl4', 
                     password='Barkbark1',
                     user_agent='PrawTut', 
                     username='goddard0001')

# submissions = reddit.get_subreddit('unexpectedjihad').get_top(limit=3)

subreddit = reddit.subreddit('videomemes')    
 
submissions = subreddit.hot(limit=2)

# urls = []
# def yt() :
#     for x in submissions:
#         urls.append(str(x.url))
#     return urls
# 
# yt_urls = yt()
# 
# for item in yt_urls:
#     print ("downloading..." + " ")
#     os.system("youtube-dl" + " " + item)
#     print ("done")


for item in submissions:
   # see options at https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py#L89
   ydl_opts = {'outtmpl': item.title + '.%(ext)s'}
   with youtube_dl.YoutubeDL(ydl_opts) as ydl:
       ydl.download([item.url, ])



# subreddit = reddit.subreddit('videomemes')    
# 
# # hot_python = subreddit.hot(limit=1)
# 
# # for submission in hot_python:
# #     print(submission)
# #     
# # for submission in hot_python:
# #     print(submission.title)
# #     
# 
# posts = subreddit.hot(limit=1)
# 
# 
# for post in posts:
#     url = (post.url)
#     print('url:  ', url)
#     file_name = url.split("/")
#     if len(file_name) == 0:
#         file_name = re.findall("/(.*?)", url)
#     file_name = file_name[-1]
#     if "." not in file_name:
#         file_name += ".mp4"
#     print(file_name)
# r = requests.get(url)
# with open(file_name,"wb") as f:
#     f.write(r.content)
    
    