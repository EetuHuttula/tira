def check_number(number):
    check = [3, 7, 1, 3, 7, 1, 3, 7]
    total = 0
    for i in range(len(check)):
        multply = check[i] * int(number[i])
        total += multply        
        if len(number) < 8 or len(number) > 9 or number[0] != "0":
            return False
    next_10th = (total + 9) // 10 * 10
    return ((next_10th - total) % 10) == ((int(number) % 10))

         
if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
    print(check_number("059103335")) # False
    print(check_number("032238170")) # True
    print(check_number("100000007")) # True