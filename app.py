from pytube import YouTube, streams
from pytube.extract import video_info_url


url = input("Introduce the URL Here:")
yt = YouTube(url)
print(yt.title)
print("Downloading...")


#YouTube(url).streams.get_highest_resolution().download()
#YouTube(url).streams.get_audio_only().download(r"/home/square/Desktop/Downloader")
YouTube(url).streams.get_highest_resolution().download(r"/home/square/Downloads")

print("The download was finished succesfully!!")
