# myactuator_command_formats.py
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


def get_commands():

    class _Command():
        def __init__(self, hex_cmd: int ,send_format: list,recieve_format: list):
            self.hex_cmd = hex_cmd
            self.send_format = send_format
            self.recieve_format = recieve_format

    class _AllCommands:
    
        READ_PID = _Command(
            hex_cmd = 0x30,
            send_format = [0x30,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'current loop p',
                'current loop i',
                'speed loop p',                
                'speed loop i',
                'position loop p',
                'position loop i',
                ]
            )
        
        WRITE_PID_RAM = _Command(
            hex_cmd = 0x31,
            send_format = [
                'cmd_byte',
                'null',
                'current loop p',
                'current loop i',
                'speed loop p',                
                'speed loop i',
                'position loop p',
                'position loop i',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'current loop p',
                'current loop i',
                'speed loop p',                
                'speed loop i',
                'position loop p',
                'position loop i',
                ]
            )
        
        WRITE_PID_ROM = _Command(
            hex_cmd = 0x32,
            send_format = [
                'cmd_byte',
                'null',
                'current loop p',
                'current loop i',
                'speed loop p',                
                'speed loop i',
                'position loop p',
                'position loop i',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'current loop p',
                'current loop i',
                'speed loop p',                
                'speed loop i',
                'position loop p',
                'position loop i',
                ]
            )
        
        READ_ACCEL = _Command(
            hex_cmd = 0x42,
            send_format = [0x42,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',    
                'null',
                'null',
                'null',
                'acceleration low byte 1',
                'acceleration byte 2',              
                'acceleration byte 3',
                'acceleration byte 4',
                ]
            )
        
        WRITE_ACCEL_RAM_ROM = _Command(
            hex_cmd = 0x43,
            send_format = [0x43,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',    
                'null',
                'null',
                'null',
                'acceleration low byte 1',
                'acceleration byte 2',              
                'acceleration byte 3',
                'acceleration byte 4',
                ]
            )
        
        READ_MULTI_TURN_ENCODER_POS = _Command(
            hex_cmd = 0x60,
            send_format = [0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'encoder position low byte 1',
                'encoder position byte 2',
                'encoder position byte 3',
                'encoder position byte 4',
                ]
            )
        
        READ_MULTI_TURN_ENCODER_ORIGINAL_POS = _Command(
            hex_cmd = 0x61,
            send_format = [0x61,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'encoder original position byte 1',
                'encoder original position byte 2',
                'encoder original position byte 3',
                'encoder original position byte 4',
                ]
            )
        
        MULTI_TURN_ENCODER_ZERO_OFFSET = _Command(
            hex_cmd = 0x62,
            send_format = [0x62,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'encoder offset byte 1',
                'encoder offset byte 2',
                'encoder offset byte 3',
                'encoder offset byte 4',
                ]
            )
        
        WRITE_MULTI_TURN_ENCODER_VAL_AS_ZERO = _Command(
            hex_cmd = 0x63,
            send_format = [0x63,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'encoder zero bias low byte 1',
                'encoder offset byte 2',
                'encoder offset byte 3',
                'encoder offset byte 4',
                ]
            )
        
        WRITE_MULTI_TURN_ENCODER_POS_AS_ZERO = _Command(
            hex_cmd = 0x64,
            send_format = [0x64,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'encoder zero bias low byte 1',
                'encoder offset byte 2',
                'encoder offset byte 3',
                'encoder offset byte 4',
                ]
            )
        
        SINGLE_TURN_ENCODER_COMMAND = _Command(
            hex_cmd = 0x90,
            send_format = [0x90,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'encoder position low byte',
                'encoder position high byte',
                'encoder original position low byte',
                'encoder original position high byte',
                'encoder zero bias low byte',
                'encoder zero bias high byte',
                ]
            )
        
        READ_MULTI_TURN_ANGLE = _Command(
            hex_cmd = 0x92,
            send_format = [0x92,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'angle low byte 1',
                'angle bytes 2',
                'angle bytes 3',
                'angle bytes 4',
                ]
            )
        
        READ_SINGLE_TURN_ANGLE = _Command(
            hex_cmd = 0x94,
            send_format = [0x94,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'single turn angle low byte',
                'single turn angle high byte',
                ]
            )
        
        READ_MOTOR_STATUS_1_AND_ERROR_FLAG = _Command(
            hex_cmd = 0x9A,
            send_format = [0x9A,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'motor temperature',
                'null',
                'brake release command',
                'voltage low byte',
                'voltage high byte',
                'error status low byte 1',
                'error status byte 2',
                ]
            )
        READ_MOTOR_STATUS_2 = _Command(
            hex_cmd = 0x9C,
            send_format = [0x9C,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'motor temperature',
                'torque current low byte',
                'torque current high byte',
                'motor speed low byte',
                'motor speed high byte',            
                'motor angle low byte',
                'motor angle high byte',
                ]
            )
        
        READ_MOTOR_STATUS_3 = _Command(
            hex_cmd = 0x9D,
            send_format = [0x9D,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'motor temperature',
                'phase A current low byte',
                'phase A current high byte',
                'phase B current low byte',
                'phase B current high byte',            
                'phase C current low byte',
                'phase C current high byte',
                ]
            )
        
        MOTOR_SHUTDOWN = _Command(
            hex_cmd = 0x80,
            send_format = [0x80,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ]
            )
        
        MOTOR_STOP = _Command(
            hex_cmd = 0x81,
            send_format = [0x81,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ]
            )
        TORQUE_CLOSED_LOOP_CONTROL = _Command(
            hex_cmd = 0xA1,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'torque current control value low byte',
                'torque current control value high byte',
                'null',
                'null',
                ],
            recieve_format = [
                'cmd_byte',
                'motor temperature',
                'torque current low byte',
                'torque current high byte',
                'motor speed low byte',
                'motor speed high byte',
                'motor angle low byte',
                'motor angle high byte',
                ]

            )
        
        SPEED_CLOSED_LOOP_CONTROL = _Command(
            hex_cmd = 0xA2,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'speed control low byte',
                'speed control',
                'speed control',
                'speed control high byte',
                ],
            recieve_format = [
                'cmd_byte',
                'motor temperature',
                'torque current low byte',
                'torque current high byte',
                'motor speed low byte',
                'motor speed high byte',
                'motor angle low byte',
                'motor angle high byte',
                ]

            )
        
        
    return _AllCommands()
        

def get_cmd_hex():

    class _CommandBytes():

        READ_PID = 0x30
        WRITE_PID_RAM = 0x31
        WRITE_PID_ROM = 0x32
        READ_ACCEL = 0x42
        WRITE_ACCEL_RAM_ROM = 0x43
        READ_MULTI_TURN_ENCODER_POS = 0x60
        READ_MULTI_TURN_ENCODER_ORIGINAL_POS = 0x61
        READ_MULTI_TURN_ENCODER_ZERO_OFFSET = 0x62
        WRITE_MULTI_TURN_ENCODER_VAL_AS_ZERO = 0x63
        WRITE_MULTI_TURN_ENCODER_POS_AS_ZERO = 0x64
        READ_SINGLE_TURN_ENCODER = 0x90
        READ_MULTI_TURN_ANGLE = 0x92
        READ_SINGLE_TURN_ANGLE = 0x94
        READ_MOTOR_STATUS_1_AND_ERROR_FLAG = 0x9A
        READ_MOTOR_STATUS_2 = 0x9C
        READ_MOTOR_STATUS_3 = 0x9D
        MOTOR_SHUTDOWN = 0x80
        MOTOR_STOP = 0x81
        TORQUE_CLOSED_LOOP_CONTROL = 0xA1
        SPEED_CLOSED_LOOP_CONTROL = 0xA2
        ABSOLUTE_POSITION_CLOSED_LOOP_CONTROL = 0xA4
        SINGLE_TURN_POSITION_CONTROL = 0xA6
        INCREMENTAL_POSITION_CLOSED_LOOP_CONTROL = 0xA8
        SYSTEM_OPERATING_MODE_ACQUISITION = 0x70
        MOTOR_POWER_ACQUISITION = 0x71
        SYSTEM_RESET = 0x76
        SYSTEM_BRAKE_RELEASE = 0x77
        SYSTEM_BREAKE_LOCK = 0x78
        SYSTEM_RUNTIME_READ = 0xB1
        SYSTEM_SOFTWARE_VERSION_DATE = 0xB2
        COMMUNICATION_INTERRUPT_PROTECTION_TIME_SETTING = 0xB3
        COMMUNICATION_BAUD_RATE_SETTING = 0xB4
        MOTOR_MODEL_READING = 0xB5
        FUNCTION_CONTROL = 0x20
        MULTI_MOTOR = 0x280 # (+ command)
        CAN_ID_SETTING = 0x79
        MOTION_MODE_CONTROL_CAN = 0x400 # (+ id)
        RS485_MULTI_MOTOR = 0xCD # (+ command)
        RS485_ID_SETTING = 0x79

    return _CommandBytes()

def get_send_formats():

    class _SendFormats:
        READ_PID = 'n/a'

    return _SendFormats
    

def get_reply_formats():
    class _ReplyFormats:

        READ_PID = [
            'cmd_byte',
            'null',
            'current loop p',
            'current loop i',
            'speed loop p',                
            'speed loop i',
            'position loop p',
            'position loop i',
            ]
    
        WRITE_PID_RAM = READ_PID
        WRITE_PID_ROM = READ_PID


        WRITE_PID_RAM = 0x31
        WRITE_PID_ROM = 0x32
        READ_ACCEL = 0x42
        WRITE_ACCEL_RAM_ROM = 0x43
        READ_MULTI_TURN_ENCODER_POS = 0x60
        READ_MULTI_TURN_ENCODER_ORIGINAL_POS = 0x61
        READ_MULTI_TURN_ENCODER_ZERO_OFFSET = 0x62
        WRITE_MULTI_TURN_ENCODER_VAL_AS_ZERO = 0x63
        WRITE_MULTI_TURN_ENCODER_POS_AS_ZERO = 0x64
        READ_SINGLE_TURN_ENCODER = 0x90
        READ_MULTI_TURN_ANGLE = 0x92
        READ_SINGLE_TURN_ANGLE = 0x94
        READ_MOTOR_STATUS_1_AND_ERROR_FLAG = 0x9A
        READ_MOTOR_STATUS_2 = 0x9C
        READ_MOTOR_STATUS_3 = 0x9D
        MOTOR_SHUTDOWN = 0x80
        MOTOR_STOP = 0x81
        TORQUE_CLOSED_LOOP_CONTROL = 0xA1
        SPEED_CLOSED_LOOP_CONTROL = 0xA2
        ABSOLUTE_POSITION_CLOSED_LOOP_CONTROL = 0xA4
        SINGLE_TURN_POSITION_CONTROL = 0xA6
        INCREMENTAL_POSITION_CLOSED_LOOP_CONTROL = 0xA8
        SYSTEM_OPERATING_MODE_ACQUISITION = 0x70
        MOTOR_POWER_ACQUISITION = 0x71
        SYSTEM_RESET = 0x76
        SYSTEM_BRAKE_RELEASE = 0x77
        SYSTEM_BREAKE_LOCK = 0x78
        SYSTEM_RUNTIME_READ = 0xB1
        SYSTEM_SOFTWARE_VERSION_DATE = 0xB2
        COMMUNICATION_INTERRUPT_PROTECTION_TIME_SETTING = 0xB3
        COMMUNICATION_BAUD_RATE_SETTING = 0xB4
        MOTOR_MODEL_READING = 0xB5
        FUNCTION_CONTROL = 0x20
        MULTI_MOTOR = 0x280 # (+ command)
        CAN_ID_SETTING = 0x79
        MOTION_MODE_CONTROL_CAN = 0x400 # (+ id)
        RS485_MULTI_MOTOR = 0xCD # (+ command)
        RS485_ID_SETTING = 0x79

        PID = 
        
        ACCEL = [
            'cmd_byte',    
            'null',
            'null',
            'null',
            'acceleration low byte 1',
            'acceleration byte 2',              
            'acceleration byte 3',
            'acceleration byte 4',
            ]
        
        MULTI_TURN_ENCODER_POSITION = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'encoder position low byte 1',
            'encoder position byte 2',
            'encoder position byte 3',
            'encoder position byte 4',
            ]
        
        MULTI_TURN_ENCODER_ORIGINAL_POSITION = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'encoder original position byte 1',
            'encoder original position byte 2',
            'encoder original position byte 3',
            'encoder original position byte 4',
            ]
        
        MULTI_TURN_ENCODER_ZERO_OFFSET = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'encoder offset byte 1',
            'encoder offset byte 2',
            'encoder offset byte 3',
            'encoder offset byte 4',
            ]
        
        MULTI_TURN_ENCODER_VAL_AS_ZERO = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'encoder offset byte 1',
            'encoder offset byte 2',
            'encoder offset byte 3',
            'encoder offset byte 4',
            ]
        
        MULTI_TURN_ENCODER_POS_AS_ZERO = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'encoder zero bias low byte 1',
            'encoder offset byte 2',
            'encoder offset byte 3',
            'encoder offset byte 4',
            ]
        
        SINGLE_TURN_ENCODER_COMMAND = [
            'cmd_byte',
            'null',
            'encoder position low byte',
            'encoder position high byte',
            'encoder original position low byte',
            'encoder original position high byte',
            'encoder zero bias low byte',
            'encoder zero bias high byte',
        ]

        MULTI_TURN_ANGLE_COMMAND = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'angle low byte 1',
            'angle bytes 2',
            'angle bytes 3',
            'angle bytes 4',
        ]
        SINGLE_TURN_ANGLE_COMMAND = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'null',
            'null',
            'single turn angle low byte',
            'single turn angle high byte',
        ]

        MOTOR_STATUS_1_AND_ERROR_FLAG = [
            'cmd_byte',
            'motor temperature',
            'null',
            'brake release command',
            'voltage low byte',
            'voltage high byte',
            'error status low byte 1',
            'error status byte 2',
        ]

        MOTOR_STATUS_2 = [
            'cmd_byte',
            'motor temperature',
            'torque current low byte',
            'torque current high byte',
            'motor speed low byte',
            'motor speed high byte',            
            'motor angle low byte',
            'motor angle high byte',
        ]
        MOTOR_STATUS_3 = [
            'cmd_byte',
            'motor temperature',
            'phase A current low byte',
            'phase A current high byte',
            'phase B current low byte',
            'phase B current high byte',            
            'phase C current low byte',
            'phase C current high byte',
        ]

        MOTOR_SHUTDOWN = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'null',
            'null',
            'null',
            'null',
        ]
        MOTOR_STOP = [
            'cmd_byte',
            'null',
            'null',
            'null',
            'null',
            'null',
            'null',
            'null',
        ]

        
    return _ReplyFormats()



def get_write_formats():

    class _WriteFormats():
        PID_RAM = [0x31,0x00,0x00,0x00,0x00,0x00]
        PID_ROM = [0x32,0x00,0x00,0x00,0x00,0x00]
        ACCEL_RAM_ROM = [0x43,0x00,0x00,0x00,0x00,0x00]
        MULTI_TURN_ENCODER_VAL_AS_ZERO = [0x63,0x00,0x00,0x00,0x00,0x00]
        MULTI_TURN_ENCODER_POS_AS_ZERO = [0x64,0x00,0x00,0x00,0x00,0x00]
        MOTOR_SHUTDOWN = [0x80,0x00,0x00,0x00,0x00,0x00]       
        MOTOR_STOP = [0x81,0x00,0x00,0x00,0x00,0x00]  

    return _WriteFormats()


def get_system_error_states():

    states = {
        0x0002 : 'motor stall',
        0x0004 : 'low pressure',
        0x0008 : 'overvoltage',
        0x0010 : 'overcurrent',
        0x0040 : 'power overrun',
        0x0100 : 'speeding',
        0x0200 : 'null',
        0x0400 : 'null',
        0x0800 : 'null',
        0x1000 : 'motor temperature over temperature',
        0x2000 : 'encoder calibration error',
    }

    return states 
