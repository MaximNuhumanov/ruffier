text_index = "Ваш індекс Руф'є: "
text_workheart = "Працездатність серця: "
list_rez = [
    "Звернітся до лікаря, вам потрібний медичний огляд",
    "Поганий функціональний стан",
    "Середній функціональний стан",
    "Гарний функціональний стан",
    "Чудовий функціональний стан"]


def ruffier_index(P1, P2, P3):
    ruffier_index = (4 * (P1 + P2 + P3) - 200) / 10
    return ruffier_index

def max_ruffier_index(age):
    index = (min(age, 15) - 7) // 2
    result = 21 - index * 1.5
    return result

def ruffier_level(ruffier_ind, max_ruffier_ind):


    if ruffier_ind >= max_ruffier_ind: 
        return 0

    max_ruffier_ind = max_ruffier_ind - 4
    
    if ruffier_ind >= max_ruffier_ind: 
        return 1

    max_ruffier_ind = max_ruffier_ind - 5
    
    if ruffier_ind >= max_ruffier_ind: 
        return 2

    max_ruffier_ind = max_ruffier_ind - 5.5
    
    if ruffier_ind >= max_ruffier_ind: 
        return 3
    
    return 4
    
def test(P1,P2,P3,age):
    if age < 7:
        return "Неможливо розрахувати індекс Руф'є (для віку нижче 7 років недостатньо досліджень щоб робити висновки стосовно стану здоров'я)"
    ruffier_ind = ruffier_index(P1,P2,P3)
    if ruffier_ind < 0:
        return "Введений пульс занадто низький. Можливо ви помилились під час вимірювання, або вам варто звернутись до лікаря" 
    max_ruffier_ind = max_ruffier_index(age)
    level = ruffier_level(ruffier_ind, max_ruffier_ind)
    return text_index + str(ruffier_ind) + "\n" + text_workheart + list_rez[level]

