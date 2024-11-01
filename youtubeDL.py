import pytubefix as pytube
import os
import platform

class YouTubeDL:
    def __init__(self, url):
        self.url = url
        self.video = pytube.YouTube(url)
        
        try:
            self.title = self.video.title
            self.thumbnail = self.video.thumbnail_url
        except :
            print("Error: Could not get video title or thumbnail")
            self.title = "Unknown Title"
            self.thumbnail = None

        
         
        if platform.system() == 'Windows':
            self.download_path = os.path.join(os.getenv('USERPROFILE'), 'Pictures', 'youtube')
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            self.download_path = os.path.join(os.getenv('HOME'), 'Pictures', 'youtube')
        else:
            self.download_path = '/sdcard/Pictures/youtube'  

        #
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def download(self):
        self.video.streams.get_highest_resolution().download(self.download_path)

    


yt = YouTubeDL("https://www.youtube.com/watch?v=9bZkp7q19f0")
print(yt.title) 
print(yt.thumbnail)
yt.download()