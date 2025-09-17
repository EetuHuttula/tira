def find_order(n):
    players = list(range(1, n +1))
    exits = []
    for i, elem in enumerate(players):
        if i % 2 == 0:
            players.append(elem)
        else:
            exits.append(elem)
    return exits
if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]
""" 
    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929] """

numbers = [1] * 10**5 + [2]
print(numbers)