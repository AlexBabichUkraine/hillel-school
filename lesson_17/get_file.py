airport_list = []

with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    col_name_list = file.readline().split(';')
    iso_country_index = col_name_list.index('iso_country')
    airport_name_index = col_name_list.index('name')
    for line in file.readlines():
        data = line.split(';')
        if data[iso_country_index] == 'UA':
            airport_list.append(f"{data[airport_name_index]}\n")

airport_list.sort()

with open('ukraine_airports_list.txt', mode='w', encoding='utf-8') as file_for_write:
    file_for_write.writelines(airport_list)

print(*airport_list)
