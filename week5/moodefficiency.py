import time 
import random

def find_mode(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x
    return mode

def mode_by_sort(numbers):
    n = len(numbers)
    number = sorted(numbers)
    mode = numbers[0]
    count = 1
    curr = 1

    for i in range(1, n):
        if number[i-1] == number[i]:
            curr += 1
        else:
            curr = 1

        if curr > count:
            count = curr
            mode = number
    return mode 


rn = 10**7
randlist = [random.randint(1,1000) for i in range(rn)]

start = time.time()
find_mode(randlist)
finish = time.time()
print(f"Find mode with dict: {finish - start:.4f}")

start = time.time()
mode_by_sort(randlist)
finish = time.time()
print(f"Find mode with sorting: {finish - start:.4f}")