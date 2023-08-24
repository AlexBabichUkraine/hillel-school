def check_age_and_response(age: int) -> str:
    if age <= 0 or age >= 101:
        return 'Please enter number in range 1-100'
    if 1 <= age <= 18:
        return 'You are a kid'
    if 19 <= age <= 65:
        return 'You are not old and not young'
    if 101 > age > 65:
        return 'You are too old'
