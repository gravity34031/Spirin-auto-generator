# Spirin-auto-generator
Данный проект позволяет автоматически генерировать solution, projects (console app; library; mstest; winforms), создавать все необходимые зависимости между ними, и автозаполнять по шаблону каждый из файлов в проекте.
По сути проект делает шаблон для начала работы на сайте s1-programming, не тратя ~5 минут на создание шаблона, позволяя сразу перейти к выполнению задания

# Как пользоваться?
1. Установи python. Это можно сделать через магазин Microsoft Store. Либо же через любой другой источник
2. Скачай файл main.py
3. Отредактируй main.py, вставляя в настройки свои параметры. 
    Отредактировать можно любым инструментом, включая пкм->открыть с помощью->блокнот
    Редактировать нужно только блок SETTINGS, находящийся в самом верху. Нужно поменять значения следующих переменных:
        - projects_directory - Путь к папке, где находятся ВСЕ solution(спринты). Не конкретно взятый solution(спринт)! 
            ЗАМЕЧАНИЕ:  Папки в пути должны быть разделены двумя слэшами: не '\', а '\\'
            Пример ПРАВИЛЬНЫЙ: "C:\\Users\\c# sprints"
            Пример НЕПРАВИЛЬНЫЙ: "C:\Users\# sprints"
        - initials - От них будут зависить названия файлов
        - initials_ru - Нужно для заполнения Program.cs - вывода фио на экран
        - sprint_number - номер текущего спринта. Не забывать менять раз в 7 тасков
        - title - Заголовок текущего таска. Копировать с сайта
        - condition - Описание задания. Брать с сайта
4. Запустить скрипт main.py любым способом. Можно просто кликнуть 2 раза.
5. Ввести номер текущего таска и номер варианта через пробел
    Пример: №таска №варианта через пробел: 1 4
6. После завершения создания, перезапустить visual studio

# Замечания
Если solution уже существует, то программа будет работать непосредственно с ним, но если вы перешли к другому спринту, при этом не создав новый solution, то скрипт создаст и заполнит его сам. В таком случае все будет точно таким же, но !!!впервый раз необходимо будет запустить solution через проводник, открыв файл Tyuiu.FIO.Sprint0.sln вручную, либо выбрав его через visual studio!!! 
Если какие-то библиотеки в итоге не подключились, то проверьте, есть ли файл tyuiu.cources.programming.interfaces.dll в папке solution; и установлен ли на компьютер .net framework 8.0. с версией 4.8 работать не будет.