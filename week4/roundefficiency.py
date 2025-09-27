import time
import random
def count_rounds(numbers):
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds


def count_rounds_dict(numbers):
    n = len(numbers)
 
    pos = {}
    for i, elem in enumerate(numbers):
        pos[elem] = i
 
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1
    return rounds


randlist = list(range(1, 10**7))
random.seed(1337) 
random.shuffle(randlist)

start = time.time()
_ = count_rounds(randlist)
finish = time.time()
print(f"Count rounds with list: { finish - start:.4f}")
  

start = time.time()
_ = count_rounds_dict(randlist)
finish = time.time()
print(f"Count rounds with dictionary: { finish - start:.4f}")