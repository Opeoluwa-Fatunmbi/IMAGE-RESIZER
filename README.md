# IMAGE-RESIZER


This script will look for all files with .jpg or .png extension in the directory passed in and resize them to the size specified in the size variable,
and then save them in the same directory with "resized_" prefixing the original filename.

The script uses the os.listdir() function to get a list of all files in the directory,
and the PIL.Image.open() function to open an image file. The resize() method is then used to resize the image,
and the save() method is used to save the resized image to disk.

Please note that this script will overwrite the original images. 
If you want to keep the original images and save the resized images with new names, you can modify the script accordingly.
