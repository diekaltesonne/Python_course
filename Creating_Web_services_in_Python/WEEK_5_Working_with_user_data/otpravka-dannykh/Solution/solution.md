Решение задания по отправке данных
Для решения этого задания достаточно библиотеки requests и консоли python.
```Python
Python 3.6.5 (default, Apr 1 2018, 05:46:30) [GCC 7.3.0] on linuxType "help",
"copyright", "credits" or "license" for more information.
>>> import json
>>> import requests
>>> headers = {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'}
>>> response = requests.post('http://79.137.175.13/submissions/1/', headers=headers)
>>> json.loads(response.content.decode('utf-8'))
{'password': 'ktotama', 'path': 'submissions/super/duper/secret/', 'instructions': 'Сделайте PUT запрос на тот же хост, но на path указанный в этом документе c логином и паролем из этого документа. Логин и пароль также передайте в заголовке Authorization.', 'login': 'galchonok'}
```
Далее кодируем новый логин и пароль в base64.
```Python
>> import base64
>>> base64.b64encode(b'galchonok:ktotama')
b'Z2FsY2hvbm9rOmt0b3RhbWE='
```
После этого делаем еще один запрос на новую точку API.
```Python
>>> headers = {'Authorization': 'Basic Z2FsY2hvbm9rOmt0b3RhbWE='}
>>> response = requests.put('http://79.137.175.13/submissions/super/duper/secret/', headers=headers)
>>> json.loads(response.content.decode('utf-8'))
{'answer': 'w3lc0m370ch4p73r4.2'}
```
И получаем ответ на задание.
