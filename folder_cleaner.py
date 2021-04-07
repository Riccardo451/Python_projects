#!/usr/local/bin/python3
import shutil
from time import sleep

# Add /. to the end of folder path if you desire to delete only 
# the content and not the entire folder

dir_paths = ['/Users/riccardo/Desktop/cartella/.','/Users/riccardo/Desktop/cartella2/.','/Users/riccardo/Desktop/cartella3/.']


#########################################################
while 1:
    for path in dir_paths:
        try:
            shutil.rmtree(path)
        except OSError as e:          
            pass
            #print("Error: %s : %s" % (path, e.strerror))
    #print("Cache cleaned")
    
    # Refresh interval in seconds
    sleep(600)
