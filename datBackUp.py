import os
import shutil
import pathlib
import sys
from datetime import datetime

originFolders = ['X:\\ITM','E:\\source','X:\\Writing']
backUpLocations = ['D:\\backup','F:\\backup']

def backUpFile(file_path,backUp_file_path):
    try:
        if not os.path.exists(os.path.dirname(backUp_file_path)):
            os.makedirs(os.path.dirname(backUp_file_path))
        shutil.copy2(file_path, backUp_file_path)
        print('Copied: '+file_path)
    except PermissionError:
        print(f'Permission denied when copying {file_path}')


print('BackUp of ',originFolders.count,' location(s) starting at ',datetime.now())

for originFolder in originFolders:
    #goes through every location you want to backup
    count = 0
    for dirpath, dirnames, filenames in os.walk(originFolder):
        #goes through every file
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            #goes through every backUpLocation
            for backUpLocation in backUpLocations:
                
                
                backUp_file_path = backUpLocation+file_path.replace(os.path.dirname(originFolder),'\\')
                #Checks if the file exists in the backupFolder
                if not os.path.exists(backUp_file_path):
                    backUpFile(file_path,backUp_file_path)
                #Checks if the modified date of the backup File is older than the original File
                elif os.path.getmtime(backUp_file_path)<os.path.getmtime(file_path):
                    backUpFile(file_path,backUp_file_path)
            count=count+1
            sys.stdout.write('\r\r'+str(count)+' files processed from '+originFolder)

print('BackUp of ',originFolders.count,' location(s) finished at ',datetime.now())