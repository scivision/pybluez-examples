#!/usr/bin/env python3
"""
demo of basic Bluetooth device scanning/discovery
Michael Hirsch
GPLv3+
http://blog.kevindoran.co/bluetooth-programming-with-python-3/
"""
try:
    import bluetooth as bt
except ImportError as e:
    print('*** you must have PyBluez installed.  pip install pybluez ')
    exit(str(e))

scansec = 10 #how long to scan for (seconds)

devsfound = bt.discover_devices(duration=scansec, flush_cache=True, lookup_names=False )

print('found ' +str(len(devsfound)) + ' devices in Bluetooth range: ' + str(devsfound))