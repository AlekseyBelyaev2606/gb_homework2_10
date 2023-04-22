coin = []
while (True):

    temp = int(input("Заполните монеты в формате 0 1 или 2 для выхода"))

    if temp == 2:
        break
    elif temp != 0 and temp != 1:
        print("Вы ввели неправильный формат")
        break
    else:
        coin.append(temp)

print(coin)

zero, one = 0, 0
for i in coin:
    if coin[i] == 1:
        zero += 1
    else :
        one += 1
print(zero,one)
print(f"Надо перевернуть {min(zero, one)} штук(и)")