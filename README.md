<a name="readme-top"></a>
<div align="center">
  <h2>Water meter readings<br />(Показания счётчиков воды)</h2>
  <p> Моя программа для быстрого расчёта сумм к оплате по показаниям счётчиков воды. </p>
    <br />
    <br />

</div>

<!-- ABOUT THE PROJECT-->
## О проекте

Проблема: в ежемесячных квитанциях за коммунальные услуги приходят пустые поля за водоснабжение/водоотведение. Мне надоело каждый раз высчитывать на калькуляторе сколько я должен оплатить в квитанции за холодную/горячую воду по показаниям счётчиков.

<img src="https://github.com/nymedvedev/water_meter_readings/blob/main/screenshots/screenshot_utility_bill.png?raw=true" alt="Часть квитанции">

Решение: я написал программу, которая делает это максимально быстрым и удобным образом.

Дополнительно, чтобы не открывать специально IDE (в моём случае PyCharm), я сделал программу .exe-исполняемым файлом. 

<img src="https://github.com/nymedvedev/water_meter_readings/blob/main/screenshots/screenshot_directory.png?raw=true" alt="Иконка программы">

Спасибо <a href="https://www.flaticon.com/ru/free-icons/" alt="Хабр">этому</a> ресурсу за прикольную иконку счётчика для исполняемого .exe-файла.

Запущенная программа выглядит так (исполняется в командной строке).

<img src="https://github.com/nymedvedev/water_meter_readings/blob/main/screenshots/screenshot_start_program_exe.png?raw=true" alt="Старт программы">

Т.к. тарифы на воду могут меняться, программа сначала просит их проверить. Иначе будет недоплата - долг - пени.

Затем мне нужно просто ввести показания счётчиков горячей и холодной воды.
Отработавшая программа выглядит так:

<img src="https://github.com/nymedvedev/water_meter_readings/blob/main/screenshots/screenshot_program_complete.png?raw=true" alt="Программа отработала">

Программа предусматривает, что я могу ошибиться при вводе в меньшую сторону (что приведёт к образованию задолженности), поэтому просит ввести корректные показания конкретного счётчика, в противном случае завершается.

<img src="https://github.com/nymedvedev/water_meter_readings/blob/main/screenshots/screenshot_not_correct_readings.png?raw=true" alt="Неверные показания">

Также программа выводит предупреждение, если разница показаний подозрительно большая (больше или равно 10 м3).

<img src="https://github.com/nymedvedev/water_meter_readings/blob/main/screenshots/screenshot_not_big_difference.png?raw=true" alt="Большая разница показаний">

И, самое главное, программа хоранит в readings.txt предыдущие показания и текущие тарифы,
а при закрытии заменяет их на новые показания и актуальные тарифы соответственно.

<p align="right">(<a href="#readme-top">вверх</a>)</p>

## Использование

0. Я пользуюсь <b>"MS Windows"</b>, и на других платформах программу не тестировал.
   Если у вас не выполняется .exe-файл, вы всегда можете запустить программу в вашей IDE, используя файл <b>"Water_meter_readings.py"</b> из папки <a href="https://github.com/nymedvedev/water_meter_readings/tree/main/Readings%20Code">Readings Code</a>. <br /><br />
   <b>ВАЖНО</b>: в папке с python-файлом обязательно должен находиться текстовый файл <b>readings.txt</b>.<br /><br />
1. Скачайте папку <a href="https://github.com/nymedvedev/water_meter_readings/tree/main/Readings%20(exe%20desktop%20program)" alt="Ссылка на папку с проектом"><b>"Readings (exe desktop program)"</b></a> на своё устройство с <b>"MS Windows".</b><br />
1.1. Если вы запускаете программу впервые, то сначала откройте файл <b>readings.txt</b>.
   Введите в нём соотв. значения в таком порядке:
     * предыдущие показания горячей воды, м3.
     * предыдущие показания холодной воды, м3.
     * тариф за горячую воду, руб/м3.
     * тариф за хоолдную воду, руб/м3.
   Сохраните файл.
2. Запустите файл <b>Water_meter_readings.exe</b>
3. Следуйте инструкциям программы.
4. Отработавшая программа выдаст, сколько вы должны заплатить за горячую и за холодную воду.
   И справочно общую сумму к оплатиие за воду.<br /><br />
4.1. Если вы случайно ввели не те показания или тарифы, просто закройте программу и запустите заново, не доходя до конца выполнения кода. <br />
4.2. Если дошли до конца кода, и сохранились неверные значения, просто отредактируйте их в файле <b>readings.txt</b>, как в п.1.1.<br />
<br />

<p align="right">(<a href="#readme-top">вверх</a>)</p>

## Создание программы

1. Мотивация решить назойливую рутинную задачу.
2. Использовал Python3:
   * работа с файлом через with, а также file.truncate, file.seek, file.write
   * процедурный код с if / else для реакций на вводимые данные
   * input() для ввода показаний или выбора действий
   * модуль sys для вызова завершения программы
3. Для преобразования .py-файла в .exe-файл использовал библиотеку <b>auto-py-to-exe</b>,
   про неё и процесс её использования я прочитал <a href="https://habr.com/ru/companies/vdsina/articles/557316/" alt="Хабр">тут</a>.
4. Иконку для исполняемого файла взял  <a href="https://www.flaticon.com/ru/free-icons/" alt="Хабр">тут</a>.


## Разработал с помощью

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)][Python-url]


## Контакт 

Nikolay Medvedev - Telegram: @ny_medvedev - medvedev.ny@gmail.com

Project Link: [https://github.com/nymedvedev/water_meter_readings](https://github.com/nymedvedev/water_meter_readings)

[Python-url]: https://www.python.org

## [License](https://github.com/nymedvedev/water_meter_readings/blob/main/LICENSE.md)

<b>Water_meter_readings</b> © [Medvedev Nikolay](https://github.com/nymedvedev)


<p align="right">(<a href="#readme-top">вверх</a>)</p>
