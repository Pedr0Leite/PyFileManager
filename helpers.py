import os
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move

class DirectoryUtils:
    def __init__(self):
        self.absolute_path = os.path.dirname(__file__)
    
    def get_source_dir(self):
        pwd = os.getcwd()
        with open(f'{self.absolute_path}\source_dir.txt', 'r') as f:
            source_dir = f.readlines()
            return source_dir
        
    def write_new_source_dir(self, new_dir):
        with open(f'{self.absolute_path}\source_dir.txt', 'r') as f:
            f.write(str(new_dir))
            
    def get_folders_names(self):
        with open(f'{self.absolute_path}\folder_names.txt', 'r') as f:
            folder_names = f.readlines()
            return folder_names
    
    def create_new_folder(dest, folder_name):
        path = f'${dest}/${folder_name}'
         
        try: 
            os.mkdir(path)
            print("Directory '% s' created" % path)  
        except OSError as error: 
            print('create_new_folder Error: ' + error)  
    
    def mv_file_to_folder(dest, entry, folder_name):
        if exists(f"{dest}/{folder_name}"):
            return move(entry, dest)
        else:
            DirectoryUtils.create_new_folder(dest, folder_name)
            return DirectoryUtils.mv_file_to_folder(dest, entry, folder_name)

            