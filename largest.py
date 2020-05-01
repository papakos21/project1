def find_largest(lista1):
    if len(lista1) > 0:

        max_so_far = lista1[0]
        for i in range(1, len(lista1)):
            if lista1[i] > max_so_far:
                max_so_far = lista1[i]
        return max_so_far
    else:
        return None
