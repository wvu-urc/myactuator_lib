import can
from myactuator_lib.can_data import CanDataParameter, CanData

class _Motor():

	def __init__(self, arbitration_id: int):
		minimum_id = 0x141
		maximum_id = 0x172

		if (minimum_id < arbitration_id < maximum_id): 
			self.arbitration_id = arbitration_id
		else:
			raise ValueError(f"The arbitration id {arbitration_id} is invalid")

	def _create_can_message(self, created_can_data: CanData) -> can.Message:

		can_data = created_can_data.byte_array

		if not (len(can_data) == 7): # need to populate 7 bytes only, check
			raise ValueError

		for byte in can_data:
			if not (0x00 <= byte <= 0xFF): # int not guaranteed to be within range of hex byte, check
				raise ValueError

		return can.Message(
			arbitration_id = self.arbitration_id,
			is_extended_id = False,
			data = can_data)