import string_to_list_library

VALUE = {
    'input_value': 'a2bc-90-9Nm457',
    'expected_value': 'abc'
}


def test_string_transformation():
    expected_result = VALUE['expected_value']
    our_result = ''.join(string_to_list_library.convert_string_to_list(VALUE['input_value']))
    assert expected_result == our_result


def test_length_transformation():
    our_result = string_to_list_library.convert_string_to_list(VALUE['input_value'])
    assert len(our_result) < 100
