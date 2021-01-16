# Полезные ссылки и дополнительные примеры - part_1
1. "Компьютерные сети. Принципы, технологии, протоколы. Учебник" - Виктор Олифер, Наталия Олифер. Главы, которые стоит изучить: адресация в стеке протоколов TCP/IP, протокол межсетевого взаимодействия, базовые протоколы TCP/IP, адресация в стеке протоколов TCP/IP (Система DNS), сетевые службы (Протокол HTTP)
2. Спецификация протокола IP (https://tools.ietf.org/html/rfc791)
3. Спецификация протокола TCP (https://tools.ietf.org/html/rfc793)
4. Спецификация протокола UDP (https://tools.ietf.org/html/rfc768)
5. Спецификация протокола DNS (https://www.ietf.org/rfc/rfc1034.txt и https://www.ietf.org/rfc/rfc1035.txt)
6. Спецификация протокола HTTP (https://tools.ietf.org/html/rfc2616)
7. Документация от Mozilla по HTTP (https://developer.mozilla.org/ru/docs/Web/HTTP)

# Полезные ссылки и дополнительные примеры - part_2
Полезные ссылки:
* Документация Python: Модуль re https://docs.python.org/3/library/re.html
* Хабрахабр: Регулярные выражения в Python от простого к сложному https://habrahabr.ru/post/349860/
* regex101.com: Проверка регулярных выражений online https://regex101.com/
* Hackerrank: Практика по regexp https://www.hackerrank.com/domains/regex
* Книга: Фридл Дж. Регулярные выражения 3-е издание

# И несколько практических примеров:
``` python
# Найти все действительные числа, например: -100; 21.4; +5.3; -1.5; 0
res = re.findall(r"[-+]?\d+(?:\.\d+)?", test_str)


# Проверить, что строка это серийный номер вида 00XXX-XXXXX-XXXXX-XXXXX, где X - шестнадцатиричная цифра
if re.match(r"^00[\da-f]{3}(?:-[\da-f]{5}){3}$", serial_str, re.IGNORECASE):


# Проверить, что строка является корректным IPv4 адресом
if re.match(r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.|$)){4}(?<!\.)$", ip_str):


# Проверить, что логин содержит от 8 до 16 латинских букв, цифр и _
if re.match(r"^\w{8,16}$", login):


# Проверить, что пароль состоит не менее чем из 8 символов без пробелов. Пароль должен содержать хотя бы одну: строчную букву, заглавную, цифру
if re.match(r"^(?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9])\S{8,}$", password):


# Переформатировать код, убрав лишние пробелы между def, именем функции и (
# Например: def    myFunc   (x, y):  => def myFunc(x, y):
re.sub(r'def\s+(\w+)\s*\(', r'def \1(', code)


#Заменить все "camel_case" на "сamelCase"
# Например: my_function_name, peer__2__peer  =>  myFunctionName, peer2Peer
re.sub('_+([a-zA-Z\d])', lambda x: x.group(1).upper(), code.lower())
```
