def add(*num):
    result = 0
    for val in num:
        result += val
    return result

# result_sum = add(1,23,412)
# print(result_sum)

def sendmail(**data):
    for key, val in data.items():
        print(key,":",val)
    
sendmail(
    subject = 'python',
    content = 'study python',
    to = '1@163.com',
    cc = '2@163.com',
    try_times = 5
)