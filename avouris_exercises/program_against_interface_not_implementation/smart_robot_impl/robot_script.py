from avouris_exercises.program_against_interface_not_implementation.smart_robot_impl.Robot import Robot
from avouris_exercises.program_against_interface_not_implementation.GuessingGame import GuessingGame


robot =Robot()
GuessingGame().game(input_interface=robot, output_interface=robot)