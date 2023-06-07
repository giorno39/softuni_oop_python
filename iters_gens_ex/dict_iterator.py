class dictionary_iter:
    def __init__(self, dct):
        self.dct = list(dct.items())
        self.start = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.dct):
            raise StopIteration

        idx = self.start
        self.start += 1
        return self.dct[idx]



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
