def get_word(input_word):
    input_word = str(input_word)
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    if len(input_word) <= 9:
        input_word = input_word.ljust(9, " ")

        for i in range(len(input_word)):
            if i <= 2:
                list1.append(input_word[i])
            elif 2 < i <= 5:
                list2.append(input_word[i])
            elif 5 < i <= 8:
                list3.append(input_word[i])
        list4 = [list1, list2, list3]
        return list4

    elif len(input_word) > 9:
        return "too long!!!!"


get_word('abcdefghi')
