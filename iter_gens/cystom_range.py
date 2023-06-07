class custom_range:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.finish:
            raise StopIteration
        value_to_return = self.start
        self.start += 1
        return value_to_return

