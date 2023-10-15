from pytube import YouTube
import os
# url input from user
yt = YouTube (input("Enter the URL of the video you want to download: \n>> "))
# extract only audio
video = yt.streams.filter (only_audio=True). first()


# download the file
out_file = video.download ()
# save the file
base, ext = os.path.splitext (out_file)
new_file = base + '.wav'
os. rename (out_file, new_file)
# result of success
print (yt.title + " has been successfully downloaded.")