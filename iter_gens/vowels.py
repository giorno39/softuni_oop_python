class NextIter:
    def __init__(self, vow):
        self.string = vow.string
        self.start = vow.start

    def __next__(self):
        searched_chars = "eyuioa"
        while True:
            if self.start == len(self.string):
                raise StopIteration
            curr_char = self.string[self.start]
            self.start += 1
            if curr_char.lower() in searched_chars:
                return curr_char

class vowels:
    def __init__(self, string):
        self.string = string
        self.start = 0

    def __iter__(self):
        return NextIter(self)




my_string = vowels('Abcedifuty0o')
my_string2 = vowels("oiuhvcasd")

