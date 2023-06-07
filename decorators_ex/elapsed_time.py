from time import time


def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        with open(".\\result.txt", "w") as file:
            file.write(str(end - start))
        return end - start

    return wrapper


@elapsed_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())

