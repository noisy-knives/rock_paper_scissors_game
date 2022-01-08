import random

comp_options = ['камень', 'ножницы', 'бумага']
comp_turn = random.choice(comp_options)
print(comp_turn)
print('Юзер! Сыграем в камень, ножницы, бумага!')
users_turn = input('Твой ход, юзер: ')
if comp_turn == users_turn:
    print('Ничья!')
elif comp_turn == 'камень' and users_turn == 'ножницы' or comp_turn == 'ножницы' and users_turn == 'бумага' or comp_turn == 'бумага' and users_turn == 'камень':
    print('Компьютер победил!')
elif comp_turn == 'камень' and users_turn == 'бумага' or comp_turn == 'ножницы' and users_turn == 'камень' or comp_turn == 'бумага' and users_turn == 'ножницы':
    print('Юзер победил!')
else:
    print('Юзер, введи камень, ножницы или бумага!')