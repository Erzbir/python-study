print("欢迎来到英雄联盟")
#登录界面 p1
def sign_up(user):
    user_acout = user
    user_passwd = input("输入密码:")
    passwd_sure = input("确认密码:")
    if passwd_sure == user_passwd:
        print("\n注册成功")
        users = [user_acout,user_passwd]
        return users
users=dict()
j=1
while True:
    login_selc = input("\nsign in(登陆)\nsign up(注册)\nexit(退出)\n请输入选项:")
    if login_selc == 'sign up':
        user = input("输入用户名:")
        users[user]=(sign_up(user))
    if login_selc == 'sign in':
        while True:
            login_ac = input("输入用户名:")
            login_passwd = input("输入密码:")
            if login_ac in users[login_ac] and login_passwd in users[login_ac]:
                    print("\n登陆成功")
                    j=0
                    break
            else:
                print("\n登陆失败,请检查")
                j=1
                break
    if login_selc == 'exit':
        break    
    if j == 0:    
        print("\t英雄联盟商城首页\n")
        print("~*~*~*~**~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n")
        while True:
            print("\t     1.进入英雄商城")
            print("\t     2.休闲小游戏")
            print("\t     3.退出登录")
            a=input("(温馨提示)请输入您的选项:")
            if a=='1':
                while True:
                    print("\t\t英雄联盟商城")
                    print("1.英雄\n2.皮肤\n3.表情")
                    b=input("输入选项,exit退出:")
                    if b=='exit':
                        break
                    while True:
                        if b=='1':
                            #英雄列表 p3
                            print("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
                            print("编号  姓名  昵称  价格  库存  描述")
                            print("1  纳尔  迷失之牙  4800  100  丛林不会原谅盲目与无知")
                            print("2  瑞雯  放逐之刃  4800  100  她是残忍高效的战士")
                            print("3  薇恩  暗夜猎手  4800  100  这个世界不像人们想象的那么美好")
                            print("4  扎克  生化魔人  4800  100  即使你没有脊柱，你也必须站起来")
                            print("5  杰斯  未来守护者 4800 100  武装着睿智与魅力，你的选择没有错")
                            print("\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
                            q=input("请输入购买的英雄编号,q退出:")
                            if q=='1':
                                #英雄详情页面 p4
                                print("英雄详情\n")
                                print("\t\t\t\t英雄商城购买英雄")
                                print("英雄购买票据")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                print("\t英雄名称:纳尔")
                                print("\t英雄属性:HP400")
                                print("\t英雄价格:4800")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                buy=input("请付款,yes or no:")
                                #订单页面 p5
                                if buy=='yes':
                                    print("\t\t\t\t英雄商城购买英雄")
                                    print("英雄购买票据")
                                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                    print("\t英雄名称:纳尔")
                                    print("\t英雄属性:HP400")
                                    print("\t英雄价格:4800")
                                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                    print("购买成功")
                                if buy=='no':
                                    print('取消购买')
                            if q=='2':
                                print("英雄详情\n购买界面\n")
                                print("\t\t\t\t英雄商城购买英雄")
                                print("英雄购买票据")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                print("\t英雄名称:瑞雯")
                                print("\t英雄属性:HP400")
                                print("\t英雄价格:4800")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                buy=input("请付款,yes or no:")
                                if buy=='yes':
                                    print("购买成功")
                                if buy=='no':
                                    print('取消购买') 
                            if q=='3':
                                print("英雄详情\n购买界面\n")
                                print("\t\t\t\t英雄商城购买英雄")
                                print("英雄购买票据")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                print("\t英雄名称:薇恩")
                                print("\t英雄属性:HP400")
                                print("\t英雄价格:4800")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                buy=input("请付款,yes or no:")
                                if buy=='yes':
                                    print("购买成功")
                                if buy=='no':
                                    print('取消购买')                                                                     
                            if q=='4':
                                print("英雄详情\n购买界面\n")
                                print("\t\t\t\t英雄商城购买英雄")
                                print("英雄购买票据")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                print("\t英雄名称:扎克")
                                print("\t英雄属性:HP400")
                                print("\t英雄价格:4800")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                buy=input("请付款,yes or no:")
                                if buy=='yes':
                                    print("购买成功")
                                if buy=='no':
                                    print('取消购买') 
                            if q=='5':
                                print("英雄详情\n购买界面\n")
                                print("\t\t\t\t英雄商城购买英雄")
                                print("英雄购买票据")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                print("\t英雄名称:杰斯")
                                print("\t英雄属性:HP400")
                                print("\t英雄价格:4800")
                                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n\n")
                                buy=input("请付款,yes or no:")
                                if buy=='yes':
                                    print("购买成功")
                                if buy=='no':
                                    print('取消购买') 
                            if q=='q':
                                break
                        if b=='2':
                            print("源计划-风")
                            print("黑夜使者")
                            q=input("q退出:")
                            if q=='q':
                                break
                        if b=='3':
                            print("魂罗")
                            q=input("q退出:")
                            if q=='q':
                                break
            if a=='2': 
                while True:
                    c=input("暂未开放,q退出:")
                    if c=='q':
                        break
            if a=='3':
                break