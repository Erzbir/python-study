#注册模块
def sign_up(user):
    user_acout = user
    user_passwd = input("输入密码:")
    passwd_sure = input("确认密码:")
    if passwd_sure == user_passwd:
        print("\n注册成功")
        users = [user_acout,user_passwd]
        return users
def sign_in():
    while True:
        login_ac = input("输入用户名:")
        login_passwd = input("输入密码:")
        if login_ac in users[login_ac]:
            if login_passwd in users[login_ac]:
                print("\n登陆成功")
                break
            else:
                print("\n登陆失败,请检查")
                break
users=dict()
while True:
    login_selc = input("\nsign in(登陆)\nsign up(注册)\nexit(退出)\n请输入选项:")
    if login_selc == 'sign up':
        user = input("输入用户名:")
        users[user]=(sign_up(user))
    if login_selc == 'sign in':
        sign_in()
    if login_selc == 'exit':
        break