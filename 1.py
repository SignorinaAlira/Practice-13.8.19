try:
    tickets = int(input("Введите количество билетов: "))
except ValueError:
    print("Нужно ввести число!")
else:
    if tickets:
        order = {}
        summa = 0
        for visitor in range(1, tickets+1):
            try:
                age = int(input(f"Введите возраст посетителя {visitor}: "))
            except ValueError:
                print("Нужно ввести число!")
                break
            else:
                if age:
                    order[visitor] = age
                else:
                    print(f"Вы не ввели возраст посетителя {visitor}, расчет стоимости невозможен.")
                    break
        if order:
            for value in order.values():
                if 18 <= value < 25:
                    summa += 900
                elif value >= 25:
                    summa += 1390
            print(f"Сумма к оплате: {summa}")
            if tickets > 3:
                summa *= 0.9
                print(f"Сумма к оплате со скидкой: {summa}")
    else:
        print("Вы не ввели нужное количество билетов!")
