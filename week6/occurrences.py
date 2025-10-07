class OccurrenceTracker:
    def __init__(self):
        self.dict = {}

    def append(self, number):
        if number in self.dict:
            self.dict[number] += 1
        else:
            self.dict[number] = 1
    def count(self):
        return len(set(self.dict.values()))

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3

    tracker = OccurrenceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(i % 100 + 1)
        total += tracker.count()
    print(total) # 198901