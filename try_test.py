def division(x: int, y: int):
    try:
        result = x / y
    except ValueError:
        result = 'Division by zero'
    return result


print(division(56, 0))
