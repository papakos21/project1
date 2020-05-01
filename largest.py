def find_largest(lista):
    if len(lista) > 0:

        max_so_far = lista[0]
        for i in range(1, len(lista)):
            if lista[i] > max_so_far:
                max_so_far = lista[i]
        return max_so_far
    else:
        return None
