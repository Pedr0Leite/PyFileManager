import os
import sys
import time
import logging

from helpers import DirectoryUtils
from file_mover_handler import FileMoverHandler
import watchdog

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


confirmation = input('Use current saved source? If not, saved will be erased [y/n]')

if confirmation == 'y':
    source_dir = DirectoryUtils.get_source_dir()

    if len(source_dir) == 0:
        new_source = input('No source directory saved, please create a new one: ')
        DirectoryUtils.write_new_source_dir(new_source)
        
        source_dir = DirectoryUtils.get_source_dir()
else:
    open('source_dir.txt', 'w').close()
    new_source = input('Please insert the new directory: ')
    DirectoryUtils.write_new_source_dir(new_source)
        
    source_dir = DirectoryUtils.get_source_dir()
    


# # Listener part
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.isAlive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()