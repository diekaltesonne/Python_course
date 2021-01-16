# ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
line ="ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\neardrum.cpu 0000 0000\n\n"
line2 = "ok\n\n"
line3 ="ok\npalm.cpu 10.5 11111\neardrum.cpu 15.3 22222\neardrum.cpu 4.2 0000\neardrum.cpu 1.2 4444\n\n"
line4 ="ok\npalm.cpu 10.5 11111\n\n"
def codum(reply):
    d = {}
    repl = reply.split("\n")
    for i in repl:
        k = i.split()
        if (len(k) == 1) or (len(k) == 0) :
            continue
        key, *value = k
        if d.get(key) == None:
            d[key] =[]
            d[key].append(tuple([int(value[1]),float(value[0])]))
        else:
            d[key].append(tuple([int(value[1]),float(value[0])]))
    for key in d:
        d[key] =sorted(d[key], key=lambda range: range[0])
    return d
print(codum(line4))
