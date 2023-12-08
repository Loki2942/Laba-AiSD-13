# 13.	Определить количество взрослых(=>18), севших в порту Шербур,
# в возрастном интервале средний возраст  5 позиций и сколько из них выжило

import csv

file = open("titanic.csv", "r")
rows = list(csv.reader(file))

# Переменные для подсчета
counter_alive = 0
counter_total = 0
sum = 0
num = 0
age_list = []  # список возрастов

for i in rows:
    if i[1] == "1" or i[1] == "0":  # для обхода первой строки
        if i[5] != "" and i[5] != " ":  # Проверка на пустую строку
            if float(i[5]) >= 18.0:
                age_list.append(i[5])  # добавляем в список возрастов

for i in rows:
    if i[1] == "1" or i[1] == "0":  # для обхода первой строки
        if i[5] != "" and i[5] != " ":  # Проверка на пустую строку
            sum += float(i[5])
            num += 1
        average_age = sum / num  # средний возраст

age_list.append(str((average_age)))
sort_aglist = sorted(age_list)
indx = sort_aglist.index(str((average_age)))
average_age_list = sort_aglist[
                   indx - 5: indx + 6]  # Берем срез значений из списка +- 5 позиций, считая от индекса среднего возраста

for i in rows:
    if i[11] == "C":  # Проверка на соответствие условию C = Cherbourg Q = Queenstown S = Southampton
        if i[5] != "" and i[5] != " ":  # Проверка на пустую строку
            if i[5] in average_age_list:
                counter_total += 1
                if i[1] == "1":
                    counter_alive += 1

print(f"Взрослых, севших в порту Шейбур : {counter_total}\nИз них выжило: {counter_alive}")
