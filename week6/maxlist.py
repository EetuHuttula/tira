class MaxList:
    def __init__(self):
        self.count = 0
        self.max_number = None

    def append(self, number):
        if self.count == 0:
            self.max_number = number
        else: 
            self.max_number = max(self.max_number, number)

        self.count += 1
    def max(self):
        return self.max_number

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8

    numbers = MaxList()
    total = 0
    for i in range(10**5):
        numbers.append(i * 999983 % 10**9)
        total += numbers.max()
    print(total) # 99 49 83 81 79 75 17