#注册模块
def sign_up(user):
    user_acout = user
    user_passwd = input("输入密码:")
    passwd_sure = input("确认密码:")
    if passwd_sure == user_passwd:
        print("注册成功")
        users = [user_acout,user_passwd]
        return users
user_ac=list()
users=dict()
while True:
    login_selc = input("\nsign in(登陆)\nsign up(注册)\nexit(退出)\n请输入选项:")
    if login_selc == 'sign up':
        user = input("输入用户名:")
        user_ac.append(sign_up(user))
        users[user]=user_ac
    if login_selc == 'sign in':
        while True:
            login_ac = input("输入用户名:")
            login_passwd = input("输入密码:")
            if user_ac.count(login_passwd)==1 and user_ac.count(login_ac)==1:
                    print("登陆成功")
                    break
            else:
                print("登陆失败，请检查")
                break
    print(users)
    print(user_ac)
    if login_selc == 'exit':
        break