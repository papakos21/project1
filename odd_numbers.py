table = []


def all_odd(num):
    num = int(num)
    while num > 1:
        if num % 2 == 0:

            for x in range(1, num, 2):
                table.append(x)
                return table
        else:
            num = num + 1
            for x in range(1, num, 2):
                table.append(x)
            return table



