def find_number(numbers):
    count = {}
    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1
    return sorted(count, key=lambda minval: count[minval])[0]
if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100

numbers = [1] * 10**5 + [2]
print(find_number(numbers))  #2 