array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Понял, что сей код выглядит колхозно :(
# Поэтому пришлось взять грех на душу и посмотреть разбор ДЗ, и переписать с пониманием того, что переписываю

# number_1 = ''.join('"{}"'.format(array[1].zfill(2)))
# array[1] = number_1

# number_2 = ''.join('"{}"'.format(array[3].zfill(2)))
# array[3] = number_2

# number_3 = ''.join('"{}"'.format(array[-2].zfill(3)))
# array[-2] = number_3

# array = " ".join(array)
# print(array)

new_array = []
for elements in array:
    if elements.isdigit():
        new_array.extend(['"', f'{int(elements):02}', '"'])
    elif (elements.startswith('+') or elements.startswith('-')) and elements[1:].isdigit():
        new_array.extend(['"', f'{elements[0]}{int(elements):02}', '"'])
    else:
        new_array.append(elements)

final_result = ' '.join(new_array)
print(final_result)
