from pytube import YouTube, streams
from pytube.extract import video_info_url
from progress.bar import Bar, IncrementalBar



url = input("Enter URL Here: ")
yt = YouTube(url)
print(yt.title)

bar = IncrementalBar('Processing', suffix='%(percent)d%%')
for i in range(100):
    # Download function with progressive bar en porcentaje 
    yt.streams.get_highest_resolution().download(r"/home/square/Pictures/Videos") 
    bar.next()
bar.finish()

print("The download was finished succesfully!!")


# (r"/home/square/Desktop/Downloads")


# Example Code
#YouTube(url).streams.get_highest_resolution().download()
#YouTube(url).streams.get_audio_only().download()
#YouTube(url).streams.get_highest_resolution().download(r"/home/square/Downloads")

# Normal Download Functions
#YouTube(url).streams.get_audio_only().download(r"/home/square/Desktop/Music")
#YouTube(url).streams.get_highest_resolution().download(r"/home/square/Videos")

