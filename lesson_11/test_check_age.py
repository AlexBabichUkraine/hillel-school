from our_library import check_age_and_response


VALUES = {
    'wrong_value': 101,
    'young_value': 13,
    'middle_value': 25,
    'old_value': 67,
}


def test_wrong_age():
    expected_result = 'Please enter number in range 1-100'
    current_result = check_age_and_response(VALUES['wrong_value'])
    assert expected_result == current_result
    # assert type(current_result) == str


def test_young_age():
    expected_value = 'You are a kid'
    current_result = check_age_and_response(VALUES['young_value'])
    assert expected_value == current_result


def test_middle_age():
    expected_value = 'You are not old and not young'
    current_result = check_age_and_response(VALUES['middle_value'])
    assert expected_value == current_result


def test_old_age():
    expected_value = 'You are too old'
    current_result = check_age_and_response(VALUES['old_value'])
    assert expected_value == current_result
