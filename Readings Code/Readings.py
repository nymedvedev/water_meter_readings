# Эта программа помогает легко считать стоимость коммуналки
# для оплаты за водоснабжение, чтобы не считать вручную

import sys
# БЛОК 1. ОБРАБОТКА ИСХ. ДАННЫХ

# ОТКРЫВАЕМ ФАЙЛ, В КОТОРОМ ХРАНЯТСЯ ПРЕДЫДУЩИЕ ПОКАЗАНИЯ И СООТВ.ТАРИФЫ
with open("readings.txt", "r+", encoding='cp1252') as file:
    hot_water_prev, cold_water_prev, tarif_hot_water, tarif_cold_water = file.readlines()
    # это тест содержимого файла readings.txt
    '''print("TEST: ", hot_water_prev.strip(), cold_water_prev.strip(),
          tarif_hot_water.strip(), tarif_cold_water.strip())'''
    # ПРЕОБРАЗУЮ str К ЧИСЛОВЫМ ТИПАМ
    hot_water_prev, cold_water_prev, tarif_hot_water, tarif_cold_water = \
        int(hot_water_prev), int(cold_water_prev), float(tarif_hot_water), float(tarif_cold_water)

    print("РАСЧЁТ СТОИМОСТИ ПОЛЬЗОВАНИЯ ВОДОЙ")
    print("-"*50)
    # ВЫВОД ТЕКУЩИХ ТАРИФОВ
    print("Текущие тарифы:", "\n", "Тариф за 'СТОК.ГОР.В.' = ", tarif_hot_water, "руб/м3", "\n",
          "Тариф за 'ХОЛ.В. И СТОК.' = ", tarif_cold_water, "руб/м3")

    # ПРОВЕРКА АКТУАЛЬНОСТИ ТАРИФОВ
    print("Проверьте тарифы в новой квитанции. Данные актуальны?")
    if input("Введите 'нет', если НЕ актуальны, иначе нажмите 'ENTER' ") in \
            ['нет','Нет','НЕТ','no','NO']:
        # РАЗ ТАРИФЫ ДРУГИЕ, ВВОДИМ НОВЫЕ ЗНАЧЕНИЯ
        tarif_hot_water = float(input("Введите актуальный тариф на 'СТОК.ГОР.В.': "))
        print("Тариф за 'СТОК.ГОР.В.' = ", tarif_hot_water, "руб/м3")
        tarif_cold_water = float(input("Введите актуальный тариф на 'ХОЛ.В. И СТОК.': "))
        print("Тариф за 'ХОЛ.В. И СТОК.' = ", tarif_cold_water, "руб/м3")
    else:
        print("Тарифы не изменились.")
    print("-" * 50)
    # ЕСЛИ ТАРИФЫ АКТУАЛЬНЫ, ВЫВОД СТАРЫХ ПОКАЗАНИЙ И ВВОД НОВЫХ
    print("Предыдущие показания: ", "\n", "СТОК.ГОР.В. = ", hot_water_prev, "м3", "\n",
          "ХОЛ.В. И СТОК. = ", cold_water_prev, "м3")
    print("-" * 50)

    # БЛОК 2. ВВОД НОВЫХ ДАННЫХ.

    print("Текущие показания:")
    hot_water = int(input("Введите показания счётчика КРАСНОГО цвета: "))
    # ПРОВЕРЯЕМ ВАЛИДНОСТЬ НОВЫХ ДАННЫХ
    if hot_water >= hot_water_prev:
        if hot_water-hot_water_prev>=10:
            print("-" * 50, "\n", "ПРЕДУПРЕЖДЕНИЕ: разница показаний >= 10 м3.", "\n",
                  "Проверьте корректность введённых показаний.", "\n", "-" * 50)
        print("СТОК.ГОР.В. = ", hot_water, "м3")
    else:
        print("Текущие показания не могут быть МЕНЬШЕ предыдущих.")
        hot_water = int(input("Введите КОРРЕКТНЫЕ показания КРАСНОГО счётчика: "))
        if hot_water >= hot_water_prev:
            print("СТОК.ГОР.В. = ", hot_water, "м3")
        else:
            sys.exit("Необходимо ПРОВЕРИТЬ показания КРАСНОГО счётчика. ПРОГРАММА ЗАВЕРШЕНА.")
    cold_water = int(input("Введите показания счётчика СИНЕГО цвета: "))
    if cold_water >= cold_water_prev:
        if cold_water-cold_water_prev>=10:
            print("-" * 50, "\n", "ПРЕДУПРЕЖДЕНИЕ: разница показаний >= 10 м3.", "\n",
                  "Проверьте корректность введённых показаний.", "\n", "-" * 50)
        print("ХОЛ.В. И СТОК. = ", cold_water, "м3")
    else:
        print("Текущие показания не могут быть МЕНЬШЕ предыдущих.")
        cold_water = int(input("Введите КОРРЕКТНЫЕ показания СИНЕГО счётчика: "))
        if cold_water >= cold_water_prev:
            print("ХОЛ.В. И СТОК. = ", cold_water, "м3")
        else:
            sys.exit("Необходимо ПРОВЕРИТЬ показания СИНЕГО счётчика. ПРОГРАММА ЗАВЕРШЕНА.")
    print("-" * 50)

    # БЛОК 3. РАСЧЁТ СУММ К ОПЛАТЕ.

    # CЧИТАЕМ РАЗНИЦУ ПОКАЗАНИЙ, ВЫВОДИМ СТОИМОСТЬ И ОБЩУЮ СУММУ
    hot_difference = hot_water - hot_water_prev
    cold_difference = cold_water - cold_water_prev
    print("Разница показаний:", "\n", "СТОК.ГОР.В. = ", hot_difference, "м3", "\n",
          "ХОЛ.В. И СТОК. = ", cold_difference, "м3")
    hot_pay = hot_difference * tarif_hot_water
    cold_pay = cold_difference * tarif_cold_water
    print("-" * 50)
    print("К оплате:", "\n", "За горячую воду: ", "{:.2f}".format(hot_pay), "руб.", "\n",
          "За холодную воду: ", "{:.2f}".format(cold_pay), "руб.", "\n",
          "Общая сумма за пользование водой: ", "{:.2f}".format(hot_pay+cold_pay), "руб.")

    # БЛОК 4. ОБНОВЛЯЕМ ДОКУМЕНТ С ИСХ. ДАННЫМИ.

    # УДАЛЯЕМ СТАРЫЕ ДАННЫЕ ИЗ "readings.txt", ПИШЕМ НОВЫЕ
    file.truncate(0)
    file.seek(0, 0)
    file.write(str(hot_water).strip()), file.write("\n")
    file.write(str(cold_water).strip()), file.write("\n")
    file.write(str(tarif_hot_water).strip()), file.write("\n")
    file.write(str(tarif_cold_water).strip())

    # ВЫХОДИМ ИЗ ПРОГРАММЫ
    print("-" * 50)
    input("Нажмите 'ENTER', чтобы выйти из программы.")
