import random
import time
numbers = [random.randint(0, 100) for _ in range(10**7)] 

def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

start = time.time()
count_even(numbers)
finish = time.time()
print(f"Time 1: {finish - start}")


start = time.time()
count_even2(numbers)
finish = time.time()
print(f"Time 2: {finish - start}")