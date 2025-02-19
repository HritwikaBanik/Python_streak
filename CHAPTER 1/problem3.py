import os             #imported OS module to perform content checking inside directories
directory_path = 'C:/Users'                #path to directory
directory_content =  os.listdir(directory_path)    #os.listdir() helps to read the contents of a directory
print("Contents of the directory:")
for item in directory_content:     #using for loop to display all the list of directories
    print(item)