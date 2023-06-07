from functools import wraps


def is_even(num):
    return num % 2 == 0


def even_numbers(func):
    @wraps(func)
    def wrapper(nums):
        result = [x for x in nums if is_even(x)]
        return result

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
