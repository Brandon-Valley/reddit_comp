import glob
import os
# import shutil
 
 
def get_newest_file_path(dir_path):
    list_of_files = glob.glob(dir_path + '/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    # print (latest_file)
    return latest_file


def delete_all_files_in_dir(dir_path):
    for the_file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
            
def get_relative_path_of_files_in_dir(dir_path, file_type):
    # Getting the current work directory (cwd)
    thisdir = os.getcwd()
    
    path_list = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(dir_path):
        for file in f:
            if file_type in file:
#                 print(os.path.join(r, file))
                path_list.append(os.path.join(r, file))
    return path_list
            
            
            
import download_vids
if __name__ == '__main__':
#     download_vids.download_vids(20, ['videomemes'])
    print(get_relative_path_of_files_in_dir('vids_to_compile', '.mp4'))






