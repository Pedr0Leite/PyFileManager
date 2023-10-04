import os
from helpers import DirectoryUtils

class RunInitialMover():
    def __init__(self):
        self.absolute_path = DirectoryUtils().get_source_dir()
        self.run_first_time()
        
    def run_first_time(self):
        entries = os.scandir(self.absolute_path[0])

        for file in entries:
            name = file.name
            dest = self.absolute_path[0]
            ext_list = file.name.split('.')
            extension = ext_list[len(ext_list) - 1]
            print(f'Name: ->  {name} ||| Extension: -> {extension}')