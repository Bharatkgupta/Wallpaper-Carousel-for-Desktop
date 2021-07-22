# Wallpaper-Carousel-for-Desktop
Automatically downloads Bing Image of the day daily.

Requiremrnt: Python 3.X

## Steps to setup it in your pc
1) Clone this repo.
2) Put "Bing Images" folder somewhere in your pc(Ex. in "C:\Users\Public\Pictures").
3) Run setup.exe inside "Bing Image" folder and Enter your Python PATH i.e where your python.exe file is located.
(Don't change "Bing Image" folder location after running this)
4) In PC Settings -> Personalization -> Background -> Choose albums for your slideshow, click on browse and select "Bing Images" folder.
5) Also set image change frequency as your requirment. Done!

## Working

### downloader.py
This script downloads 'bing image of the day' and places it in the folder containing downloader.py file. The images will be downloaded from 'https://bing.gifposter.com' , I don't own any images.

### setup.exe
This file creates a task in windows task scheduler to run downloader.py daily 2pm(it will run as soon as possible if it misses a run at 2pm).

Note
- Internet connection will be required to download images.
- You have to remove/delete images yourself to limit number of images.
- To remove this setup, you can delete the task(name-"Wallpaper_Downloader") present in windows task scheduler and delete related files.

***Any suggestions are welcomed.***
