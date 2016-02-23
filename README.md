## raspberry-pi (https://github.com/tarah-s/raspberrypi)

Go to Docs for RPI set up



### Install PIP

```
sudo apt-get install python-pip
```


### Install python-firebase

```
sudo apt-get install python-dev
sudo pip install requests
sudo pip install python-firebase
```


### Install MPG321
you can install mpg321 to play mp3 files with command control of the volume Omxplayer
seems to cut short mp3 files, prefer to use MPG321 over Omxplayer. If the sound is
available you may need to turn the volume up in the playsound.sh file changing
default 100 to a higher percentage.

```
sudo apt-get -y install mpg321
```



### Auto Start scripts
Launch terminal on startup

Pi 1
```
sudo vim /etc/xdg/lxsession/LXDE/autostart

```

Pi 2
```
sudo vim /etc/xdg/lxsession/LXDE-pi/autostart

```

run terminal on startup
```
@lxterminal

```

update .bashrc file
```
sudo vim .bashrc

```

at the end of the bash rc file add the bash scripts you would like to run
```
sh ~/PATH/script.sh

```

### Structure

start up
```
- /home/pi/STARTFOLDER
  - start.sh
  - audiofix.sh
```

program
```
- /home/pi/Desktop/PROJECTFOLDER/
  - SOUNDSFOLDER
  - playsound.sh
  - program.py
```



### Install Temp/Humidity sensor

```
sudo vim /boot/config.txt
```

add the following line to the bottom and reboot

```
dtoverlay=w1-gpio

```

The above step usually needs to take place before the following so we can detect devices

```
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls -l
```

### Resources
* [RPi Debian Auto Login] (http://elinux.org/RPi_Debian_Auto_Login)
* [Audio Configuration] (https://www.raspberrypi.org/documentation/configuration/audio-config.md)
* [Physical computing with Raspberry Pi] (https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/)
* [Raspberry Pi] (http://openmicros.org/index.php/articles/94-ciseco-product-documentation/raspberry-pi)
* [gpio_python_code] (https://github.com/allench86/Raspberry-Pi/tree/master/gpio_python_code)
* [SSH into Pi] (https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)
* [Start up scripts] (http://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up)
* [On boot scripts] (https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)
