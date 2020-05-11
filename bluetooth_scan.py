#!/usr/bin/env python
"""
Bluetooth device scanning/discovery

http://blog.kevindoran.co/bluetooth-programming-with-python-3/
https://github.com/pybluez/pybluez
"""
import bluetooth as bt

try:
    from bluetooth.ble import DiscoveryService
except ImportError:
    DiscoveryService = None


def bluetooth_classic_scan(timeout=10):
    """
    This scan finds ONLY Bluetooth classic (non-BLE) devices in *pairing mode*
    """
    return bt.discover_devices(duration=scansec, flush_cache=True, lookup_names=True)


def bluetooth_low_energy_scan(timeout=10):
    """
    currently Linux only
    """
    if DiscoveryService is None:
        return None

    svc = DiscoveryService()
    return svc.discover(timeout)


if __name__ == "__main__":
    scansec = 5  # how long to scan for (seconds)

    dev_classic = bluetooth_classic_scan(scansec)
    if dev_classic:
        for d in dev_classic:
            print(d)

    dev_ble = bluetooth_low_energy_scan(scansec)
    if dev_ble:
        for u, n in dev_ble.items():
            print(u, n)
