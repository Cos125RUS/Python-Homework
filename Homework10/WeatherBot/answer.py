

#-----------------------------------------------------
# Создание ответа
# 
# def create_answer(tuple(str,str,str,str))
# return str
# 
def create_answer(data):
    main, temp, windSpeed, pressure = data
    main = main_translation(main)
    answer = f'{main}\nТемпература: {temp}\nСкорость ветра: {windSpeed}\nДавление: {pressure}\n\n'
    comment = temperature_comment(temp) + "\n"
    if temp > 0:
        comment += rain_comment(main) + "\n" 
    comment += wind_comment(windSpeed)
    answer += comment
    # Формируем итоговую строку
    return answer

#-----------------------------------------------------

#-----------------------------------------------------
# Метод возвращает рекмондации по погоде основываясь на температуре.
#
# def temperature_comment(string temperature):
#    return (string comment)
#
def main_translation(main):
    translate = {'Clouds': 'Облачно', 'Clear': 'Ясно', 'Rain': 'Дождь', 'Snow': 'Снег'}
    return translate[main]



#-----------------------------------------------------
# Метод возвращает рекмондации по погоде основываясь на температуре.
#
# def temperature_comment(string temperature):
#    return (string comment)
#
def temperature_comment(temperature):
    # преобразуем string в float
    temperature = float(temperature)
    comment = ""
    # оценить температуру, сгенерировать рекомендацию
    if temperature > 30:
        comment = "На улице жара как в Африке. Интересно, что говорят люди в Африке, когда на улице жарко?"
    elif 30 >= temperature > 15:
        comment = "Довольно комфортная температура. Сегодня день для мороженки - съешь шоколадную!"
    elif 15 >= temperature > 5:
        comment = "Прохладно. Но лучше чем, -5 С."
    elif 5 >= temperature > 0:
        comment = "Ну и слякоть. Ты же в калошах?"
    elif 0 >= temperature > -5:
        comment = "Лужи взялись коркой льда. Смотри не поскользнись."    
    elif -5 >= temperature > -15:
        comment = "Прохладно. Но не более того."
    elif -15 >= temperature > -30:
        comment = "Довольно холодно. Сегодня бы в баню, а не вот это вот все..."
    elif temperature <= -30:
        comment = "Ты на северном полюсе? Или это Якутия? В такую погоду лучше остаться дома!"
    return comment
#-----------------------------------------------------

#-----------------------------------------------------
# Метод возвращает рекмондации по погоде основываясь на осадках.
#
# def rain_comment(bool rain):
#    return (string comment)
#
def rain_comment(rain):
    if rain == 'rain':
        comment = "На улице дождь! Не забудь лодку."
    else:
        comment = "Дождя пока не наблюдается."
    return comment
#-----------------------------------------------------

#-----------------------------------------------------
# Метод возвращает рекмондации по погоде основываясь на скорости ветра.
#
# def rain_comment(string wind):
#    return (string comment)
#
def wind_comment(wind):
    # преобразуем string в float
    wind = float(wind)
    # если ветер дует в другую сторону
    if wind < 0:
        wind = -1 * wind
    comment = ""
    # оценить скорость ветра, сгенерировать рекомендацию
    if 0 <= wind < 1.6:
        comment = "Затишье."
    elif 1.6 <= wind < 4.8:
        comment = "Легкий ветерок. Освежает..."
    elif 4.8 <= wind < 11.3:
        comment = "Легкий бриз."
    elif 11.3 <= wind < 28.9:
        comment = "Умеренный бриз. Надо разобраться, что такое этот 'Бриз'..."
    elif 28.9 <= wind < 49.9:
        comment = "Сильный бриз. С зонтом быстрее долетишь до работы."
    elif 49.9 <= wind < 61.1:
        comment = "Сильный ветер. Одень шапку и примотай к голове на всякий случай!"
    elif 61.1 <= wind < 74.0:
        comment = "Буря. Сиди дома!"
    elif 74.0 <= wind:
        comment = "Шторм! Точно сиди дома!"
    return comment
#-----------------------------------------------------

#-----------------------------------------------------
# Пример работы методов модуля
# print(temperature_comment("-30.5"))
# print(rain_comment(False))
# print(wind_comment("-100"))
# print(main_translation('Clouds'))
#-----------------------------------------------------
