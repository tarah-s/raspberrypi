## raspberry-pi (https://github.com/tarah-s/raspberrypi)

Go to Docs for RPI set up

 

### Install PIP 

``` 
sudo apt-get install python-pip
```


### Install python-firebase 

``` 
pip install -e git://github.com/mikexstudios/python-firebase.git#egg=python-firebase
```


### Install MPG321
you can install mpg321 to play mp3 files with command control of the volume
Omxplayer seems to cut short mp3 files, prefer to use MPG321 over Omxplayer

``` 
sudo apt-get -y install mpg321
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

You should now have a list of devices



### Resources
* [RPi Debian Auto Login] (http://elinux.org/RPi_Debian_Auto_Login) 
* [Audio Configuration] (https://www.raspberrypi.org/documentation/configuration/audio-config.md) 
* [Physical computing with Raspberry Pi] (https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/) 
* [Raspberry Pi] (http://openmicros.org/index.php/articles/94-ciseco-product-documentation/raspberry-pi) 
* [gpio_python_code] (https://github.com/allench86/Raspberry-Pi/tree/master/gpio_python_code) 