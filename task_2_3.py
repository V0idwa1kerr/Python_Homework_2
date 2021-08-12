names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

name_str = ' '.join(names)
name_array = name_str.title()
j = name_array.split(' ')

name_1 = ('Привет, ' + j[1])
name_2 = ('Привет, ' + j[4])
name_3 = ('Привет, ' + j[8])
name_4 = ('Привет, ' + j[10])

print("{}\n{}\n{}\n{}".format(name_1, name_2, name_3, name_4))
