================
pybluez-examples
================
Example Bluetooth tasks using the Python PyBluez module.
Tested on Raspberry Pi 2 with CSR bluetooth 4.0 USB adapter & Bluez 5

.. contents::

Prereqs
=======
::

    sudo apt-get install libbluetooth-dev bluez bluez-hcidump  libboost-python-dev libboost-thread-dev libglib2.0-dev

    pip install pybluez gattlib

    sudo adduser lp $(whoami)
    sudo reboot

Scanning for bluetooth devices from Python 
==========================================
using pybluez::

    python blueztools.py

If you get OSError: No such device  you may not be finding your bluetooth adapter. Try enabling it via::

    sudo hciconfig hci0 up

one-time pairing
================
optional commands commented out, with Bluez 5, we use the bluetoothctl agent::

    #sudo hciconfig hci0 up   #enables bt on computer
    #hcitool scan  # gets UUID of devices in pairing mode
    #hcitool dev # get BT adapter uuid

    bluetoothctl -a  #starts interactive prompt
    scan on          #scans for UUID of device (BT and BLE) in pairing mode
    pair uuid        # where "uuid" is what you found with scan 
    trust uuid
    connect uuid    # after pairing, this is how you connect in the future
    
Notes
=====
If you get the message "Creating device failed: org.bluez.Error.AuthenticationRejected: Authentication Rejected", then:: 

    sudo nano /etc/bin/bluez-simple-agent

and change "KeyboardDisplay" to "DisplayYesNo"
(thanks to http://www.wolfteck.com/projects/raspi/iphone/)

Also try::

    bluez-test-device trusted <speaker uuid> yes


If connected but lacking sound try::

    nano ~/.asoundrc

paste in::   

    pcm.btspkr {
       type plug
       slave {
           pcm {
               type bluetooth
               device "AA:BB:CC:DD:EE:FF"
               profile "auto"
           }   
       }   
       hint {
           show on
           description "BT Speaker"
       }   
    }
    ctl.btspkr {
      type bluetooth
    }  

    pcm.btspkr_softvol
    {
       type softvol
       slave.pcm "btspkr"
       control.name "Bluetooth"
       control.card 0
    }

    # Using bluetooth as default : 
    pcm.!default {
        type plug
        slave.pcm "btspkr_softvol"
    }

(thanks https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=570468)

to connect 
==========
(note, in ubuntu it disconnects after a second, maybe because system
bluetooth menu is overriding with "off"::

    sudo hcitool cc <uuid>


Errors
=======
Cannot open shared library /usr/lib/arm-linux-gnueabihf/alsa-lib/libasound_module_pcm_bluetooth.so::

    sudo apt-get install bluez-alsa



bt_audio_service_open: connect() failed: Connection refused (111)::

    sudo nano /etc/bluetooth/audio.conf

paste in::

    [general]
    Enable=Sink,Source,Socket
    Disable=Media

    AutoConnect=true
    SCORouting=PCM


then::

     sudo service bluetooth restart

Picking the Bluetooth speaker as default audio device
=====================================================
First test it works with::

    mpg321 -a bluetooth  myfile.mp3

or::

    mplayer -ao alsa:device=bluetooth myfile.mp3


Then, list your audio ALSA devices with::

    aplay -L
 
and you can use::
   
    alsamixer


References
==========

https://bitbucket.org/OscarAcena/pygattlib

https://wiki.archlinux.org/index.php/bluetooth_keyboard

https://github.com/oz123/dude/blob/master/bin/speakersswitcher.sh

http://blog.scphillips.com/2013/01/sound-configuration-on-raspberry-pi-with-alsa/


https://wiki.debian.org/Bluetooth/Alsa

http://www.raspberrypi.org/forums/viewtopic.php?f=63&t=92900

http://samtuke.com/2014/10/manually-pair-bluetooth-devices-on-linux-via-cli-nfc-workaround/

http://www.correderajorge.es/bluetooth-on-raspberry-audio-streaming/

http://www.ioncannon.net/linux/1570/bluetooth-4-0-le-on-raspberry-pi-with-bluez-5-x/

https://gist.github.com/dustywilson/8267078

http://www.correlatedcontent.com/blog/bluetooth-keyboard-on-the-raspberry-pi/
