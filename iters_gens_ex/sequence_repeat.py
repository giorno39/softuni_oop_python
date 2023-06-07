class sequence_repeat:
    def __init__(self, string, count):
        self.string = string
        self.count = count
        self.start = 0
        self.length = len(string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.count:
            raise StopIteration

        value_to_return = self.string[self.start % self.length]
        self.start += 1
        return value_to_return


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
