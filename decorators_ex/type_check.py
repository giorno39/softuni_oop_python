from functools import wraps


def type_check(primitive):
    def decorator(func):
        @wraps(func)
        def wrapper(element):
            if not isinstance(element, primitive):
                return "Bad Type"
            return func(element)

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
