import os
import datetime
import sys
import subprocess
import time

def Record2file():
   date = datetime.datetime.now()
   date = date.isoformat()
   date = date[0:10]

   link = input("Enter Link Without HTTP header >> ")
   filename = "P:/FootballGames/" + date +".mp4"
                
   # start livestreamer process
   subprocess.call(["livestreamer",  "hls://"+link, "best","-o", filename])

   print("Recording stream is done. Fixing video file.")
   
   time.sleep(10)
  # subprocess.call(["taskkill /IM livestreamer.exe"])
Record2file()
