#!/usr/bin/env python
# AnySubtitleDownloader.py

__author__ = "Jai Singhal"
__copyright__ = "Copyright 2017"
__version__ = "1.0.1"
__maintainer__ = "Jai Singhal"
__email__ = "jaisinghal48@gmail.com"
__website__ = "http://jaisinghal.com"
__github_repo__ = "https://github.com/jai-singhal/subtitle-downloader"

#Imports
import sys
import os
import hashlib
import urllib.request


#api
#this hash function receives the name of the file and returns the hash code
def get_hash(name):

    """

    #######################
    SUBTITLE DOWNLOADER API
    ########################

    source : http://thesubdb.com/api/

    work: returns hashcode of a file name, when provide a video file name, it converts to
            unique hash which is matched in subtitle db
    
    arguement: file name of a video file

    Returns the hash code of given file
    
    """
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()



def subtitle_downloader(file_path):  

    """
    
    ######################
     To Download Subtitle
    ######################
    
    Creates a "srt" file of the name same as the media file name
    
    arguement: absolute path of file

    Returns None

    """
    try:
        media_file = file_path.split("\\")[-1]

        language = "&language=en"
        try:
            hash_media = get_hash(file_path)
        except:
            print("Not able to find the media")
            return
        url = "http://api.thesubdb.com/?action=download&hash=" + hash_media + language
        headers = {'User-Agent': 'SubDB/1.0 (subtitle-downloader/1.0;'}

        req = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(req).read()

        media_file_name = media_file[0:-4]
        current_path = os.getcwd()
        output_srt_file_name = current_path + "\\" +media_file_name + ".srt"

        srt_file_out = open(output_srt_file_name, "wb")
        srt_file_out.write(response)
        srt_file_out.close()
        print("Download Completed")
    except:
        print("Download Unsuccessful")
        input("Press any key to exit")


def main():

    """
    Main function

    takes a system arguement

    """
    file_path = sys.argv[1]
    subtitle_downloader(file_path)


if __name__ == "__main__":
    main()
    