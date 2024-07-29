# myactuator_lib

Message [Nate Adkins](mailto:npa00003@mix.wvu.edu) on Slack with any questions or suggestions

## Overview

This Python library facilitates the control of an X6 or X10 myactuator motor using the CAN protocol. The library defines a `Motor` class, which represents the actuator and provides methods for various commands. The library also includes a `CanData` class for handling CAN data and a `CanDataParameter` class for defining parameters within CAN messages.

## Classes

### `Motor` Class

The `Motor` class is the main class in the library representing the actuator. It includes methods for various commands such as reading PID parameters, writing PID parameters to RAM and ROM, reading acceleration, and controlling the motor in closed-loop modes. The class ensures that the provided arbitration ID is within a valid range.

### `CanData` Class 

The `CanData` classs handle the creation of the data field of a can message by recieving CanDataParameter(s) and proplery formatting them. The class is used internally by the `_Motor` class for constructing messages with specific commands and parameters. Please do not access.

### `CanDataParameter` Class

The `CanDataParameter` classs handle the creation of a single data field found within a can message for this particular motor. Instances of this class are given to the CanData class to parse into part of the contents of a can message. The class is used internally by the `_Motor` class for constructing messages with specific commands and parameters. Please do not access. 

## Installation

### 1. Clone this repository
- ```bash
  git clone git@github.com:your-username/myactuator_lib.git
  ```
### 2. Navigate to the repository directory 
- ```bash
  cd myactuator_lib
  ```
### 3. Install the pip package
- ```bash 
  pip install . 
  ```
## Example usage

```python
import myactuator_lib 
motor = myactuator_lib.Motor(0x141)
can_message = motor.Speed_Closed_loop_Control_Command(600)
# (now send can message over interface of your choice)
```

## Known Limitations
As of now, all commands should work but many remain untested. The only one 100% confirmed to be functional is the `Speed_Closed_loop_Control_Command()`

The can_test script is mostly functional but has not been modified to be user friendly. It is very much a work in progress but should have enough in place to allow for basic testing of a motor over CAN