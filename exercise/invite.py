invite_list =["Алина", "Семён","Ваня"]
print("\n\tРазослать приглашения:\n")
print(f"Дорогой друг, {invite_list[0]}, приглашаем тебя похавать мяса и порыгать от газировки")
print(f"Дорогой друг, {invite_list[1]}, приглашаем тебя похавать мяса и порыгать от газировки")
print(f"Дорогой друг, {invite_list[2]}, приглашаем тебя похавать мяса и порыгать от газировки")

print(f"Наш друг {invite_list[2]} не сможет прийти на встречу, поэтому мы приглашаем другого гостя")
invite_list[2] = "Анжела"
print("\n\tРазослать новые приглашения:\n")
print(f"Дорогой друг, {invite_list[0]}, приглашаем тебя похавать мяса и порыгать от газировки")
print(f"Дорогой друг, {invite_list[1]}, приглашаем тебя похавать мяса и порыгать от газировки")
print(f"Дорогой друг, {invite_list[2]}, приглашаем тебя похавать мяса и порыгать от газировки")

print("\tТак как мы приобрели\n\tновый обеденный стол - мест стало больше!\n\tМы добавляем трёх новых гостей\n\tРазослать новые приглашения:")
invite_list.insert(0, "Илья")
invite_list.insert(2, "Никита")
invite_list.append("Максим")
print("\n\tРазослать новые приглашения:\n")
print(f"Дорогой друг, {invite_list[0]}, приглашаем тебя похавать мяса и порыгать от газировки")#Переделать текст 
print(f"Дорогой друг, {invite_list[1]}, приглашаем тебя похавать мяса и порыгать от газировки")#сообщений каждому приглашённому
print(f"Дорогой друг, {invite_list[2]}, приглашаем тебя похавать мяса и порыгать от газировки")#
print(f"Дорогой друг, {invite_list[3]}, приглашаем тебя похавать мяса и порыгать от газировки")#
print(f"Дорогой друг, {invite_list[4]}, приглашаем тебя похавать мяса и порыгать от газировки")#
print(f"Дорогой друг, {invite_list[5]}, приглашаем тебя похавать мяса и порыгать от газировки\n")#

print(f"Мы очень расстроены, так как стол не успеваеют привезти и хватит места только для двух гостей\n")
not_invited = invite_list.pop()
print(f"{not_invited.title()}, мы сожалеем, но мы не можем принять тебя в этот вечер")
not_invited = invite_list.pop()
print(f"{not_invited.title()}, мы сожалеем, но мы не можем принять тебя в этот вечер")
not_invited = invite_list.pop()
print(f"{not_invited.title()}, мы сожалеем, но мы не можем принять тебя в этот вечер")
not_invited = invite_list.pop()
print(f"{not_invited.title()}, мы сожалеем, но мы не можем принять тебя в этот вечер")
print(f"{invite_list[0].title()} приглашаем тебя похавать мяса и порыгать от газировки")
print(f"{invite_list[1].title()} приглашаем тебя похавать мяса и порыгать от газировки")

del invite_list[0]
del invite_list[0]
print(invite_list)
print(len(invite_list))