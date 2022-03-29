#slies или сегменты
my_foods = ['pizza','falfel', 'carrot cake']
friend_foods = my_foods[:]


print(f"Выведем список моей еды:\n{my_foods}")
print(f"Выведем список еды моих друзей, который копируется из моего списка:\n{friend_foods}")
friend_foods.append('beer')
my_foods.append('mashrooms')
print(f"Добавим в каждый по одному элементу:\n{my_foods}")
print(f"{friend_foods}")
print(f"Покажем только три первых элемента этих списков:\n{my_foods[:3]}\n{friend_foods[:3]}")
print(f"Покажем 2 элемента из центра этих списков:\n{my_foods[1:3]}\n{friend_foods[1:3]}")
print(f"Покажем только три последних элемента этих списков:\n{my_foods[1:]}\n{friend_foods[1:]}")