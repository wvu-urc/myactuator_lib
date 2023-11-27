# This library is used to generate CAN messages that can be sent to MyActuator motors

# read_pid_parameters 
send - cmd byte
reply:
hex values -> decimal 
max val of current loop -> 3 
3/256 * decimal = K parameter 

# set_pid_parameters (use rom)
same process as above
reply exact same 

# read_acceleration
send - cmd byte
reply
4 bytes converted directly to decimal 

# set_acceleration 
indexes for function 
0x00 -> position accel
0x01 -> position decel
0x02 -> speed accel
0x03 -> speed decel 
4 bytes converted directly to decimal 

# read_encoder_values_offset MULTITURN
value is after subtracting zero offset
4 bytes converted directly to decimal 
units of pulses 

# read_encoder_values MULTITURN
value is without subtracting zero offset
4 bytes converted directly to decimal 
units of pulses 

# read_zero_offset MULTITURN
4 bytes directly to decimal 
units of pulses 

# set_encoder_value_offset MULTITURN
send 4 bytes - directly to dec 

# reset_encoder_value_offset MULTITURN
send cmd byte 
recieve new offset 

# read_encoder_values 
send cmd_byte
recieve position, original position, zero point (3 sets of 2 bytes)

# read_angle
send cmd_byte 
