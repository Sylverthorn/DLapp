import pytubefix as pytube



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

    def download(self):
        self.video.streams.get_highest_resolution().download()



yt = YouTubeDL("https://www.youtube.com/watch?v=9bZkp7q19f0")
print(yt.title) 
print(yt.thumbnail)