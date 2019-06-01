
import dl_utils
# import template
VIDS_TO_COMPILE_FOLDER_PATH = 'vids_to_compile'


print('  Trying to download video...')
try:
    dl_utils.download_youtube_vid("https://youtu.be/wFnw5EVGOiI", VIDS_TO_COMPILE_FOLDER_PATH, 'post_111')
except Exception as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print('  Video unavailable:  ', message)