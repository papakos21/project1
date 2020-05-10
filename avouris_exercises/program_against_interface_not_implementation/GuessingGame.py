from avouris_exercises.program_against_interface_not_implementation.human_implementations import RegularOutputProvider, \
    RegularInputProvider, RandomNumberProvider
from avouris_exercises.program_against_interface_not_implementation.interfaces import InputInterface, OutputInterface, \
    RandomNumberInterface


class GuessingGame():

    def game(self,
             number_generator: RandomNumberInterface = RandomNumberProvider.RandomNumberProvider(),
             input_interface: InputInterface = RegularInputProvider.RegularInputProvider(),
             output_interface: OutputInterface = RegularOutputProvider.RegularOutputProvider()
             ):

        def input_is_valid(inputstr_):
            return inputstr_.isdigit() and int(inputstr_) in range(0, 101)

        first_message = "θέλεις να παίξεις; (Y/N)"
        repeat_message = "θέλεις να ξαναπαίξεις; (Y/N)"

        max_attempts = 10
        repeat = False
        game = True
        while game:

            welcome_message_note = first_message if not repeat else repeat_message
            welcome_message = input_interface.get_input(welcome_message_note)

            if welcome_message is None: return #this is for testing mode

            if welcome_message.upper() == "N":
                game = False

            if welcome_message.upper() == "Y":
                points, prospatheies, random_number = 10, 0, number_generator.get_num()

                if random_number is None:return #this is for testing mode

                while True:
                    if prospatheies < max_attempts:
                        inp_msg = "Δώσε αριθμό από 1 έως 100 : "
                        input_number = input_interface.get_input(inp_msg)


                        if input_number is None:return #this is for testing mode


                        if not input_is_valid(input_number):
                            continue

                        input_number = int(input_number)
                        if input_number == random_number:
                            points = points - prospatheies
                            output_interface.print_output(
                                "Το βρήκατε μετά από {} προσπάθειες, και κερδίσατε {} πόντους".format(prospatheies,
                                                                                                      points))

                            repeat = True
                            break

                        else:
                            output_interface.print_output("Ο κρυμμένος αριθμός είναι " + (
                                "μικροτερος " if input_number > random_number else "μεγαλυτερος"))
                            prospatheies += 1

                    elif prospatheies == max_attempts:
                        output_interface.print_output("Χάσατε με 0 πόντους!")