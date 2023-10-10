# PyFileManager
This python application will organize your download files based on the extensions that you configure on the "extensions_names.txt". There are a bunch of them already there, but feel free to add/remove them as you wish.

## Specific Packages to be installed with pip

* os
* shutil
* datetime
* watchdog
* time

## Main folder to be organized
Create a .txt file called "source_dir.txt" and add, on the first and only line, the URL that you wish the listener to be watching for file changes.

example: 
```sh 
C:\Users\UserName\Downloads
```

## Auto-Run
To make this application automatically running when your computer (windows) starts, you must do the following steps:

1. Press the keys "Win" + R
2. Run the command `shell:startup`
3. Create a `cmd` file with the name you want
4. Inside, add the command to run python on your machine, either `py` or `python` and the full path to run the `main.py` file of this application.

example:
```
py "C:\Users\UserName\Folder\Documents\PythonScripts\PyFileManager\main.py"
```

5. Save it