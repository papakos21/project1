from avouris_exercises.program_against_interface_not_implementation.interfaces.RandomNumberInterface import \
    RandomNumberInterface


class NumberProvider(RandomNumberInterface):

    def __init__(self, numbers):
        self.numbers = numbers
        self.it = numbers.__iter__()

    def get_num(self):
        return next(self.it,None)
