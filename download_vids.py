# pip install --upgrade --force-reinstall pytube

# Video unavailable:   An exception of type KeyError occurred. Arguments:
# ('s',)

# youtube_dl.utils.DownloadError: ERROR: unable to rename file: [WinError 32] The process cannot access the file because it is being used by another process: 'vids_to_compile\\post_0051.fdash-VIDEO-1.mp4.part' -> 'vids_to_compile\\post_0051.fdash-VIDEO-1.mp4'

# Video unavailable:   An exception of type RegexMatchError occurred. Arguments:
# ('regex pattern (\\bc\\s*&&\\s*d\\.set\\([^,]+\\s*,\\s*\\([^)]*\\)\\s*\\(\\s*(?P<sig>[a-zA-Z0-9$]+)\\() had zero matches',)


from selenium import webdriver
import youtube_dl # need??????????????????
import time

import file_system_utils
import get_post_info_dl
import dl_utils

import testing_utils
from test.test_optparse import _check_duration
from distutils.command.check import check

PHANTOM_JS_PATH = 'C:/Users/Brandon/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe' ## SET YOU PATH TO phantomjs

VIDS_TO_COMPILE_FOLDER_PATH = 'vids_to_compile'

MAX_CLIP_DURATION = 45 # seconds

INDENT = '                                            '



QUICK_TEST = True
def download_vids(num_posts, subreddit_list):
    print(INDENT + 'QUICK_TEST:  ', QUICK_TEST)
    print(INDENT + 'Getting post_info_dl...')
    if QUICK_TEST == True:
        post_info_dl = get_post_info_dl.get_post_info_dl(num_posts, subreddit_list, quick_test = True)
    else:
        post_info_dl = get_post_info_dl.get_post_info_dl(num_posts, subreddit_list)

#     # set up browser
#     print('  Setting up phanomJS browser (needed for some vid duration stuff)...')
#     driver = webdriver.PhantomJS(PHANTOM_JS_PATH)

    print(INDENT + 'Deleting all files in %s...' %(VIDS_TO_COMPILE_FOLDER_PATH))
    file_system_utils.delete_all_files_in_dir(VIDS_TO_COMPILE_FOLDER_PATH)

    for post_num, post_info_d in enumerate(post_info_dl):
        
        testing_utils.print_str_wo_error(INDENT + "Starting on post_info_d #:  %s   title: %s..." %(post_num, post_info_d['postTitle']))
 
        vid_save_title = 'f_' + str(post_num) + '/' + dl_utils.make_vid_save_name(post_num) #~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
                            
        
        # youtube video
        if post_info_d['postType'] == None:
            print(INDENT + 'Trying to download youtube video...')
            try:
                if dl_utils.get_vid_duration__youtube(post_info_d) < MAX_CLIP_DURATION:
                    dl_utils.download_youtube_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH, vid_save_title)
            except Exception as e:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(e).__name__, e.args)
                print(INDENT + 'Video unavailable:  ', message)
                continue
        # embedded reddit video
        elif post_info_d['postType'] == 'direct':
            print(INDENT + 'Trying to download reddit video...')
            print(INDENT + 'Sleeping...')
            time.sleep(1)
            while True:
                try:
                    #try to get vid duration
                    check_vid_duration_after_download = False
                    vid_duration = dl_utils.get_vid_duration__reddit(post_info_d['postId'])
                    
                    if vid_duration == False:
                        check_vid_duration_after_download = True
                    elif vid_duration > MAX_CLIP_DURATION:
                        break
                    
#                     if dl_utils.get_vid_duration__reddit(post_info_d['postID']) < MAX_CLIP_DURATION:
                    dl_utils.download_reddit_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH, vid_save_title)
                   
                    # delete video if its too long
                    vid_save_path = VIDS_TO_COMPILE_FOLDER_PATH + '/' + vid_save_title + '.mp4'
                    if check_vid_duration_after_download == True and dl_utils.get_vid_length(vid_save_path) > MAX_CLIP_DURATION:
                        print('  Video too long, deleting video...')
                        os.remove(vid_save_path)
                    break                   
                
                except (youtube_dl.utils.DownloadError, OSError) as e:
                    print(e.args)
                    print(INDENT + 'Download error, sleeping, then re-trying   post_info_d #:  %s   title: %s...' %(post_num, post_info_d['postTitle']))
                    time.sleep(5)
                
                    
        

        
    #     # check url to use the right downloader
    #     if post_info_d['postURL'].startswith('https://www.you'):
    #         download_youtube_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title, post_info_d_title)
    #     else:
    # #         download_reddit_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title)
    #         pass
        
        

           
if __name__ == '__main__':
    download_vids(70, ['dankvideos'])
    print('done!')
    
    