import os
import shutil

REPLACEMENTPATH = 'D:\\Unity Projects\\Symposium Demo Shared SA\\Assets\\All_Defect_Resources\\'

success = False

while not success:
    answer = input("Unity MUST BE CLOSED in order for this script to work. Please check to ensure it is closed!\n\nIs Unity closed (y/n)? ")
    if answer == "y":
        print("Copying and Overwriting SVG files from this folder to " + REPLACEMENTPATH + "...")

        #find files
        fileList = os.listdir()
        svgList = [x for x in fileList if len(x) > 4 and x[-4:] == ".svg"]

        #copy files over
        for svg in svgList:
            shutil.copy(svg,REPLACEMENTPATH)

        print("Done!")
        success = True

    elif answer == "n":
        success = True

    else:
        print("Invalid Response")