from avouris_exercises.program_against_interface_not_implementation.interfaces.InputInterface import InputInterface


class PredeterminedInputProvider(InputInterface):

    def __init__(self, sequence_of_inputs, data):
        self.sequence_of_inputs = sequence_of_inputs
        self.it = self.sequence_of_inputs.__iter__()
        self.history = data

    def get_input(self, descriptor):
        self.history.append(descriptor)
        to_return = self.it.__next__()
        self.history.append(to_return)
        return to_return