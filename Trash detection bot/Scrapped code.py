import libusb1
import nxt
from mindstorms import MSHub
import nxt.locator
import usb.core
import usb.backend.libusb1
import usb.util


 if end != 'q':
            key = sys.stdin.read(1)
            False
                #if key == 'q':
                #both.brake()
                #both.idle()

for dev in libusb1.find(find_all=True):
    print(dev)

libusb1_backend = usb.backend.libusb1.get_backend(find_library=libusb1.find_library)
print(list(usb.core.find(find_all=True, backend=libusb1_backend)))

for dev in usb.core.find(find_all=True):
    print(dev)

with nxt.locator.find() as b:
    print(b.get_device_info()[0:2])




os.environ['PYUSB_DEBUG'] = 'debug'
import usb.core
usb.core.find()



logging.basicConfig(level=logging.DEBUG)
back = libusb1.get_backend()
print(type(back))

dev = usb.core.find(backend=back)
print(type(dev))

print("Hello World")

with nxt.locator.find() as b


import logging 
import usb.core
from usb.backend import libusb1
import nxt.locator
#import nxt.bluesock
import os
#import bluetooth

## Address name of the NXT Brick on bluetooth: 00:16:53:12:9F:34

address= "00:16:53:12:9F:34"

sock= bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((address, 1))


print("Found brick:", b.get_device_info()[0])
b.play_tone(440,250)