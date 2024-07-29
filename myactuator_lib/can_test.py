import sys
from motor import Motor as MyActuator
import can
from time import sleep

def pretty(command : can.Message):
    print(f"[{hex(command.arbitration_id)}]  {hex(command.data[0])} {hex(command.data[1])} {hex(command.data[2])} {hex(command.data[3])} {hex(command.data[4])} {hex(command.data[5])} {hex(command.data[6])} {hex(command.data[7])}")

motor_id = int(sys.argv[1])
motor_speed = sys.argv[2]

bus = can.Bus(
    interface = "socketcan", 
    channel = "can0", 
    is_extended_id = "False",
    bitrate = "1000000"
)

# if not isinstance(motor_id, int):
#     print(f"{motor_id} is not an ingeter")

# if not isinstance(motor_speed, int):
#     print(f"{motor_id} is not an ingeter")

can_command : can.Message

can_command = MyActuator.Speed_Closed_loop_Control_Command(MyActuator(motor_id), int(motor_speed))

for i in range(0,100):
    try:
        pretty(can_command)
        bus.send(can_command)
        can_command.arbitration_id += 1
        recieved_message = bus.recv(0.10)

        if recieved_message:
            pretty(recieved_message)
        elif recieved_message == None:
            print(f"Motor: {can_command.arbitration_id} is not connected -> Hardware")
        else:
            print(f'did not recieve data (recieved message was of type {type(recieved_message)})')

        bus.flush_tx_buffer()
        sleep(0.1)

    except Exception as error:    
        print(f'can_subscriber_node:\nError:{error}\nTraceback:{error.with_traceback}')

    # sleep(1)
