def askisi_2():

    lala  = True
    while  lala:
        x = int(input("δώσε x:"))
        y = int(input("δώσε y:"))
        athr = x + y
        gino = x * y
        print("To άθροισμα είναι {}".format(athr))
        print("Τό γινόμενο είναι {}".format(gino))

        apantisi = input("να συνεχίσω;")
        if apantisi == "stop":
            break
        else :
            continue

        #return (athr, gino)
askisi_2()

#programma pou zitaei duo arithmous k dinei to athroisma kai to ginomeno , se rwtaei na sunexisei k stamataei
#an dwseis apantisi stop alliws sunexizei. epeidi to ekana function k afto exw kolllisei me to return gia na mporesw
#na ftiaksw to test
