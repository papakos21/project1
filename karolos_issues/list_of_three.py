def split(word):
    return list(word)

def get_word(input_word):
    listara=[]
    input_word = str(input_word)
    if len(input_word) <= 9:
        n = 3
        input_word = input_word.ljust(9, " ")
        listoula = [input_word[i:i + n] for i in range(0, len(input_word), n)]
        for i in range (len(listoula)):
            listara.append(split(listoula[i]))
        return listara
    elif len(input_word) >=9 :
        return "too long!!!!"


get_word("abcdefghi")

