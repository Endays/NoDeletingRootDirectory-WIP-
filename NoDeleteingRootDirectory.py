
def fileInput():
    print("Please Input a file to scan:")
    file = file.input('')
    return file

fileName = fileInput()

def scanFile(fileName):
    message = f"would you like to scan {fileName}"
    print(message)
    while True:
     choice = input('[Y/N]')
     if (choice != 'y' and choice != 'n'):
        print("Invalid input")
        pass
     else: 
         if(choice == 'y'):
          print("Yes Input")
          break
         else:
           if(choice == 'n'):
              print("Input No")
              fileInput()
               
   
scanFile(fileName)




