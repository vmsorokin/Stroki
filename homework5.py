name='Владимир'
a=123
immutable_var=tuple([name, [6,11,1988], 'Дата моего рождения', True])
print('Immutable_var:', immutable_var)
#immutable_var[3][True] = False # нельзя менять объекты в кортеже
immutable_var[1][1]=1# изменяемы типы данных, такие как список можно менять
print('Immutable_var:',immutable_var)
mutable_list=["Дата моего рождения:", 6, 11,1988, True]
print('Mutable list:', mutable_list)
mutable_list[4] = False
print('Mutable list:', mutable_list)