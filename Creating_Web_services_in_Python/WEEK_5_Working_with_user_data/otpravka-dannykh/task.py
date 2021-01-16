import requests
import base64
from requests.auth import HTTPBasicAuth
def posting():
    headers= {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'}
    url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'
    r = requests.post(url, headers=headers)
    print(r.text)
def posting_1():
    #headers= {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'}
    #url = 'https://datasend.webpython.graders.eldf.ru/submissions/1/'
    #r = requests.post(url, headers=headers)
    #print(r.text)
    password =  "ktotama"
    login = "galchonok"
    spec = base64.b64encode(f"{login}:{password}".encode())
    spec_2 = 'Basic'+' '+spec.decode('ascii')
    spec_2 = spec.decode('ascii')
    headers= {'Authorization': spec_2}
    #print(spec_2)
    r1 = requests.put('https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/', auth=("galchonok", "ktotama"))
    print(r1.text)

#posting()
posting_1()
