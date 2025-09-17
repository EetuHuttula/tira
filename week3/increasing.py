def count_sublists(numbers):
    length = len(numbers)
    current_count = 1
    total_count = 0
    for pos in range(length):
        if pos != 0 and numbers[pos - 1] < numbers[pos]:
            current_count += 1
        else:
            current_count = 1
        total_count += current_count
    return total_count 
if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers)) # 5000050000