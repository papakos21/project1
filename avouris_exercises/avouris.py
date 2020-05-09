def initials(text):
    text = text.upper() #kanoume to keimeno kefalaia
    text = text.split() #vazoume kathe leksi se lista
    return_value = []   #keni lista
    for i in range(len(text)):
        init = text[i]
        return_value.append(init[0] + '.') #vazoume se nea lista to prwto gramma kathe leksis kai mia teleia

    x = " ".join(return_value) #enwnoume ta koutakia tis listas kai ta xwrizoume me keno
    return x


initials("hello lena kant")
