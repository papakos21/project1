import unittest

from GuessingGame import GuessingGame
from test_impl.NumberProvider import NumberProvider
from test_impl.OutputRecorder import OutputRecorder
from test_impl.PredeterminedInputProvider import \
    PredeterminedInputProvider


class GuessingGameTest(unittest.TestCase):

    def test_a_random_game(self):
        my_little_console = []
        r = OutputRecorder(my_little_console)
        p = PredeterminedInputProvider(["Y", "50", "bla", "60", "N"], my_little_console)
        n = NumberProvider([60])
        GuessingGame().game(number_generator=n, input_interface=p, output_interface=r)

        assert my_little_console[-3] == "Το βρήκατε μετά από 1 προσπάθειες, και κερδίσατε 9 πόντους"
