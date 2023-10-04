import os
import helpers
# from watchdog.events import FileSystemEventHandler
from helpers import DirectoryUtils

# class FileMoverHandler(FileSystemEventHandler):
class FileMoverHandler():
    def __init__(self, event):
        self.absolute_path = DirectoryUtils().get_source_dir()
        
        self.when_folder_is_modified(event)
    
    def when_folder_is_modified(self, event):
        # self.absolute_path = DirectoryUtils().get_source_dir()
        # print('Folder was modified! Organizing...')
        # print(f"hey, {event.src_path} has been created!")
        print(f"hey, has been created!")
        # entries = os.scandir(self.absolute_path)

        # for file in entries:
        #     name = file.name
        #     dest = self.absolute_path
        #     print(f'Name: ->  {name}')
            