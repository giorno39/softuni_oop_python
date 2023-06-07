def reverse_text(text):
    length = len(text)
    return (text[length - n - 1] for n in range(len(text)))

for char in reverse_text("step"):
    print(char, end='')
