def convert_to_string(foo):
    def wrapper(*args, **kwargs):
        result = str(foo(*args, **kwargs))
        return result
    return wrapper


@convert_to_string
def product_func(arg1: int, arg2: int) -> int:
    result = arg1 ** arg2
    return result


def product_funk_alt(arg1: int, arg2: int) -> int:
    result = arg1 ** arg2
    return result


print(type(product_func(54, 75)))
print(type(product_funk_alt(54, 75)))
