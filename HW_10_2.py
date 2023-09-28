# Задание 2.Возьмите любую из задач с прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса,
# а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

# Задание 2 из Семинара 6
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint


class GuessNumber:
    _LOWER_LIMIT = 0
    _UPPER_LIMIT = 100
    _TRY_QUANTITY = 5


    def __init__(self, lower_limit=_LOWER_LIMIT, upper_limit=_UPPER_LIMIT, try_quantity=_TRY_QUANTITY):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.try_quantity = try_quantity


    def guess(self):
        print(f"Я загадаю случайное число в диапазоне от {self.lower_limit} до {self.upper_limit}.\nУ тебя есть {self.try_quantity} попыток, чтобы угадать его")
        num = randint(self.lower_limit, self.upper_limit)
        try_counter = self.try_quantity
        while try_counter > 0:
            input_data = int(input(f"Кол-во оставшихся попыток: {try_counter}. Введи число: "))
            if input_data < self.lower_limit or input_data > self.upper_limit:
                print("Неверный ввод!")
            elif num == input_data:
                print(f"Угадал - загаданное мной число: {num}")
                return True
            elif num > input_data:
                print(f"Назови большее число")
            else:
                print(f"Назови меньшее число")
            try_counter -= 1
        else:
            print(f"У тебя больше не осталось попыток. Я загадал число {num}")
        return False

if __name__ == "__main__":
    p = GuessNumber(1, 10, 5)
    p.guess()