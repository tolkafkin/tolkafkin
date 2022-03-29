# генераторы списков и числовые списки
for number in range(1,21):
    print(number)

one_million = [num for num in range(1,1000001)]
print(sum(one_million))
print(min(one_million))
print(max(one_million))
# for num in one_million:
#     print(num)

odd_numbers = [odd for odd in range(1,21,2)]
for odd in odd_numbers:
    print(odd)

print('_____________________________________________')
multiples_of_three = [nums for nums in range(3,31,3)]
for nums in multiples_of_three:
    print(nums)

print('_____________________________________________') 
cubes = [value**3 for value in range(1,11)]
for value in cubes:
    print(value)

cubes1 = map(lambda x: x**3, range(1, 11))#способ от Санька
for value in cubes1:
    print(value)
    
cubes2 = map(lambda x: x**3, range(1, 11))# и её один способ
for value in cubes2:
    print(value)