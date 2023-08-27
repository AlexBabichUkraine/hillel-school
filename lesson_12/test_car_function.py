from random import randint
import car_function_library
import pytest

test_values = [
    ([randint(0, 100), randint(0, 100), randint(0, 2000)], str),
    ([randint(0, 100), randint(0, 100), randint(0, 2000)], str),
    ([randint(0, 100), randint(0, 100), randint(0, 2000)], str),
    ([randint(0, 100), randint(0, 100), randint(0, 2000)], str),
    ([randint(0, 100), randint(0, 100), randint(0, 2000)], str),
]


@pytest.mark.parametrize('input_values, expected', test_values)
def test_input_values(input_values, expected):
    our_result = car_function_library.car_parameters(
        time=input_values[0],
        speed=input_values[1],
        weight=input_values[2]
    )
    expected_result = f"Car weight of {input_values[2]}kg was moving {input_values[0]} seconds" \
                      f" with speed {input_values[1]}m/s and traveled {input_values[0] * input_values[1]} meters"
    expected_type = expected
    print(f"speed={input_values[0]}, time={input_values[1]}, weight={input_values[2]}")
    assert our_result == expected_result
    assert type(our_result) is expected_type
