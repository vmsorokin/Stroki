#1st_program
my_dict={'Миша': 2007,
            'Лера': 2013,
            'Давид': 2017,
            'Даниил': 2017}
print('Список:',my_dict)
print('Существующее значение:', my_dict['Лера'])
print('Не существующее значение:', my_dict.get('Катя'))
del_=my_dict.pop('Миша')
print('Удаленное значение:',del_)
my_dict.update({'Вика':1989,
                'Ксюша':1985})
print('Обновленный список:',my_dict)
#2sr_program
my_set={6,12,23,18,9,'Дни рождения','Праздники', 9,18, 'Праздники'}
print('Set:', my_set)
my_set.update([255, 'Ура, работает!'])
my_set.remove('Праздники')
print('Новый Set:', my_set)