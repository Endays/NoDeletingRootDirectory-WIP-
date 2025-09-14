from pathlib import Path
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
 

searchString = '# enter search string here'

fileTypes = {
    1: '*.TXT',
    2: '*.PDF',
    3: '*.MD',
    4: '*.EXE',
    5: '*.PY',
    6: '*.SH',
    7: '*.PDF',
    8: '*.JPG',
    9: '*.MP4',
    0: '*.DOCZ',   
}
def findfile():
    while True:
        for key in sorted(fileTypes):
            print(f"{key}: {fileTypes[key]}")

        userInput = input('Choose a file type: ')
        if userInput.isdigit():
            result = fileTypes.get(int(userInput))
            if result:  
                print(f"You selected: {result}")
                return result  
            else:
                print("Invalid number, please choose from the menu.")
        else:
            print("Invalid input, please enter a number from the menu.")

selectedFile = findfile()

def searchFile(selectedFile):
    detectedFiles = []
    searchPath = Path(input('Please enter path to search: '))

    if not searchPath.exists() or not searchPath.is_dir():
        print("The path does not exist or is not a directory. Exiting search.")
        return

    for file_path in searchPath.rglob('*'):
     if file_path.suffix.upper() == selectedFile[1:]: 
        detectedFiles.append(file_path)
    if detectedFiles:
        print(detectedFiles)
    else:
        print("no detected files")
    return detectedFiles
        
    
detectedFiles = searchFile(selectedFile)
    
def scanFile(detectedFiles, searchString):
    for file in detectedFiles:
     try: 
         with open(file, 'r') as f:
          for line_number, line in enumerate(f, 1):
           if searchString in line:
            print(f"{searchString} found on line {line_number}: {line.strip()} in file {file}")
     except: 
      print("string not found in file")
    return
 
 
scanFile(detectedFiles, searchString)
