import subprocess
import json

import file_system_utils

# optional arguments:
#   -h, --help            show this help message and exit
#   --directory DIRECTORY, -d DIRECTORY
#                         Specifies the directory where posts will be downloaded
#                         to
#   --NoDownload          Just gets the posts and stores them in a file for
#                         downloading later
#   --verbose, -v         Verbose Mode
#   --quit, -q            Auto quit afer the process finishes
#   --link link, -l link  Get posts from link
#   --saved               Triggers saved mode
#   --submitted           Gets posts of --user
#   --upvoted             Gets upvoted posts of --user
#   --log LOG FILE        Takes a log file which created by itself (json files),
#                         reads posts and tries downloading them again.
#   --subreddit SUBREDDIT [SUBREDDIT ...]
#                         Triggers subreddit mode and takes subreddit's name
#                         without r/. use "frontpage" for frontpage
#   --multireddit MULTIREDDIT
#                         Triggers multireddit mode and takes multireddit's name
#                         without m/
#   --user redditor       reddit username if needed. use "me" for current user
#   --search query        Searches for given query in given subreddits
#   --sort SORT TYPE      Either hot, top, new, controversial, rising or
#                         relevance default: hot
#   --limit Limit         default: unlimited
#   --time TIME_LIMIT     Either hour, day, week, month, year or all. default:
#                         all

EXE_PATH = "C:/Users/Brandon/Documents/Personal_Projects/reddit_comp/bulk_downloader_for_reddit-1.6.5-windows/bulk-downloader-for-reddit.exe "
LOG_FILES_SAVE_PATH = 'bulk_download_log_files'
DEFAULT_SORT_TYPE = 'hot'


def build_arg_str(num_posts, subreddit_l, sort_type = DEFAULT_SORT_TYPE):
    # build_subreddit_l_str
    subreddit_l_str = subreddit_l[0]
    for subreddit in subreddit_l[1:]:
        subreddit_l_str += '+' + subreddit
            
    args = [' --directory ' + LOG_FILES_SAVE_PATH,
            ' --subreddit ' + subreddit_l_str,
            ' --limit '     + str(num_posts),
            ' --sort '      + sort_type,
            ' --NoDownload'
           ]
    
    #build arg_str
    arg_str = ''
    for arg in args:
        arg_str += arg
    
    return arg_str
    
    
def build_post_info_dl_from_json():
    #get path to most recent json logfile
    newest_log_file_dir = file_system_utils.get_newest_file_path(LOG_FILES_SAVE_PATH + '/LOG_FILES')
    json_file_path = newest_log_file_dir + '/POSTS.json'
    
    post_info_dl = []
    
    # read in json file
    with open(json_file_path) as json_file:  
        data = json.load(json_file)
        
        # fill post_info_dl
        post_num = 1
        while(str(post_num) in data):
            post_info_dl.append(data[str(post_num)][0])
            post_num += 1
        
    return post_info_dl
        

def get_post_info_dl(num_posts, subreddit_list):
    exe_arg_str = build_arg_str(num_posts, subreddit_list)
     
    cmd = EXE_PATH + exe_arg_str
    subprocess.call(cmd, shell=True)
    
    post_info_dl = build_post_info_dl_from_json()
    return post_info_dl













# print( get_post_info_dl(4, ['videomemes', 'pics']))

    