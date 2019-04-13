def __login__():
    i = 0
    uid = input('请输入用户名：').strip()
    while i <= 2:
        if uid:
            if uid == "lemon":
                pwd = input('请输入密码：').strip()
                while i <= 2:
                    if pwd:
                        if pwd == "lemon":
                            print('Welcome!Dear Lemon!')
                            break
                        else:
                            i += 1
                            if i == 3:
                                print('您登录信息输入错误次数已达3次，请稍后登录')
                                break 
                            else:
                                pwd = input('密码错误！您还有{0}次机会，请重新输入：'.format(3-i)).strip()                         
                    else:
                        i += 1
                        if i == 3:
                            print('您登录信息输入错误次数已达3次，请稍后登录')
                            break
                        else:
                            pwd = input('密码不能为空，您还有{0}次机会，请输入密码：'.format(3-i)).strip()                           
                break
            else:
                i += 1
                if i == 3:
                    print('您登录信息输入错误次数已达3次，请稍后登录')
                    break
                else:
                    uid = input('用户名错误！您还有{0}次机会，请重新输入：'.format(3-i)).strip()
        else:
            i += 1
            if i == 3:
                print('您登录信息输入错误次数已达3次，请稍后登录')
                break
            else:
                uid = input('用户名不能为空，您还有{0}次机会,请输入用户名：'.format(3-i)).strip()
         

__login__()