"""Игра угадай число
Компьютер сам загадывает и сам угадывает число менее чем за 20 попыток
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0
    number = np.random.randint(1, 101) # 
    min = 0
    max = 100
    while True:
        predict = round((min+max)/2) # Предсказание в диапазоне среднего значения минимального и максимального числа
        count += 1
        if number == predict: # Если число - нужное загаданное случайное число - стоп
            break
        elif number > predict: # Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа
            min = predict
        elif number < predict:
            max = predict

    # Ваш код заканчивается здесь

    return count


def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)