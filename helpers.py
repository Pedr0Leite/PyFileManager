import os
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from datetime import datetime

class DirectoryUtils:
    def __init__(self):
        self.absolute_path = os.path.dirname(__file__)
    
    def get_source_dir(self):
        with open(f'{self.absolute_path}\source_dir.txt', 'r') as f:
            source_dir = f.readlines()
            return source_dir
        
    def write_new_source_dir(self, new_dir):
        with open(f'{self.absolute_path}\source_dir.txt', 'w') as f:
            f.write(str(new_dir))
            
    def get_folders_names(self):
        with open(f'{self.absolute_path}\folder_names.txt', 'r') as f:
            folder_names = f.readlines()
            return folder_names
    
    def get_extensions_names(self):
        with open(f'{self.absolute_path}\extension_names.txt', 'r') as f:
            extensions_names = f.readlines()
            return extensions_names
    
    def create_new_folder(dest, folder_name):
        path_of_new_folder = f'{dest}\{folder_name}'
         
        try: 
            os.mkdir(path_of_new_folder)
            print("Directory '% s' created" % path_of_new_folder)  
        except OSError as error: 
            print('create_new_folder Error: ' + error)  
    
    def mv_file_to_folder(path, file_name, folder_name, special_extension=False):
        
        if special_extension:
            folder_name = 'Other'
        
        if exists(f"{path}\{folder_name}"):
            destination = f"{path}\{folder_name}"
            file_path = f"{path}\{file_name}"
            
            _, _, files_inside_folder = next(os.walk(destination))
            
            if file_name in files_inside_folder:
                now = datetime.now()
                date_time = now.strftime("%m.%d.%Y_%HH%MM%SS")
                ext_list = file_name.split('.')
                extension = ext_list[len(ext_list) - 1]
                ext_list.pop()
                new_file_name_temp = ''
                new_file_name_temp = new_file_name_temp.join(ext_list)
                
                new_file_name =  f'{new_file_name_temp}_{date_time}.{extension}'
                new_file_name_path = f'{path}\\{new_file_name}'
                
                os.rename(file_path, new_file_name_path)
                file_name = new_file_name
                file_path = f"{path}\{file_name}"
            
            return move(file_path, destination)
            
        else:
            DirectoryUtils.create_new_folder(path, folder_name)
            return DirectoryUtils.mv_file_to_folder(path, file_name, folder_name)

            