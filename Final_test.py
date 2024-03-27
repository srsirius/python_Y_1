from datetime import datetime as dt

FORMAT = ('%H:%M:%S')
WEIGHT = 75   # вес
HEIGHT = 175  # рост
K_1 = 0.035   # коэф. для подсчета каллорий
K_2 = 0.029   # коэф. для подсчета каллорий
STEP_M = 0.65  # длина шага в метрах
TRANSFER_COEFF = 1000  # кэф для пересчета км в метры

storage_data = {}  # словарь для хранения полученных данных

def check_correct_data(data):
    """ Проверка корректности полученных данных """

    if len(data) != 2 or data[0] is None or data[1] is None:
        return False
    return True

def chek_correct_time(time):
    """ Проверка корректности полученного времени """
    for time_check in storage_data.keys():
        if time_check >= time and storage_data != {}:
            return False
    return True

def get_steps_day(steps):
    """ Получение шагов пройденых за день"""

    for step in storage_data.values():
        steps += step

    return  steps

def get_distance(steps):
    """ Расчитать дистанцию в км исходя из пройденных шагов и их длины"""

    distant = round(steps * STEP_M / TRANSFER_COEFF, 2)
    return distant

def get_spent_calories(dist, current_time):
    """ Получить значение потраченых калорий"""

    hours = current_time.hour + current_time.minute / 60
    mean_speed = dist / hours
    spent_calories = round((K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * hours * 60, 2)
    return spent_calories

def get_achievement(dist):
    """ мотивирующие сообщения"""

    if dist >= 6.5:
        achievement = 'Отличный результат! Цель достигнута'
    elif dist >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'

    return achievement


if __name__ == '__main__':
    current_time = dt.now()
    get_spent_calories(6, current_time)
    print(current_time)
    print(get_spent_calories(6, current_time))



