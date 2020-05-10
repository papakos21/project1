import random

paixnidi = True
while True:
    welcome_message = input(
        "αν θέλεις να παίξεις πληκτρολόγησε YES ,αν θες να βγεις από το παιχνίδι πληκτρολογησε STOP :")

    if welcome_message == "STOP":

        paixnidi = False
        break
    if welcome_message == "YES":
        prospatheies = 0
        points = 10
        random_number = random.randint(0, 99)

        while True:
            if prospatheies < 10:
                input_number = input("Δώσε αριθμό από 1 έως 100 : ")
                if not input_number.isdigit():
                    continue
                else:
                    input_number = int(input_number)
                if input_number < 1 or input_number > 100:
                    continue
                if input_number == random_number:
                    points = points - prospatheies
                    print("Το βρήκατε μετά από {} προσπάθειες, και κερδίσατε {} πόντους".format(prospatheies, points))
                    synexeia = input("Θέλετε να ξαναπαίξετε; YES/NO ")
                    if synexeia == "YES":
                        points = 10
                        prospatheies = 0
                        random_number = random.randint(0, 99)
                        input_number = input("Δώσε αριθμο απο 1 εως 100:")
                        if not input_number.isdigit():
                            continue
                        else:
                            input_number = int(input_number)

                        if input_number < 1 or input_number > 100:
                            continue

                    elif synexeia == "NO":
                        break
                if input_number > random_number:
                    print("Ο κρυμμένος αριθμός είναι μικρότερος")
                    prospatheies += 1


                if input_number < random_number:
                    print("Ο κρυμμένος αριθμός είναι μεγαλύτερος")
                    prospatheies += 1


            elif prospatheies == 10:
                print("Χάσατε με 0 πόντους!")
                break
