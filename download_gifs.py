import praw,requests,re

reddit = praw.Reddit(client_id='0MND-O3qUZg0gw',
                     client_secret='XuwpmqtersoJVnbukddVFOgKXl4', 
                     password='Barkbark1',
                     user_agent='PrawTut', 
                     username='goddard0001')

subreddit = reddit.subreddit('pics')    

# hot_python = subreddit.hot(limit=1)

# for submission in hot_python:
#     print(submission)
#     
# for submission in hot_python:
#     print(submission.title)
#     

posts = subreddit.hot(limit=2)


for post in posts:
    url = (post.url)
    file_name = url.split("/")
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name += ".jpg"
    print(file_name)
r = requests.get(url)
with open(file_name,"wb") as f:
    f.write(r.content)
    
    