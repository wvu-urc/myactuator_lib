import numpy as np

class CanDataParameter:
    def __init__(self, decimal_value, allowable_range, start_position, num_bytes):
        self.decimal_value = self._validate_decimal_value(decimal_value, allowable_range)
        self.num_bytes = num_bytes
        self.position = start_position
        self.byte_array = self._calculate_byte_array()

    def _validate_decimal_value(self, decimal_value, allowable_range):
        if decimal_value < allowable_range[0] or decimal_value > allowable_range[1]:
            raise ValueError(f"Decimal value {decimal_value} must be in the range {allowable_range}")
        return decimal_value

    def _calculate_byte_array(self):
        # Convert decimal value to bytes using numpy
        byte_array = np.array(self.decimal_value, dtype=np.int32).tobytes()

        # Ensure the list has the correct length (num_bytes)
        int_list = [int(byte) for byte in byte_array[:self.num_bytes]]

        return int_list

class CanData:
    def __init__(self, initial_byte, parameter_list: list[CanDataParameter]):
        self.initial_byte = initial_byte
        self.parameter_list = parameter_list
        self.byte_array = self._construct_byte_array()

    def _construct_byte_array(self):
        used_positions = set()
        total_bytes = sum(param.num_bytes for param in self.parameter_list) + 1  # Add 1 for the initial byte
        byte_array = [self.initial_byte] + [0] * 7 # Pad with zeros to make it 8 bytes

        for param in self.parameter_list:
            start_position = param.position # +1 to skip the initial byte
            end_position = start_position + param.num_bytes

            # Check if any positions are already occupied
            if any(pos in used_positions for pos in range(start_position, end_position)):
                raise ValueError(f"Invalid combination: Parameter at position {param.position} with length {param.num_bytes} conflicts with existing bytes.")
            
            # Update the set of used positions
            used_positions.update(range(start_position, end_position))

            # Place the bytes in the byte array
            byte_array[start_position:end_position] = param.byte_array

        return byte_array[:8]
