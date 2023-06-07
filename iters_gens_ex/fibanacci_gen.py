def fibonacci():
    first, second = 0, 1
    yield first
    yield second
    while True:
        result = first + second
        first, second = second, result
        yield result


generator = fibonacci()
for i in range(5):
    print(next(generator))
