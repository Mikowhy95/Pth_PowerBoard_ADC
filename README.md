# Pth_PowerBoard_ADC
Python code for testing PowerBoard's ADC on Husarion Panther v1.2 devel 

# The Orign
The idea of a code for testing ADC goes from https://github.com/radeknh/power-board repo.
Currently I couldn't find a way to configure two dtoverlays what originaly was made by puting
```
dtoverlay=ads1015,addr=0x48
dtoverlay=ads1015,addr=0x49 
```
in */boot/config.txt* file.
Command *ls /sys/bus/iio/devices/* always says that there is only one device. Well, this is consistient to https://forums.raspberrypi.com/viewtopic.php?t=149244

Finally, I came to the conclusion that the fastest way is to write new test code, Python for example, based on the original (C language) using proven libraries.

# Python code
This is just simple Python code, strongly commented. Just clone it, run it and enjoy :)

```
git clone https://github.com/Mikowhy95/Pth_PowerBoard_ADC.git
```
```
python Pth_PowerBoard_ADC/read_adc.py
```

# Back to the beginning
Anyway, if there is a solution for using two ADS1015 via dtoverlay here is complited configuration:

```
dtoverlay=ads1015
dtparam=addr=0x48
dtparam=cha_enable=true
dtparam=chb_enable=true
dtparam=chc_enable=true
dtparam=chd_enable=false
dtparam=cha_gain=2
dtparam=chb_gain=1
dtparam=chc_gain=2

dtoverlay=ads1015
dtparam=addr=0x49
dtparam=cha_enable=true
dtparam=chb_enable=true
dtparam=chc_enable=true
dtparam=chd_enable=true
dtparam=cha_gain=1
dtparam=chb_gain=1
dtparam=chc_gain=1
dtparam=chd_gain=1
```