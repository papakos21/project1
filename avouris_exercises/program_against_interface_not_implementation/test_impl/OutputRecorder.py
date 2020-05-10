from avouris_exercises.program_against_interface_not_implementation.interfaces.OutputInterface import OutputInterface


class OutputRecorder(OutputInterface):

    def __init__(self, data):
        self.data = data

    def print_output(self, ouput_message):
        self.data.append(ouput_message)