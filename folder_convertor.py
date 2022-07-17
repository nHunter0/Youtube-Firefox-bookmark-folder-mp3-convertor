from __future__ import unicode_literals
import youtube_dl
import re

config = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3', 
        'preferredquality': '192',
    }],
}

bookmarks = open("bookmark.txt",'r')
BM_heading = bookmarks.readline()
print ("Converting bookmark links for bookmark:", BM_heading) 

"""
Thank you to @brunodles for this youtube regex pattern
Can be found at: https://gist.github.com/brunodles/927fd8feaaccdbb9d02b
"""
pattern = '(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?'

count = 0
num_lines = bookmarks.readlines() 
for line in num_lines:
    url = line.strip()

    #If url is a youtube link 
    if re.match(pattern, url):
        count += 1
        print("\nUrl {}: {}".format(count, url))
        try:
            youtube_dl.YoutubeDL(config).download([url])
        except:
            print("Download unsuccessful") 
    else:
        print (url, "is not a youtube link. Skipped")

bookmarks.close()
