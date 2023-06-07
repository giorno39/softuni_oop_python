def squares(num):
    for side in range(1, num + 1):
        yield side * side


print(list(squares(5)))