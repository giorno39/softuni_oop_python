from elapsed_time import elapsed_time


def cache(func):
    memo = {}

    def wrapper(num):
        if num not in memo:
            result = func(num)
            memo[num] = result
            return result

        return memo[num]

    wrapper.log = memo
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(30)
print(fibonacci.log)
