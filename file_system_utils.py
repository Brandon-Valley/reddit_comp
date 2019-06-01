import glob
import os
 
 
 
def get_newest_file_path(dir_path):
    list_of_files = glob.glob(dir_path + '/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    # print (latest_file)
    return latest_file