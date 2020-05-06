def initials(text):
    text=text.upper()
    print (text[0],'.',end=' ')

    for x in range (len(text)):
        if text[x] == ' ':
            letter=text[x+1]
            print (letter,'.', end =' ')




initials("hello lena kant")