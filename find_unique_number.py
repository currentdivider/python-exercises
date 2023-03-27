# Write a method that findss, efficiently with respect to time used, all numbers that occurs exactly once in the input list.

import time

def find_unique_numbers(numbers):
    unique_numbers = []
    for number in numbers:
        count = numbers.count(number)
        if count == 1:
            unique_numbers.append(number)
        else: 
            continue

    return unique_numbers

if __name__ == "__main__":
    start_time = time.time()
    print(find_unique_numbers([1, 2, 1, 3]))
    print("--- %.10f seconds ---" % (time.time() - start_time))