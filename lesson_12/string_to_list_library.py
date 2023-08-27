def convert_string_to_list(string_value: str) -> list:
    final_list = []
    letter_counter = 0
    while letter_counter < len(string_value) and len(final_list) < 100:
        if string_value[letter_counter].isalpha() and string_value[letter_counter] not in wrong_letters_list:
            final_list.append(string_value[letter_counter])
        letter_counter += 1
    return final_list


wrong_letters_list = ['M', 'm', 'N', 'n']

if __name__ == '__main__':
    func_result = convert_string_to_list('FDgdhd436-nb- 536498ni56934b-6v4,s   fdf sdg sdgfg sdfggrE')
    print(func_result)
