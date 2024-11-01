import instaloader
import os
import platform
import requests

loader = instaloader.Instaloader()

class InstaDL:
    def __init__(self, url):
        self.url = url
        self.shortcode = url.split("/")[-2]
        
        self.video = instaloader.Post.from_shortcode(loader.context, self.shortcode)


        # Récupérer la légende et l'URL de la miniature
        self.caption = self.video.caption if self.video.caption else "Unknown Title"
        self.thumbnail = self.video.url

        
        # Définir le chemin de téléchargement en fonction du système d'exploitation
        if platform.system() == 'Windows':
            self.download_path = os.path.join(os.getenv('USERPROFILE'), 'Pictures', 'instagram')
        elif platform.system() in ['Linux', 'Darwin']:
            self.download_path = os.path.join(os.getenv('HOME'), 'Pictures', 'instagram')
        else:
            self.download_path = '/sdcard/Pictures/instagram'

        # Créer le dossier de téléchargement s'il n'existe pas
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def download(self):
        try:
            # Récupérer l'URL de la vidéo
            video_url = self.video.video_url
            video_path = os.path.join(self.download_path, f"{self.shortcode}.mp4")

            # Télécharger la vidéo
            response = requests.get(video_url, stream=True)
            response.raise_for_status()  # Vérifie si la requête a réussi

            # Écrire le fichier vidéo
            with open(video_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print("Vidéo téléchargée avec succès :", video_path)
        except Exception as e:
            print("Erreur lors du téléchargement de la vidéo :", e)


if __name__ == "__main__":
    # Utilisation de la classe
    yt = InstaDL("https://www.instagram.com/cats_of_instagram/reel/DBv9Lo8zuGe/?hl=fr")
    print(yt.caption)
    print(yt.thumbnail_url)
    yt.download()
