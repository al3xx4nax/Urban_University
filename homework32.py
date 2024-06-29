class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        elif self.start < self.end and self.start % 2 != 0:
            self.start += 1
            self.start += 2
            return self.start - 2
        else:
            self.start += 2
            return self.start - 2


en = EvenNumbers(10, 25)
for i in en:
    print(i)
