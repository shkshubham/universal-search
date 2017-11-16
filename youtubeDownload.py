import sys
import youtube_dl
import json
class MyLogger(object):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class Downloader(object):
    def __init__(self):
        settingsFile = open("settings\download.json","r")
        jsonFile = json.loads(settingsFile.read())
        url = jsonFile["option"]["url"]
        videoQuality = jsonFile["option"]["videoQuality"]
        audioQuality = jsonFile["option"]["audioQuality"]
        option = jsonFile["option"]["downloadOption"]
        output = jsonFile["option"]["output"]
        downPath = output+"\\"
        settingsFile.close()

        if videoQuality == 'Very Low':
            quality = '160'+'+bestaudio'

        elif videoQuality == 'Low':
            quality = '133'+'+bestaudio'
            
        elif videoQuality == 'Medium':
            quality = '134'+'+bestaudio'
            
        elif videoQuality == 'High':
            quality = '135'+'+bestaudio'
            
        elif videoQuality == 'HD':
            quality = '136'+'+bestaudio'
            
        elif videoQuality == 'Full HD':
            quality = '137'+'+bestaudio'

        elif videoQuality == '2K':
            quality = '264'+'+bestaudio'
            
        elif videoQuality == '4K':
            quality = '313'+'+bestaudio'
            
        elif videoQuality == 'Best Quality':
            quality = 'bestvideo+bestaudio'

        if audioQuality == '128':
            audio = '140'
        elif audioQuality == '160':
            audio = '251'
        elif audioQuality == 'Best Quality':
            audio = 'bestaudio'
        
        if option == "Audio":
            ydl_opts = {
            'format': audio+'/best',
            'outtmpl': downPath+'%(title)s.%(ext)s',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                }],
            }
        elif option == "Video":            
            ydl_opts = {
            'format': quality+'/best',
            'outtmpl': downPath+'%(title)s.%(ext)s'
            }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            #info_dict = ydl.extract_info(url,download=False)
            #video_title = info_dict.get('title', None)
            #'ffmpeg_location':"codec"
            #'logger':MyLogger(),
Downloader()
