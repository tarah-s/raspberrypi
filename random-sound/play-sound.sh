#!/bin/bash
# play-sound.sh plays a random sound file on run
# sounds file examples from https://www.reddit.com/r/DotA2/comments/2ulnjy/nba_jam_announcer_megakill_pack_working_with/


# you can install mpg321 to play mp3 files with command control of the volume
# Omxplayer seems to cut short mp3 files, prefer to use MPG321 over Omxplayer
# sudo apt-get -y install mpg321


Sounds="/PATH/TO/FILE/announcer_01.mp3
/PATH/TO/FILE/announcer_02.mp3
/PATH/TO/FILE/announcer_03.mp3
/PATH/TO/FILE/announcer_04.mp3
/PATH/TO/FILE/announcer_05.mp3
/PATH/TO/FILE/announcer_06.mp3
/PATH/TO/FILE/announcer_07.mp3
/PATH/TO/FILE/announcer_08.mp3
/PATH/TO/FILE/announcer_09.mp3
/PATH/TO/FILE/announcer_10.mp3
/PATH/TO/FILE/announcer_11.mp3"
 
sounds=($Sounds)      

num_sounds=${#sounds[*]}   



# osx test
afplay ${sounds[$((RANDOM%num_sounds))]} 



# Default Omxplayer (RPI)

# rpi sound through auto ( hdmi )
# omxplayer ${sounds[$((RANDOM%num_sounds))]}

# rpi forces sound through hdmi
# omxplayer -o hdmi ${sounds[$((RANDOM%num_sounds))]}

# rpi forces sound through audio jack
# omxplayer -o local ${sounds[$((RANDOM%num_sounds))]}



# Using MPG321 (RPI)

# MPG321 with sound percentage control
# mpg321 -g 100 ${sounds[$((RANDOM%num_sounds))]}