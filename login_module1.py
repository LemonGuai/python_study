def login_module1():
        i += 1
        if i == 3:
                print('您登录信息输入错误次数已达3次，请稍后登录')
                break 
        else:
        pwd = input('密码错误！您还有{0}次机会，请重新输入：'.format(3-i)).strip() 