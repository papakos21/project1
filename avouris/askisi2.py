# my_sum in order not to confuse with built in python function sum
def my_sum(x,y):
    return x+y


def my_product(x,y):
    return x*y


# a function should ideally do only one thing so breaking it to two
def sum_and_product(x,y,):
    return my_sum(x, y), my_product(x, y)


# the view function ( a bit difficult but not impossible to write tests - do not write tests for now)
def sum_and_product_interactive():
    while True:
        x = int(input("δώσε x:"))
        y = int(input("δώσε y:"))

        # business logic moved to other function
        (athr, gino) = sum_and_product(x,y)

        print("To άθροισμα είναι {}".format(athr))
        print("Τό γινόμενο είναι {}".format(gino))

        apantisi = input("να συνεχίσω;")

        if apantisi == "stop":
            break
        else:
            continue
sum_and_product_interactive()

#programma pou zitaei duo arithmous k dinei to athroisma kai to ginomeno , se rwtaei na sunexisei k stamataei
#an dwseis apantisi stop alliws sunexizei. epeidi to ekana function k afto exw kolllisei me to return gia na mporesw
#na ftiaksw to test
