import hashlib
from imageio import imread
import PIL
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import time
import numpy as np
import os
import glob
import cv2


#
# images = [cv2.imread(file) for file in
#           glob.glob("C:\\Users\\HP\\Desktop\\string-interpolation\\dataset\\undefined")]
#
#
#
# def file_hash(filepath):
#     with open (filepath, 'rb') as f:
#         return md5(f.read()).hexdigest()
#     os.getcwd()
#     os.chdir('C:\\Users\\HP\\Desktop\\string-interpolation\\dataset\\undefined')
#     os.getcwd()
# file_list = os.listdir()
# print(len(file_list))

#
# from PIL import Image
# from glob import glob
# import os
#
# # string interpolation for multiple data
# # folder directory
# folderPath = os.chdir('C:\\Users\\HP\\Desktop\\string-interpolation\\dataset\\Surgical tray\\undefiend')
#
# value = 0
# for img in os.listdir(folderPath):
#     new_image_name = "asdf.jpg".format(value)
#     # convert old files name into new files name
#     os.renames(img, new_image_name)
#     value = value + 1


# Function to rename multiple files
def main():
    folder = "C:/Users/HP/Desktop/Office work/iPhone-Videos-DataSet/Disection Clamp"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"frames{str(count)}.jpg"
        src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst = f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
