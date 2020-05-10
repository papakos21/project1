from avouris_exercises.program_against_interface_not_implementation.interfaces.OutputInterface import OutputInterface


class RegularOutputProvider(OutputInterface):

    def __init__(self):
        pass

    def print_output(self, ouput_message):
        print(ouput_message)
