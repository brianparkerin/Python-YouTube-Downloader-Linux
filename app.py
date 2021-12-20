from pytube import YouTube, streams
from pytube.extract import video_info_url


url = input("Introduce the URL Here:")
yt = YouTube(url)
print(yt.title)
print("Downloading...")


# Example Code
#YouTube(url).streams.get_highest_resolution().download()
#YouTube(url).streams.get_audio_only().download()
#YouTube(url).streams.get_highest_resolution().download(r"/home/square/Downloads")

# Normal Download Functions
YouTube(url).streams.get_audio_only().download(r"/home/square/Desktop/Music")
YouTube(url).streams.get_highest_resolution().download(r"/home/square/Videos")

print("The download was finished succesfully!!")
