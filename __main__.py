import os

#grabbing the directory where the files are
target_directory = os.listdir('D:/DEV/Python/Projects/renaming-bulk-files/test')

def Renamer():
    # counter so that we may order them from 0 to 6
    counter = 0

    #grabbing every file in there
    for file in target_directory:

        #defining the new name for each file
        new_name = f"D:/DEV/Python/Projects/renaming-bulk-files/test/Changed!{counter}.lmao"

        #storing the file in a variable
        current_name = f"D:/DEV/Python/Projects/renaming-bulk-files/test/{file}"

        #renaming them
        os.rename(current_name, new_name)
        
        counter += 1

Renamer()