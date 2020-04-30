import time
import random


def sorted_list_generator(size_of_list):
    r = random.Random()
    random.seed(10)
    to_return = []
    x = 0
    for i in range(size_of_list):
        x = x + r.randint(0, 10)
        to_return.append(x)
    return to_return


# print(sorted_list_generator(20))


# input number_to_find , sorted_list
# output index_of_number_or_-1

def find_index_in_list(number_to_find, sorted_list):
    for i in range(len(sorted_list)):
        if sorted_list[i] == number_to_find:
            return i

    return -1


def find_index_in_list_binary_search(number_to_find, sorted_list):
    left = 0
    right = len(sorted_list)
    while left < right:
        middle_index = (right - left) // 2
        middle_number = sorted_list[middle_index]
        if middle_number == number_to_find:
            return middle_index
        elif middle_number < number_to_find:
            right = middle_index
        else:
            left = middle_index
    return -1


# sorted_list_generator(2000000)
output_list = sorted_list_generator(2000000)
number_to_search = 7000000
start = time.time()
res = find_index_in_list(number_to_search, output_list)
print(res)
end = time.time()
total_time_slow = end-start
print(total_time_slow)

start = time.time()
res = find_index_in_list_binary_search(number_to_search, output_list)
print(res)
end = time.time()
total_time = end-start
print(total_time)
print(total_time_slow/total_time)


