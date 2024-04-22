s = input("Введите строку:")
glas = 0
soglas = 0
bykv1 = set("уеыаоэяию")
bykv2 = set("цкнгшщзхфвпрлджчсмтб")
for str in s:
    if str in bykv1:
        glas += 1
    if str in bykv2:
        soglas += 1
print("Количество гласных равно: ", glas)
print("Количество согласных равно: ", soglas)