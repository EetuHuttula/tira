class PermutationTracker:
    def __init__(self):
        self.num = {}
        self.isrepeat = False
        self.max_value = 0
        self.n = 0

    def append(self, number):
        self.n += 1

        if number in self.num:
            self.isrepeat = True
        else:
            self.num[number] = True

        if number > self.max_value:
            self.max_value = number

    def check(self):
        
        if self.isrepeat:
            return False
        if len(self.num) != self.n:
            return False
        
        return self.max_value == self.n


if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False

    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i%2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total) # 50000