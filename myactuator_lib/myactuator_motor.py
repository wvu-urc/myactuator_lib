
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

import numpy as np
import can
from myactuator_lib.myactuator_command_formats import get_commands


class MyActuatorMotor():


    def __init__(self, arbitration_id ):
        self.arbitration_id = arbitration_id
        self.is_extended_id = False
        self.commands = get_commands()


    def make_rpm_command(self, rpm):

        rpm_integer = np.int32(rpm / .01)

        can_data = [0xA2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        can_data[4:7] = self.int32_to_uint8(rpm_integer)

        return can.Message(
            arbitration_id = self.arbitration_id,
            is_extended_id = self.is_extended_id,
            data = can_data
            )


    def read_pid(self):
        return [self.commands.READ_PID] + [0] * 7
    

    def write_pid_ram(self, current_loop_p, current_loop_i, speed_loop_p, speed_loop_i, position_loop_p, position_loop_i):
        return [
            self.commands.WRITE_PID_RAM,
            0,
            current_loop_p,
            current_loop_i,
            speed_loop_p,
            speed_loop_i,
            position_loop_p,
            position_loop_i
        ]
    

    def write_pid_rom(self, current_loop_p, current_loop_i, speed_loop_p, speed_loop_i, position_loop_p, position_loop_i):
        return [
            self.commands.WRITE_PID_ROM,
            0,
            current_loop_p,
            current_loop_i,
            speed_loop_p,
            speed_loop_i,
            position_loop_p,
            position_loop_i
        ]


    def read_accel(self):
        return [self.commands.READ_ACCEL] + [0] * 7
    

    def write_accel_ram_rom(self):
        return [self.commands.WRITE_ACCEL_RAM_ROM] + [0] * 7
    

    def read_multi_turn_encoder_pos(self):
        return [self.commands.READ_MULTI_TURN_ENCODER_POS] + [0] * 7
    

    def read_multi_turn_encoder_original_pos(self):
        return [self.commands.READ_MULTI_TURN_ENCODER_ORIGINAL_POS] + [0] * 7
    

    def multi_turn_encoder_zero_offset(self):
        return [self.commands.MULTI_TURN_ENCODER_ZERO_OFFSET] + [0] * 7
    

    def write_multi_turn_encoder_val_as_zero(self):
        return [self.commands.WRITE_MULTI_TURN_ENCODER_VAL_AS_ZERO] + [0] * 7
    

    def write_multi_turn_encoder_pos_as_zero(self):
        return [self.commands.WRITE_MULTI_TURN_ENCODER_POS_AS_ZERO] + [0] * 7
    

    def single_turn_encoder_command(self):
        return [self.commands.SINGLE_TURN_ENCODER_COMMAND] + [0] * 7
    

    def read_multi_turn_angle(self):
        return [self.commands.READ_MULTI_TURN_ANGLE] + [0] * 7
    

    def read_single_turn_angle(self):
        return [self.commands.READ_SINGLE_TURN_ANGLE] + [0] * 7
    

    def read_motor_status_1_and_error_flag(self):
        return [self.commands.READ_MOTOR_STATUS_1_AND_ERROR_FLAG] + [0] * 7
    

    def read_motor_status_2(self):
        return [self.commands.READ_MOTOR_STATUS_2] + [0] * 7
    

    def read_motor_status_3(self):
        return [self.commands.READ_MOTOR_STATUS_3] + [0] * 7
    

    def motor_shutdown(self):
        return [self.commands.MOTOR_SHUTDOWN] + [0] * 7
    

    def motor_stop(self):
        return [self.commands.MOTOR_STOP] + [0] * 7
    


    def int32_to_uint8(self,byte_32):
        byte_3 = (byte_32 >> 24)
        byte_2 = (byte_32 >> 16) & 0xFF
        byte_1 =  (byte_32 >> 8) & 0xFF
        byte_0 = byte_32 & 0xFF
        bytes = np.array([byte_0, byte_1, byte_2, byte_3], dtype=np.uint8)
        return bytes