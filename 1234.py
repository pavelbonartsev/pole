import random
b, answer = ["Молоко", "Собака"], ""
while answer != "Хватит":
    if len(b) == 0:
        break
    ind = random.randint(0, len(b)) - 1
    cur = ["*"] * len(b[ind])
    while "*" in cur:
        for i in cur:
            print(i, end="")
        print()
        print("Выберите букву, которую хотели бы открыть. Или если фортуна сегодня на вашей стороне, попробуйте отгадать слово целиком (регистр не учитывается).")
        l = input()
        while l.lower() not in b[ind] and l.upper() not in b[ind] and (len(l) != 1 and (l.lower() == b[ind].lower())):
            if len(l) != 1:
                print("Букву...")
            else:
                print("Такой нет. Попробуйте другую.")
            l = input()
        if l.lower() == b[ind].lower():
            print("Будем считать, что вам повезло.")
            cur = b[ind]
        else:
            for i in range(0, len(b[ind])):
                if b[ind][i] == l.lower() or b[ind][i] == l.upper():
                    cur[i] = b[ind][i]
    for i in cur:
            print(i, end="")
    print()
    print("Поздравляем! Слово открыто.")
    del b[ind]
print("Банк слов израсходован.")
    
