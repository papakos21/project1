import time
import random


def sorted_list_generator(size_of_list, randomizer):
    to_return = []
    x = 0
    for i in range(size_of_list):
        x = x + randomizer.randint(0, 10)
        to_return.append(x)
    return to_return


def find_index_in_list(number_to_find, sorted_list):
    for i in range(len(sorted_list)):
        if sorted_list[i] == number_to_find:
            return i

    return -1


def find_index_in_list_binary_search(number_to_find, sorted_list):
    left = 0
    right = len(sorted_list)

    while left <= right:

        middle_index =  left + (right-left)//2
        middle_number = sorted_list[middle_index]

        if middle_number == number_to_find:
            return middle_index
        elif middle_number < number_to_find:
            left = middle_index+1
        else:
            right = middle_index-1
    return -1


def find_algo_timer(algorithm,number_to_search, output_list ):
    start = time.time()
    res = algorithm(number_to_search, output_list)
    end = time.time()
    total_time= end-start

    return {"time":total_time,"result":res}


def run_for_size(input_size, randomizer) :

    output_list = sorted_list_generator(input_size,randomizer)
    number_to_search = randomizer.randint(0,input_size*5)
    print("Searching for " + str(number_to_search) + " in " + str(input_size) + " random sorted list")
    results = []
    for algo in [find_index_in_list,find_index_in_list_binary_search]:
        print(find_index_in_list.__name__)
        algo_result = find_algo_timer(algo, number_to_search, output_list)
        print(algo_result)
        results.append(algo_result)

    print("Slow is " + str(results[0]["time"]/results[1]["time"]) + " times slower!!")


def run_all():
    randomizer = random.Random()
    randomizer.seed(42)
    for x in range(1,7):
        run_for_size(int(pow(10,x)),randomizer)
        print("\n\n")


run_all()