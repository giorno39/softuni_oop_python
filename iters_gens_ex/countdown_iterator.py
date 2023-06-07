class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.end:
            raise StopIteration

        value_to_return = self.count
        self.count -= 1
        return value_to_return


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
