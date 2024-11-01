from TikTokApi import TikTokApi
import requests
from urllib.error import HTTPError

class TikTok:
    def __init__(self, url):
        self.url = url
        self.api = TikTokApi()
        try:
            self.video_data = self.api.video(url=url).info()
            self.title = self.video_data['desc']
            self.thumbnail = self.video_data['video']['cover']
        except Exception as e:
            print(f"Error accessing video details: {e}")
            self.title = "Unknown Title"
            self.thumbnail = None

    def download(self, output_path):
        try:
            video_url = self.video_data['video']['playAddr']
            response = requests.get(video_url, stream=True)
            response.raise_for_status()
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Video downloaded successfully to {output_path}")
        except HTTPError as e:
            print(f"HTTP Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage
tiktok = TikTok('https://www.tiktok.com/@scout2015/video/6718335390845095173')
tiktok.download(r"C:\Users\conta\Videos\TikTok\video.mp4")