from avouris_exercises.program_against_interface_not_implementation.interfaces.InputInterface import InputInterface


class RegularInputProvider(InputInterface):

    def __init__(self):
        pass

    def get_input(self, desriptor):
        inp = input(desriptor)
        return inp