# This file was autogenerated by "generate.py" found under the "generate_commands" folder of "myactuator_lib"
import can
from myactuator_lib.can_data import CanDataParameter, CanData

class Motor():

	def __init__(self, arbitration_id: int):
		minimum_id = 0x141
		maximum_id = 0x172

		if (minimum_id <= arbitration_id <= maximum_id): 
			self.arbitration_id = arbitration_id
		else:
			raise ValueError(f"The arbitration id {arbitration_id} is invalid must be within ({minimum_id},{maximum_id}) (inclusive)")

	def _create_can_message(self, created_can_data: CanData) -> can.Message:

		can_data = created_can_data.byte_array

		if not (len(can_data) == 8): # need to populate 8 bytes only, check
			raise ValueError(f"CAN length {len(can_data)} is not 8. Data is {can_data}")

		for byte in can_data:
			if not (0x00 <= byte <= 0xFF): # int not guaranteed to be within range of hex byte, check
				raise ValueError(f"{byte} is not within bounds of a hex byte")

		return can.Message(
			arbitration_id = self.arbitration_id,
			is_extended_id = False,
			data = can_data)

	def Read_PID_parameter_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x30 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Write_PID_parameters_to_RAM_command(self, current_P_gain, current_I_gain, speed_P_gain, speed_I_gain, pos_P_gain, pos_I_gain) -> can.Message:
		range_vals = (0,256)
		can_parameters = []
		can_parameters.append(CanDataParameter(current_P_gain,range_vals,2,1))
		can_parameters.append(CanDataParameter(current_I_gain,range_vals,3,1))
		can_parameters.append(CanDataParameter(speed_P_gain,range_vals,4,1))
		can_parameters.append(CanDataParameter(speed_I_gain,range_vals,5,1))
		can_parameters.append(CanDataParameter(pos_P_gain,range_vals,6,1))
		can_parameters.append(CanDataParameter(pos_I_gain,range_vals,7,1))

		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x31 
		can_data_constructor.parameter_list = can_parameters
		self._create_can_message(can_data_constructor)

	def Write_PID_parameters_to_ROM_command(self, current_P_gain, current_I_gain, speed_P_gain, speed_I_gain, pos_P_gain, pos_I_gain) -> can.Message:
		range_vals = (0,256)
		can_parameters = []
		can_parameters.append(CanDataParameter(current_P_gain,range_vals,2,1))
		can_parameters.append(CanDataParameter(current_I_gain,range_vals,3,1))
		can_parameters.append(CanDataParameter(speed_P_gain,range_vals,4,1))
		can_parameters.append(CanDataParameter(speed_I_gain,range_vals,5,1))
		can_parameters.append(CanDataParameter(pos_P_gain,range_vals,6,1))
		can_parameters.append(CanDataParameter(pos_I_gain,range_vals,7,1))

		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x32 
		can_data_constructor.parameter_list = can_parameters
		self._create_can_message(can_data_constructor)

	def Read_acceleration_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x42 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Write_acceleration_to_RAM_and_ROM_command(self, acceleration_degrees_per_sec_per_sec) -> can.Message:
		can_parameters = []
		can_parameters.append(CanDataParameter(acceleration_degrees_per_sec_per_sec,(100,60000),2,1))
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x43 
		can_data_constructor.parameter_list = can_parameters
		self._create_can_message(can_data_constructor)

	def Read_multi_turn_encoder_position_data_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x60 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Read_multi_turn_encoder_zero_offset_data_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x62 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Read_single_turn_encoder_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x90 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Read_multi_turn_angle_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x92 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Read_single_turn_angle_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x94 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Read_Motor_Status_1_and_Error_Flag_Command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x9A 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Read_Motor_Status_2_Command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x9C 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Read_Motor_Status_3_Command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x9D 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Motor_shutdown_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x80 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Motor_stop_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x81 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Torque_closed_loop_control_command(self, torque_current_mA) -> can.Message:
		can_parameters = []
		can_parameters.append(CanDataParameter(torque_current_mA,(0,32767),4,2))
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0xA1 
		can_data_constructor.parameter_list = can_parameters
		self._create_can_message(can_data_constructor)

	def Speed_Closed_loop_Control_Command(self, speed_control_degrees_per_second) -> can.Message:
		speed_control = speed_control_degrees_per_second * 100 # actual speed is 0.01dps/LSB
		can_parameters = []
		can_parameters.append(CanDataParameter(speed_control,(0,32767),4,4))
		can_data_constructor = CanData(0xA2, can_parameters)
		return self._create_can_message(can_data_constructor)

	def Absolute_position_closed_loop_control_command(self, speed_limit, position_control) -> can.Message:
		can_parameters = []
		can_parameters.append(CanDataParameter(speed_limit,(0,32767),2,2))
		can_parameters.append(CanDataParameter(position_control,(0,32767),4,4))
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0xA4 
		can_data_constructor.parameter_list = can_parameters
		self._create_can_message(can_data_constructor)

	def Single_turn_position_control_command(self, rotation_direction, speed_limit, position_control) -> can.Message:
		can_parameters = []
		can_parameters.append(CanDataParameter(rotation_direction,(0,1),1,1))
		can_parameters.append(CanDataParameter(speed_limit,(0,35999),2,2))
		can_parameters.append(CanDataParameter(position_control,(0,35999),4,2))
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0xA6 
		can_data_constructor.parameter_list = can_parameters
		self._create_can_message(can_data_constructor)

	def System_operating_mode_acquisition(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x70 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Motor_power_acquisition(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x71 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def System_reset_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x76 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def System_brake_release_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x77 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def System_brake_lock_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0x78 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def System_runtime_read_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0xB1 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def System_software_version_date_read_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0xB2 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	def Communication_baud_rate_setting_command(self, baudrate) -> can.Message:
		can_parameters = []
		can_parameters.append(CanDataParameter(baudrate,(0,1),7,1))
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0xB4 
		can_data_constructor.parameter_list = can_parameters
		self._create_can_message(can_data_constructor)

	def Motor_model_reading_command(self) -> can.Message:
		can_data_constructor = CanData()
		can_data_constructor.initial_byte = 0xB5 
		can_data_constructor.parameter_list = []
		self._create_can_message(can_data_constructor)

	# def Function_control_command(self, can_parameters: list[CanDataParameter]) -> can.Message:
	# 	can_data_constructor = CanData()
	# 	can_data_constructor.initial_byte = 0x20 
	# 	can_data_constructor.parameter_list = can_parameters
	# 	self._create_can_message(can_data_constructor)



