import unittest

from avouris_exercises.program_against_interface_not_implementation.GuessingGame import GuessingGame
from avouris_exercises.program_against_interface_not_implementation.test_impl.NumberProvider import NumberProvider
from avouris_exercises.program_against_interface_not_implementation.test_impl.OutputRecorder import OutputRecorder
from avouris_exercises.program_against_interface_not_implementation.test_impl.PredeterminedInputProvider import \
    PredeterminedInputProvider


class GuessingGameTest(unittest.TestCase):


    def test_a_random_game(self):
             my_little_console = []
             r = OutputRecorder(my_little_console)
             p = PredeterminedInputProvider(["Y", "50", "bla", "60", "N"], my_little_console)
             n = NumberProvider([60])
             GuessingGame().game(number_generator=n, input_interface=p, output_interface=r)

             assert my_little_console[-3] == "Το βρήκατε μετά από 1 προσπάθειες, και κερδίσατε 9 πόντους"
