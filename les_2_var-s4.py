#Задание 4 Шаурма

import random

lavash1 = "обычный лаваш"
lavash2 = "лаваш с сыром"
#Начинки:
filling1 = "курица"
filling2 = "говядина"
filling3 = "овощи"

lav_options = [lavash1, lavash2]
fill_options = [filling1, filling2, filling3]
choice1 = random.choices(fill_options)
choice2 = random.choices(lav_options)

print(f"Сегодня рандомно выбрана бомбическая шаурма, внутри которой {choice1}")
print(f"Берём {choice2}, с одной стороны мажем кечинезом, {choice1} идёт мелко шинкованная")
print("Так же добавляем зелень, специи и соус по вкусу. И всё это красиво закарачиваем. Можно подрумянть на гриле")
print("Приятного аппетита! Завтра будет другая шаурма)")