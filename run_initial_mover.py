import os
from helpers import DirectoryUtils

class RunInitialMover():
    def __init__(self):
        self.absolute_path = DirectoryUtils().get_source_dir()
        self.run_first_time()
        
    def run_first_time(self):
        entries = os.scandir(self.absolute_path[0])

        for file in entries:
            special_extension = False
            file_name = file.name
            dest = self.absolute_path[0]
            ext_list = file.name.split('.')
            extension = ext_list[len(ext_list) - 1]
            file_path = f'{dest}\\{file_name}'
            replace_bars = lambda x: x.replace("\n", "")
            file_extensions_temp = DirectoryUtils().get_extensions_names()
            file_extensions = list(map(replace_bars, file_extensions_temp))
            
            if extension not in file_extensions:
                special_extension = True
            
            if os.path.isfile(file_path):
                DirectoryUtils.mv_file_to_folder(dest, file_name, extension.capitalize(), special_extension)