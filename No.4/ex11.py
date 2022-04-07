account = input("输入用户名:")
if account != 'admin':
    print("用户不存在")
if account == 'admin':
    password = input("输入密码:")
    if password == '88888':
        print("密码正确，登陆成功")
    else:
        print("密码错误")