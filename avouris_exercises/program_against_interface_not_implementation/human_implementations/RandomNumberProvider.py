import random
from avouris_exercises.program_against_interface_not_implementation.interfaces.RandomNumberInterface import RandomNumberInterface


class RandomNumberProvider(RandomNumberInterface):

    def __init__(self):
        pass

    def get_num(self):
        return random.randint(0, 99)
