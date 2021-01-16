import requests as re
import json
ACCESS_TOKEN = 'b13009f3b13009f3b13009f355b15fb16bbb130b13009f3ef77c32259b4e2fc15be826e'
V = '5.71'
id_1 = "9910602"
req = re.get('https://api.vk.com/method/users.get', params={
    'access_token': ACCESS_TOKEN,
    'user_ids': id_1,
    'v': V
    })
r2 = re.get('https://api.vk.com/method/friends.get', params={
    'access_token': ACCESS_TOKEN,
    'user_id':json.loads(req.text)['response'][0]['id'],
    'v': V,
    'fields':'bdate'
    })
data = json.loads(r2.text)
def sortBysecond(tuple):
        return tuple[1]
pr={}
lp=[]
for x in data['response']['items']:
    if 'bdate' in x:
        result = [int(item) for item in x['bdate'].split('.')]
        if(len(result)==3):
            ans = 2020 -result[2]
            #print(ans)
            if(pr.get(ans)):
                pr[ans]= pr[ans]+1
            else:
                pr[ans]= 1
for key,val in pr.items():
    lp.append((key,val))
lp.sort(key =sortBysecond, reverse=True)
print(lp)
