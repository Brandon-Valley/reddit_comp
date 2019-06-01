# pip install --upgrade --force-reinstall pytube

from selenium import webdriver

import file_system_utils
import get_post_info_dl
import dl_utils

import testing_utils

PHANTOM_JS_PATH = 'C:/Users/Brandon/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe' ## SET YOU PATH TO phantomjs

VIDS_TO_COMPILE_FOLDER_PATH = 'vids_to_compile'

MAX_CLIP_DURATION = 45 # seconds




def download_vids(num_posts, subreddit_list):
    print('  Getting post_info_dl...')
    post_info_dl = get_post_info_dl.get_post_info_dl(num_posts, subreddit_list)

    # set up browser
    print('  Setting up phanomJS browser (needed for some vid duration stuff)...')
    driver = webdriver.PhantomJS(PHANTOM_JS_PATH)

    print('  Deleting all files in %s...' %(VIDS_TO_COMPILE_FOLDER_PATH))
    file_system_utils.delete_all_files_in_dir(VIDS_TO_COMPILE_FOLDER_PATH)

    for post_num, post_info_d in enumerate(post_info_dl):
        if post_info_d['postType'] != None:
            print('  Skipping post#: %s because its postType = %s ...' %(post_num, post_info_d['postType']))
            continue
        
        testing_utils.print_str_wo_error("  Checking duration of post_info_d #:  %s   title: %s..." %(post_num, post_info_d['postTitle']))
        
        # test to see if you can tell how long the vidoe will be before
        # you start trying to download it, if you can tell, compare it 
        # to the MAX_CLIP_DURATION to see if it makes it in
        driver.get(post_info_d['postURL'])
        vid_duration = dl_utils.get_vid_duration(driver, post_info_d['postURL'])
        if vid_duration == False:
            print('    Could not get video duration')
        elif int(vid_duration) > MAX_CLIP_DURATION:
            print('    Video too long!')
            continue
        
        
        vid_save_title = 'post_' + str(post_num)#post_info_d.title.replace(" ", "_") # cant have spaces in the filenames
        
        
        print('  Trying to download video...')
        try:
            dl_utils.download_youtube_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH, vid_save_title)
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print('  Video unavailable:  ', message)
            continue
        
#         # delete video if its too long
#         vid_save_path = VIDS_TO_COMPILE_FOLDER_PATH + '/' + vid_save_title + '.mp4'
#         if dl_utils.get_vid_length(vid_save_path) > MAX_CLIP_DURATION:
#             print('  Video too long, deleting video...')
#             os.remove(vid_save_path)
        
    #     # check url to use the right downloader
    #     if post_info_d['postURL'].startswith('https://www.you'):
    #         download_youtube_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title, post_info_d_title)
    #     else:
    # #         download_reddit_vid(post_info_d['postURL'], VIDS_TO_COMPILE_FOLDER_PATH + '/' + post_info_d_title)
    #         pass
        
        

           
if __name__ == '__main__':
    download_vids(50, ['dankvideos'])
    print('done!')
    
    