import car_function_library
import pytest

# test_values = [
#     {'speed': 2, 'time': 6, 'weight': 1000},
#     {'speed': 10, 'time': 65, 'weight': 150},
#     {'speed': 200, 'time': 156, 'weight': 2540},
# ]
#
#
# @pytest.mark.parametrize('input_values', test_values)


def test_input_values():
    speed = 10
    time = 7
    weight = 1254

    our_result = car_function_library.car_parameters(
        time=time,
        speed=speed,
        weight=weight
    )
    expected_result = f"Car weight of 1254kg was moving 7 seconds with speed 10m/s and traveled 70 meters"
    expected_type = str
    # print(f"speed={speed}, time={time}, weight={weight}")
    assert our_result == expected_result
    assert type(our_result) is expected_type
