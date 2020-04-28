def black_or_white(input_number):
    if input_number == 0:
        return "white"
    if input_number == 1:
        return "black"


# 0-->white, 1-->black, 2-->blue, 3-->green
def my_colors(input_number):
    # use if else control flow
    if input_number == 0:
        return "white"
    elif input_number == 1:
        return "black"
    elif input_number == 2:
        return "blue"
    elif input_number == 3:
        return "green"
    else :
        return "unknown"


def my_colors_map(input):
    pass

    # create a dictionary color_dic keys are a numbers and values are color names 'red', 'green' , etc
    # return color_dict[input]
