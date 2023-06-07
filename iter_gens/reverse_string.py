

class reverse_iter:
    def __init__(self, item_to_iter):
        self.item_to_iter = item_to_iter
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.start) > len(self.item_to_iter):
            raise StopIteration
        value_to_return = self.item_to_iter[self.start]
        self.start -= 1
        return value_to_return


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
