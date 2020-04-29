# πρόγραμμα που με βάση τα χρήματα και το επιτόκιο σου λέει σε πόσα χρόνια θα εισαι millionaire


years = 0
money = input("Πόσα λεφτά έχεις; :")
money = int(money)
epitokio = input("Mε πόσο ετήσιο επιτόκιο %; :")
epitokio = float(epitokio)

while money < 1000000:
    Akrives_epitokio = (epitokio / 100) * money
    Akrives_epitokio = float(Akrives_epitokio)
    money = money + Akrives_epitokio
    years = years + 1
else:
    print("σε {} χρόνια θα είσαι millionaire!!".format(years))
