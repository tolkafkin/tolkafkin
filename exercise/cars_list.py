cars_list = ["Mazda Rx8", "Miata", "Honda 2000"]
print(f"My favorite lovely car is {cars_list[-2]}")
cars_list[-2]="Mazda Miata"
print(f"My favorite lovely car is {cars_list[-2]}")
cars_list.append("Audi R8")
print(cars_list)
cars_list.insert(-1, "VG Golf 2")
print(cars_list)
del cars_list[-3]
print(cars_list)
popped_cars = cars_list.pop(2)
print(cars_list)
print(popped_cars)
cars_list.remove("Audi R8")
print(cars_list)