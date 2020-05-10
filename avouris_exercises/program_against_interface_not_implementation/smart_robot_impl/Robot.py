from avouris_exercises.program_against_interface_not_implementation.interfaces.InputInterface import InputInterface
from avouris_exercises.program_against_interface_not_implementation.interfaces.OutputInterface import OutputInterface


class Robot(InputInterface,OutputInterface):

    def __init__(self):
        self.started = False
        self.finished = False
        self.left = 1
        self.right = 99
        self.current = 50

    def get_input(self, desriptor):

        print(desriptor)
        if not self.started:
            self.started = True
            return "Y"
        elif self.finished:
            return "N"

        print(self.current)
        return str(self.current)

    def print_output(self, ouput_message):

        print(ouput_message)

        if "μεγαλυτερος" in ouput_message:
            self.left = self.current
            self.current = self.current + (self.right - self.current) // 2

        if "μικροτερος" in ouput_message:
            self.right = self.current
            self.current = self.left + (self.current - self.left) // 2

        if "βρήκατε" in ouput_message:
            self.finished = True
            print("Ο αριθμος ήταν " + str(self.current))