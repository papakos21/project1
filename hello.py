
inp  = []
def my_print( *args):
    for a in args:
        inp.append(a)


def greet(name):
    my_print("Hello", name )


