from pathlib import Path

searchString = ''

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
detectedFiles = []
def targetFile():
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

selectedFile = targetFile()

def searchFile(selectedFile):
    searchPath = Path(input('Please enter path to search: '))

    if not searchPath.exists() or not searchPath.is_dir():
        print("The path does not exist or is not a directory. Exiting search.")
        return

    for file_path in searchPath.rglob('*'):
     if file_path.suffix.upper() == selectedFile[1:]: 
        file_path = list(detectedFiles.append(file_path))
        print(detectedFiles)

searchFile(selectedFile)  