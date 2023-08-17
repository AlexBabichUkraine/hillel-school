original_string = "київ,оДеса     Львів.житоМИР,уЖгОрОд.....ХарКІВ       , слАвУтИч"
cities_list = original_string.replace('.', ' ').replace(',', ' ').title().split()

# Alternative solution
#
# final_string = ''
#
# for element in original_string:
#     if element.isalpha():
#         final_string += element
#     else:
#         final_string += ' '
#
# final_list = final_string.title().split()
#
# for city_name in final_list:
#     print(f"I \U00002764 {city_name}")

for city in cities_list:
    print(f"I \U00002764 {city}")

pass

