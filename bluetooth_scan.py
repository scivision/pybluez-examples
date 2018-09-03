#!/usr/bin/env python
"""
Bluetooth device scanning/discovery

http://blog.kevindoran.co/bluetooth-programming-with-python-3/
https://github.com/pybluez/pybluez
"""
import bluetooth as bt
from bluetooth.ble import DiscoveryService


def bluetooth_classic_scan(timeout=10):
    """
    This scan finds ONLY Bluetooth (non-BLE) devices in pairing mode
    """
    devs = bt.discover_devices(duration=scansec, flush_cache=True, lookup_names=True)

    print('found', len(devs), 'Bluetooth (non-BLE) devices in pairing mode:')

    if devs:
        for u, n in devs.items():
            print(u, n)

    return devs


def bluetooth_low_energy_scan(timeout=10):
    svc = DiscoveryService()
    devs = svc.discover(timeout)

    print('found', len(devs), 'Bluetooth Low Energy (Smart) devices:')

    if devs:
        for u, n in devs.items():
            print(u, n)

    return devs


if __name__ == '__main__':
    scansec = 5  # how long to scan for (seconds)

    bluetooth_classic_scan(scansec)

    bluetooth_low_energy_scan(scansec)
