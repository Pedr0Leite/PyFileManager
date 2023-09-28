import os
import helpers
from watchdog.events import FileSystemEventHandler

class FileMoverHandler(FileSystemEventHandler):
    def when_folder_is_modified(source_dir):
        entries = os.scandir(source_dir)
        # entries = os.listdir(str(source_dir))

        for file in entries:
            name = file.name
            dest = source_dir
            print(f'Name {name}! This is the dest {source_dir}')