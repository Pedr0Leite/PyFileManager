from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move

class DirectoryUtils():
    def get_source_dir():
        with open('source_dir.txt', 'r') as f:
            source_dir = f.readlines()
            return source_dir
        
    def write_new_source_dir(new_dir):
        with open('source_dir.txt', 'w') as f:
            f.write(str(new_dir))
            
    def get_folders_names():
        with open('folder_names.txt', 'r') as f:
            folder_names = f.readlines()
            return folder_names
    
    def create_new_folder():
        pass 
    
    def mv_file_to_folder(dest, entry, folder_name):
        if exists(f"{dest}/{folder_name}"):
            return move(entry, dest)
        else:
            DirectoryUtils.create_new_folder()
            return DirectoryUtils.mv_file_to_folder(dest, entry, folder_name)

            