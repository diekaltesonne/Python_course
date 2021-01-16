import re

def find_all_digits(text):
    exp =r'\d+'#Тут напишите своё регулярное выражение
    return re.findall(exp, text)
result = find_all_digits('a123b45с6d')
print(result)
