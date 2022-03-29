#выдуманный список со всеми изученными функциями

chip_companys = ['amd','intel', 'qualcom','mediatech','nvidea', 'samsung', 'apple', 'huawei']
print(f'Исходный вид списка:\n{chip_companys}')
print(f'Выведем отсортированный по алфавиту список:\n{sorted(chip_companys)}\nА теперь в обратном порядке:')
chip_companys.sort(reverse=True)
print(f'{chip_companys}')
chip_companys.reverse()
print(f'А теперь в обратном порядке:\n{chip_companys}')
print(f'Выведем длину нашего списка:\n{len(chip_companys)}')
popped_company= chip_companys.pop(-1)
print(f'Удаляем последний элемент списка и выводим их с заглавной буквы:\n{popped_company.title()}')
print(f'Проверим длину нашего списка и его состав:\n{len(chip_companys)}\n{chip_companys}')
chip_companys.reverse()
print(f'А теперь в обратном порядке:\n{chip_companys}')
del chip_companys[-1]
print(f'Удалим последний элемент через del:\n{chip_companys}')
chip_companys.append("amd")
print(f'Вернём последний элемент через append():\n{chip_companys}')
chip_companys.remove('intel')
print(f'Уберём элемент "intel" элемент через remove():\n{chip_companys}')
chip_companys.insert(0,'intel')
print(f'Вернём элемент "intel" через insert() на 0 позицию:\n{chip_companys}')