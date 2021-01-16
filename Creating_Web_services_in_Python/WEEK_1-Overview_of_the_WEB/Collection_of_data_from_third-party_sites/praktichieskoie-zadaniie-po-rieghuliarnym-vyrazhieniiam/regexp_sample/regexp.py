def calculate(data, findall):
    #matches = findall(r"(?:(a|b|c))(?:(\-?\+?))=(?:(a|b|c{0,1}))(?:(\-?\+?\d*))")
    matches = findall(r"\d")

    # Если придумать хорошую регулярку, будет просто
    # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
    print(matches)
    for v1, s, v2, n in matches:

        p = 0
        if s == '-':
            s = -1
            p = 1
        elif s == '+':
            s = 1
            p = 1
        else:
            s = 1
        data[v1] = data[v1] * p + (data.get(v2, 0) + int(n or 0)) * s
    return data
