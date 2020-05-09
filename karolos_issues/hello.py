
inp  = []
def my_print( *args):
    print(*args)
    for a in args:
        inp.append(a)


def greet(name):
    my_print("Hello", name )

greet("elena")


