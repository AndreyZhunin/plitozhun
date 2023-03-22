from random import*
list_of_numbers = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], ['13', '14', '15', '16', '17', '18', 
'19', '20', '21', '22', '23', '24'], ['25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'], ['0'], ['00']]
list_for_random = [0, 1, 2]
number_of_chips, first_bet, desired_result = int(input()), int(input()), int(input())
bet, counter = first_bet, 0
total = 0
while True:
    total += 1
    print("Количество фишек перед ставкой:", number_of_chips)
    if number_of_chips <= bet:
        print("Вы проиграли, у вас не хватает фишек для ставки")
        break
    number = choice(choice(list_of_numbers))
    sector = choice(list_for_random)
    number_of_chips -= bet
    for i in range(3):
        if number in list_of_numbers[i]:
            dropped_sector = i
            break
    print("Ставка:", bet, "Выбранный сектор:", sector, "Выпавший сектор:", dropped_sector, "Оставшиеся фишки:", number_of_chips)
    if sector == dropped_sector:
        number_of_chips += bet * 3
        bet, counter = first_bet, 0
    else:
        counter += bet
        bet = int(counter / 2) + first_bet + 1 #ghju
        if total == 10:
            bet, counter = first_bet, 0
            total = 0
    if number_of_chips >= desired_result:
        print("Поздравляем, вы выиграли желаемую сумму!", number_of_chips)
        break
    elif number_of_chips <= first_bet:
        print("Вы проиграли, у вас закончились фишки")
        break
    print("Количество фишек после цикла:", number_of_chips)

    print("Ура")