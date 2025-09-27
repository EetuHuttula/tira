def create_distribution(string):
    s = len(string)
    count = {}
    for start in range(s):
        for end in range(start + 1, s + 1):
            scount = string[start:end]
            l = len(scount)
            if l not in count:
                count[l] = set()
            count[l].add(scount) 
            
    return {l: len(count[l]) for l in count}



if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}
    
    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}
    
    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}