my_dict = {'Masha': 1992, 'Mirra': 2017, 'Max': 1986}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Sasha'))
my_dict.update({'Taya': 1972, 'Asya': 2015})
a = my_dict.pop('Mirra')
print(a)
print(my_dict)
my_set = {1, 3, 'Tost', (2, 4.7, 5), 7, 1, 8, 3}
print(my_set)
my_set.update({"Bread", (7, 8, 9)})
my_set.discard(3)
print(my_set)