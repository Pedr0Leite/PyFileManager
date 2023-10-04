import os
import sys
import time
import logging

from time import sleep

from helpers import DirectoryUtils
from file_mover_handler import FileMoverHandler

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

# confirmation = input('Use current saved source? If not, saved will be erased [y/n]\n')

# if confirmation == 'y':
#     source_dir = DirectoryUtils().get_source_dir()

#     if len(source_dir) == 0:
#         new_source = input('No source directory saved, please create a new one: \n')
#         DirectoryUtils.write_new_source_dir(new_source)
        
#         source_dir = DirectoryUtils().get_source_dir()
    
# else:
#     open('source_dir.txt', 'w').close()
#     new_source = input('Please insert the new directory: ')
#     DirectoryUtils().write_new_source_dir(new_source)
        
#     source_dir = DirectoryUtils().get_source_dir()    

source_dir = DirectoryUtils().get_source_dir()

if len(source_dir) == 0:
    new_source = input('No source directory saved, please create a new one: \n')
    DirectoryUtils().write_new_source_dir(new_source)
        
    source_dir = DirectoryUtils().get_source_dir()
     

# # Listener part
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
    
#     path = source_dir[0]
#     # event_handler = FileMoverHandler().when_folder_is_modified()
#     event_handler = FileMoverHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
    
#     try:
#         while True:
#             sleep(5)
#             print('Running again')
#     except KeyboardInterrupt:
#             observer.stop()
#     observer.join()


if __name__ == "__main__":
    patterns = ["*"]
    path = source_dir[0]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_created(event):
        print(f"hey, {event.src_path} has been created!")
        
    my_event_handler.on_created = on_created
    # my_event_handler.on_created = FileMoverHandler(my_event_handler)
    
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(5)
            print('Running again')
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
