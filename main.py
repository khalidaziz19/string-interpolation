from PIL import Image
from glob import glob
import os

# string interpolation for multiple data
# folder directory
folderPath = os.chdir('C:\\Users\\HP\Desktop\\string interpolation\\Surgical tray\\Accessories and implants')

value = 1
for images in os.listdir(folderPath):

    # new file name with sequence number
    new_image_name = "Accessories_and_implants{}.jpg".format(value)
    # convert old files name into new files name
    os.renames(images, new_image_name)
    value = value + 1
