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
        def __init__(self, cmd_byte: int ,send_format: list,recieve_format: list):
            self.cmd_byte = cmd_byte
            self.send_format = send_format
            self.recieve_format = recieve_format

    class _AllCommands:
    
        READ_PID = _Command(
            cmd_byte = 0x30,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
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
        
        WRITE_PID_RAM = _Command(
            cmd_byte = 0x31,
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
            cmd_byte = 0x32,
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
            cmd_byte = 0x42,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x43,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x60,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x61,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x62,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x63,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x64,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x90,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x92,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x94,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x9A,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x9C,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
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
        
        READ_MOTOR_STATUS_3 = _Command(
            cmd_byte = 0x9D,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x80,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0x81,
            send_format = [                
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
            cmd_byte = 0xA1,
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
            cmd_byte = 0xA2,
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
        
        ABSOLUTE_POSITION_CLOSED_LOOP_CONTROL = _Command(
            cmd_byte = 0xA4,
            send_format = [
                'cmd_byte',
                'null',
                'speed limit low byte',
                'speed limit high byte',
                'position control low byte',
                'position control',
                'position control',
                'position control high byte',
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
        
        SINGLE_TURN_POSITION_CONTROL = _Command(
            cmd_byte = 0xA6,
            send_format = [
                'cmd_byte',
                'rotation direction byte',
                'speed limit low byte',
                'speed limit high byte',
                'position control low byte',
                'position control high byte',
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
                'encoder value low byte',
                'encoder value high byte',
                ]
            )
        
        INCREMENTAL_POSITION_CLOSED_LOOP_CONTROL = _Command(
            cmd_byte = 0xA8,
            send_format = [
                'cmd_byte',
                'null',
                'speed limit low byte',
                'speed limit high byte',
                'position control low byte',
                'position control'
                'position control'
                'position control high byte',
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
        
        SYSTEM_OPERATING_MODE_ACQUISITION = _Command(
            cmd_byte = 0x70,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'motor operating mode',
                ]
            )
        
        MOTOR_POWER_ACQUISITION = _Command(
            cmd_byte = 0x71,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'motor running power low byte',
                'motor running power high byte',
                ]
            )
        
        SYSTEM_RESET = _Command(
            cmd_byte = 0x76,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
        
        SYSTEM_BRAKE_RELEASE = _Command(
            cmd_byte = 0x77,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
        
        SYSTEM_BREAKE_LOCK = _Command(
            cmd_byte = 0x78,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
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
        
        SYSTEM_RUNTIME_READ = _Command(
            cmd_byte = 0xB1,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'system runtime low byte 1',
                'system runtime byte 2',
                'system runtime byte 3',
                'system runtime byte 4',
                ]
            )
        
        SYSTEM_SOFTWARE_VERSION_DATE = _Command(
            cmd_byte = 0xB2,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'version date low byte 1',
                'version date byte 2',
                'version date byte 3',
                'version date byte 4',
                ]
            )
        
        COMMUNICATION_INTERRUPT_PROTECTION_TIME_SETTING = _Command(
            cmd_byte = 0xB3,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'can recieve time ms low byte 1',
                'can recieve time ms byte 2',
                'can recieve time ms byte 3',
                'can recieve time ms byte 4',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'can recieve time ms low byte 1',
                'can recieve time ms byte 2',
                'can recieve time ms byte 3',
                'can recieve time ms byte 4',
                ],
            )
        
        COMMUNICATION_BAUD_RATE_SETTING = _Command(
            cmd_byte = 0xB4,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'baudrate',
                ],
            recieve_format = [ # Since the communication baud rate is modified, the reply command is random and need not be processed.
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'baudrate',
                ],
            )
        
        MOTOR_MODEL_READING = _Command(
            cmd_byte = 0xB5,
            send_format = [
                'cmd_byte',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                'null',
                ],
            recieve_format = [ 
                'cmd_byte',
                'motor model 1',
                'motor model 2',
                'motor model 3',
                'motor model 4',
                'motor model 5',
                'motor model 6',
                'motor model 7',
                ],
            )
        
        FUNCTION_CONTROL = _Command(
            cmd_byte = 0x20,
            send_format = [
                'cmd_byte',
                'function index',
                'SEE MANUAL',
                'SEE MANUAL',
                'input parameter low byte 1',
                'input parameter low byte 2',
                'input parameter low byte 3',
                'input parameter low byte 4',
                ],
            recieve_format = [
                'cmd_byte',
                'function index',
                'SEE MANUAL',
                'SEE MANUAL',
                'input parameter low byte 1',
                'input parameter low byte 2',
                'input parameter low byte 3',
                'input parameter low byte 4',
                ],
            )
        
        MULTI_MOTOR = _Command(
            cmd_byte = 0x280,
            send_format = [
                'cmd_byte',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                ],
            recieve_format = [
                'cmd_byte',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                ],
            )
        
        CAN_ID_SETTING = _Command(
            cmd_byte = 0x79,
            send_format = [
                'cmd_byte',
                'null',
                'read and write flags',
                'null',
                'null',
                'null',
                'null',
                'can id',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'read and write flags',
                'null',
                'null',
                'null',
                'can id low byte 1',
                'can id byte 2',
                ],
            )
        
        MOTION_MODE_CONTROL_CAN = _Command(
            cmd_byte = 0x400,
            send_format = [
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                ],
            recieve_format = [
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                ],
            )
        
        RS485_MULTI_MOTOR = _Command(
            cmd_byte = 0xCD,
            send_format = [
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                ],
            recieve_format = [
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                'SEE MANUAL',
                ],
            )
        
        RS485_ID_SETTING = _Command(
            cmd_byte = 0x79,
            send_format = [
                'cmd_byte',
                'null',
                'read and write flags',
                'null',
                'null',
                'null',
                'null',
                'RS485ID',
                ],
            recieve_format = [
                'cmd_byte',
                'null',
                'read and write flags',
                'null',
                'null',
                'null',
                'RS485ID low byte 1',
                'RS485ID byte 2',
                ],
            )
    
    return _AllCommands()


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


def get_motor_operation_modes():

    modes = {
        0x01 : 'current loop mode',
        0x02 : 'speed loop mode',
        0x03 : 'position loop mode',
    }

    return modes 


def get_motor_baudrates():

    baudrates = {
        0x00 : '500Kbps',
        0x01 : '1Mbps',
    }

    return baudrates 