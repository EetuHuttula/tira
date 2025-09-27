def hash_value(string):
    A = 23
    M = 2**32
    result = 0
    for char in string:
        result = (result * A + (ord(char) - ord("a"))) % M
    return result

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440 