
def find_rounds(numbers):
    list = []
    rounds = 1
    nb = numbers.copy()
    
    for i in range(len(nb)):
        sub_list = []
        for j in range(len(nb)):
            if nb[j] == rounds:
                #print(numb[j], rounds)
                sub_list.append(rounds)
                #print(sub_list)
                rounds += 1
        if sub_list:
            list.append(sub_list)
        nb = [x for x in nb if x not in sub_list]
    return list

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
