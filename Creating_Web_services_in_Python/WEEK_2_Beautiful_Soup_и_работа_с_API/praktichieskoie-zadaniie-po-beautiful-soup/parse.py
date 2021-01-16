from bs4 import BeautifulSoup
import re

def get_image(body):
    #imgs = len((body.find_all('img', width=lambda x: int(x or 0) > 199))
    list = []
    for tag in body.find_all('img'):
        if(int(tag.attrs.get('width') or 0)>=200):
            list.append(tag.attrs.get('width'))
    return len(list)

# Количество заголовков (h1, h2, h3, h4, h5, h6), первая буква текста внутри
# которых соответствует заглавной букве E, T или C.
# Например: <h1>End</h1> или <h5><span>Contents</span></h5>,
# но не <h1>About</h1> и
# не <h2>end</h2> и не <h3><span>1</span><span>End</span></h3>

def get_headers(body):
    count = 0
    #headers = len([i.text for i in body.find_all(name=re.compile(r'[hH1-6]{2}')) if i.text[0] in 'ETC'])
    for i in body.findAll(["h1", "h2", "h3", "h4", "h5", "h6"]):
        if i.text[0] in 'ETC':
            count+=1;

    #re.compile("(^E|^T|^S)[\s\S]+")
    return count
# Длину максимальной последовательности ссылок, между которыми нет

# других тегов, открывающихся или закрывающихся.
# Например: <p><span><a></a></span>, <a></a>, <a></a></p> - тут 2 ссылки подряд,
# т.к. закрывающийся span прерывает последовательность.
    # <p><a><span></span></a>, <a></a>, <a></a></p> - а тут 3 ссылки
# подряд, т.к. span находится внутри ссылки, а не между ссылками.

def get_linkslen(body):
    linkslen = 0
    for a in body.find_all('a'):
        a_siblings = a.find_next_siblings()
        len_arr = 1
        for sib in a_siblings:
            if sib.name == 'a':
                len_arr+=1
            else:
                break
            if len_arr > linkslen:
                linkslen = len_arr
    return linkslen



# Количество списков (ul, ol), не вложенных в другие списки.
# Например: <ol><li></li></ol>, <ul><li><ol><li></li></ol></li></ul> -
# два не вложенных списка (и один вложенный)

def get_lists(body):
    count = 0
    all_lists = body.find_all(['ul', 'ol'])
    for tag in all_lists:
        if not tag.find_parent(['ul', 'ol']):
            #print (tag.find_parent())
            count += 1

    lists = 0
    html_lists = body.find_all(['ul', 'ol'])
    for html_list in html_lists:
        if not html_list.find_parents(['ul', 'ol']):
            lists += 1
    return count



def parse(path_to_file):
    with open(path_to_file, encoding='utf-8') as data:
            soup = BeautifulSoup(data, "lxml")
    body = soup.find(id="bodyContent")
    #soup = BeautifulSoup(contents,  "html.parser")
    imgs = get_image(body)
    headers = get_headers(body)
    linkslen = get_linkslen(body)
    lists = get_lists(body)
    return [imgs, headers, linkslen , lists]
