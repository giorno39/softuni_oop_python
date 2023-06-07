lines = int(input())

def get_line(i, n, char="*"):
    line = ""
    line += " " * (n - 1 - i)
    line += f"{char} " * (i + 1)
    line += "\n"
    return line


def generate_rhombus(n):
    result = ""
    for i in range(n):
        result += get_line(i, n)
        result.strip()
    for i in range(n - 2, -1, -1):
        result += get_line(i, n)
        result.strip()

    return result



print(generate_rhombus(lines))