import time

def list_efficiency_append(list, n):
    for i in range (n):
        list.append(i)
    return list
list = []
def list_efficiency_pop(list, n):
    for i in range(n):
        list.pop(0)
    return list


start = time.time()
list_efficiency_append(list, 100000)
finish = time.time()
print(f"Append time: {finish - start:.4f}")

start = time.time()
list_efficiency_pop(list, 100000)
finish = time.time()
print(f"Pop time: {finish - start:.4f}")


print(list)