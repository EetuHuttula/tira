def count_substrings(string):
    length = len(string)
    count = set(string)
    for start in range(length):
        for end in range(start + 1, length + 1):
            count.add(string[start:end])
    return len(count)

if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110