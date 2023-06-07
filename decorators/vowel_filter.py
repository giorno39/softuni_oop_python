from functools import wraps


def vowel_filter(func):
    @wraps(func)
    def wrapper():
        vowels = "aeiouy"
        result = [x for x in func() if x in vowels]
        return result

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
