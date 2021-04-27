# Wallpaper-Carousel-for-Desktop
Automatically downloads Bing Image of the day daily.

## Steps to setup it in your pc
1) Clone/download this repo.
2) Put "Bing Images" folder somewhere in your pc(Ex. in "C:\Users\Public\Pictures").
3) Run setup.exe inside "Bing Image" folder.(Don't change folder location after running this)
4) In Settings -> Personalization -> Background -> Choose albums for your slideshow, click on browse and select "Bing Images" folder.
5) Also set image change frequency as your requirment. Done!

## Working

### downloader.exe
This file downloads bing image of the day and places it in the folder containing downloader.exe file. The images will be downloaded from 'https://bing.gifposter.com' 
(third party website), i don't own any images.

### setup.exe
This file creates a task in windows task scheduler to run downloader.exe daily 2pm(it will run as soon as possible if it misses a run at 2pm).

Note
- Internet connection will be required to download images.
- You have to remove/delete images yourself to limit number images.
- To remove this setup, you can delete the task(name-"Wallpaper_Downloader") in task scheduler.

***Any suggestions are welcomed.***
