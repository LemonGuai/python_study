dic = {
    "ip": "192.111.1.1",
    "port": "1111",
    "uid": "lemon",
    "pwd": "111111"
}
print(dic['ip'])
print(dic)
dic['cost'] = '200 RMB'
print(dic)
dic['cost'] = '300 rmb'
print(dic['cost'])
del dic['cost']
print(dic)