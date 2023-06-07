class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        result = ", ".join(self.data)
        result = f"[{result}]"
        return result


s = Stack()
s.push("apple")
s.push(3)
s.push("carrot")
print(s.pop())
s.push("vasko")
print(s)