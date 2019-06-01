import praw

reddit = praw.Reddit(client_id     ='0MND-O3qUZg0gw',
                     client_secret ='XuwpmqtersoJVnbukddVFOgKXl4', 
                     password      ='Barkbark1',
                     user_agent    ='PrawTut', 
                     username      ='goddard0001')

subreddit = reddit.subreddit('dankvideos')
hot_python = subreddit.hot(limit = 3)
for submission in hot_python:
    print(submission.media['reddit_video']['fallback_url'])
    print(submission.media)
