# myactuator_motor.py
# By: Nathan Adkins 
# email: npa00003@mix.wvu.edu
# WVU URC 

'''
https://www.robotshop.com/products/myactuator-rmd-x10-s2-v3-bldc-can-bus-reduction-ratio-135-w-new-driver-mc-x-500o

1.1.CAN Bus
    1.1.1. Parameters
        Bus interface: CAN
        Baud rate: 1Mbps
    1.1.2. Message format
        Identifier: Single motor command sending: 0x140 + ID(1~32)
            Multi-motor command sending: 0x280
            Reply: 0x240 + ID (1~32)
        Frame format: data frame
        Frame Type: Standard Frame
        DLC: 8 bytes
1.2.RS485 bus
    1.2.1. Parameters
        Bus interface: RS485
        Baudrate:115200bp,500Kbps,1Mbps,1.5Mbps,2Mbps

'''




class MyActuatorMotor():

    def __init__():
        pass


    def generate_sent_can_message():
        pass











def main():
    pass


if __name__ == '__main__':
    main()


    import can
    import time
    import os
    print('Bring up CAN0....')
    os.system("sudo /sbin/ip link set can0 up type can bitrate 1000000")
    time.sleep(0.1)
    bus = can.Bus(interface='socketcan', channel='can0', is_extended_id=False, bitrate=1000000)
    go_msg = can.Message(
    # Send command for 90 deg/s
    arbitration_id=0x141, data=[0xA2, 00, 00, 00, 0x28, 0x23, 0, 0], is_extended_id=False
    )
    stop_msg = can.Message(
    # Send command for 0 deg/s
    arbitration_id=0x141, data=[0xA2, 00, 00, 00, 0x00, 0x00, 0, 0], is_extended_id=False
    )
    try:
        bus.send(go_msg)
        time.sleep(2)
        bus.send(stop_msg)
        print(f"Message sent on {bus.channel_info}")
        print(bus.recv())
    except can.CanError:    
        print("Message NOT sent")
    finally:
        bus.shutdown()

    
