from django import template
register = template.Library()
# Фильтр inc. Необходимо в файле extras.py создать фильтр “inc“ который принимает
# 2 аргумента: 1-й - число которое нужно увеличить,
# 2-й - на сколько нужно увеличить первое число.
# Пример использования фильтра “inc“
# представлен в файле template/templates/filters.html

@register.filter(name = 'inc')
def inc(num,inc):
    return int(num) + int(inc)

@register.simple_tag
def division(delim, delit,to_int = False):
    if(to_int):
        return int(int(delim)/int(delit))
    else:
        return int(delim)/int(delit)

# <!--{% division a b to_int=True %}
# {% division a b %}*/-->
# 2.2. Тег division. Необходимо в файле extras.py создать тег “division“
# (то есть тег для деления),
# который принимает 3 параметра: 1-ый - делимое,  2-ой - делитель,
# 3-ий — флаг определяющий тип возвращаемого значения для результата деления
# (именованный аргумент to_int).
# Если переданное значение to_int равно False,
# необходимо выполнить вещественное деление.
# Если передано True результат вещественного деления необходимо привести к целому.
# Значение to_int по-умолчанию — False.
