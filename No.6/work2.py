import datetime
import hashlib
import os
import os.path
import pickle

salt_1 = "$%&^*$(#*%#*@(943234243kjcasn"


# 加密
def hash_passwd(obj_name, salt=salt_1):
    md5 = hashlib.md5(obj_name.encode("utf-8"))
    md5.update(salt.encode("utf-8"))
    return md5.hexdigest()


# 存储
def pic_save(obj, path):
    in_file = open(path, 'wb')
    pickle.dump(obj, in_file)
    in_file.close()
    return True


# 读取
def pic_read(path):
    out_file = open(path, 'rb')
    file = pickle.load(out_file)
    out_file.close()
    return file


# 注册模块
def sign_up(user_accout):
    users_ins = []
    user_passwd = input("输入密码:")
    passwd_sure = input("确认密码:")
    user_passwd_hash = hash_passwd(user_passwd)
    if passwd_sure == user_passwd:
        print("\n\t\t\t\t\t\t\t\t*********注册成功*********\n")
        users_ins = [user_accout, user_passwd_hash]
    os.mkdir("/Users/erzbir/test/" + user_accout)
    pic_save(users_ins, "/Users/erzbir/test/" + user_accout + '/' + user_accout + ".info")
    pets(user_accout)
    return users_ins


# 登陆
def sign_in():
    login_ac = input("输入用户名:")
    user_up = pic_read("/Users/erzbir/test/" + login_ac + '/' + login_ac + ".info")
    login_passwd = input("输入密码:")
    login_passwd_hash = hash_passwd(login_passwd)
    if login_ac in user_up:
        if login_passwd_hash in user_up:
            print("\n\t\t\t\t\t\t\t\t*********登陆成功*********\n")
            return login_ac
        else:
            print("\n\t\t\t\t\t\t\t\t*********登陆失败,请检查*********")
            return False


# 文章创建
def article_create(user_accout, article_name):
    article_user = user_accout
    print("\t\t\t\t\t\t\t\t", end='')
    create_time = datetime.datetime.now()
    article_own = [article_name, article_user, create_time]
    os.mkdir('/Users/erzbir/test/' + article_user + '/articles/')
    pic_save(article_own, '/Users/erzbir/test/' + article_user + '/' + 'articles' + '/' + article_name + '.info')
    print("\n\t\t\t\t\t\t\t\t*********创建成功*********\n")
    return article_name


# 读取文章信息
def article_info_read(article_user, article_name):
    file = pic_read('/Users/erzbir/test/' + article_user + '/' + 'articles' + '/' + article_name + '.info')
    print(file)
    print("\n\t\t\t\t\t\t\t\t*********信息读取成功*********\n")


# 写入文章内容
def article_write(article_user, article_name):
    file = open('/Users/erzbir/test/' + article_user + '/' + 'articles' + '/' + article_name + '.txt', "wb")
    while True:
        txt = input()
        if txt == '\\0':
            break
        file.write((txt + '\n').encode())
        file.flush()
    file.close()
    print("\n\t\t\t\t\t\t\t\t*********写入成功*********\n")


# 读取文章内容
def article_read(article_user, article_name):
    file = open('/Users/erzbir/test/' + article_user + '/' + 'articles' + '/' + article_name + '.txt', 'rb')
    print(file.read().decode('utf-8'))
    file.close()
    print("\n\t\t\t\t\t\t\t\t*********内容获取成功*********\n")


def pets(article_user):
    os.mkdir('/Users/erzbir/test/' + article_user + '/pet/')
    feeling = 50
    level = 1
    pet_name = input("输入宠物名:")
    pet = [level, feeling]
    pic_save(pet, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
    print("\n\t\t\t\t\t\t\t\t*********宠物生成成功*********\n")
    return pet


def pet_manage(article_user, pet_name, *seles):
    pet_info = pic_read('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
    print("\t\t\t\t\t\t\t\t", end='')
    sele = input("view, feed, play\n输入:")
    if sele == 'view' or seles == 'view':
        print("\t\t\t\t\t\t\t\t", end='')
        print("宠物信息如下:")
        print("\t\t\t\t\t\t\t\t", end='')
        print(pet_info)
    if sele == 'feed':
        print("\t\t\t\t\t\t\t\t", end='')
        foods = input("选择食物 apple cake tomato:")
        if foods == 'apple':
            pet_info[1] += 5
            pet_info[0] += 0.5
            print("\t\t\t\t\t\t\t\t", end='')
            print("!!!!!心情+5，等级+0.5!!!!!\n")
            os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
            pic_save(pet_info, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
        if foods == 'cake':
            pet_info[1] += 10
            pet_info[0] += 0.5
            print("\t\t\t\t\t\t\t\t", end='')
            print("!!!!!心情+10，等级+0.5!!!!!\n")
            os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
            pic_save(pet_info, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
        if foods == 'tomato':
            pet_info[1] += 0
            pet_info[0] += 0.5
            print("\t\t\t\t\t\t\t\t", end='')
            print("!!!!!心情+0，等级+0.5!!!!!\n")
            os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
            pic_save(pet_info, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
    if sele == 'play':
        pet_info[1] += 10
        pet_info[0] += 1
        print("\n\t\t\t\t\t\t\t\t", end='')
        print("!!!!!心情+20，等级+1!!!!!\n")
        os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
        pic_save(pet_info, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')


while True:
    print("\t\t\t\t\t\t\t\t", end='')
    print("sign in(登陆)\n\t\t\t\t\t\t\t\tsign up(注册)\n\t\t\t\t\t\t\t\texit(退出)")
    login_selc = input('请输入选项:')
    if login_selc == 'exit':
        break
    if login_selc == 'sign up':
        user = input("输入用户名:")
        sign_up(user)
    if login_selc == 'sign in':
        user = sign_in()
        input()
        if user:
            while True:
                print("\t\t\t\t\t~~~~~~~~~~~~~~~选项~~~~~~~~~~~~~~~~:\n\t\t\t\t\t\t\t\tcreate\n\t\t\t\t\t\t\t\tcat state\n\t\t\t\t\t\t\t\tedit\n\t\t\t\t\t\t\t\tview txt\n\t\t\t\t\t\t\t\tself\n\t\t\t\t\t\t\t\tpet\n\t\t\t\t\t\t\t\texit\n")
                selec = input("输入选项:")
                if selec == 'exit':
                    break
                if selec == 'create':
                    name = input("输入文章名:")
                    article_create(user, name)
                    input()
                if selec == 'cat state':
                    name = input('输入文章名:')
                    article_info_read(user, name)
                    input()
                if selec == 'edit':
                    name = input('输入文章名:')
                    article_write(user, name)
                    input()
                if selec == 'view txt':
                    name = input('输入文章名:')
                    article_read(user, name)
                    input()
                if selec == 'pet':
                    pet_ownname = input('输入宠物名称:')
                    pet_manage(user, pet_ownname)
                if selec == 'self':
                    info = pic_read("/Users/erzbir/test/" + user + '/' + user + ".info")
                    s = input("是否查看宠物(yes,no):")
                    if s == 'yes':
                        pet_ownname = input('输入宠物名称:')
                        pet_manage(user, pet_ownname, 'view')
                        print(info)
                        input()
                    if s == 'no':
                        print(info)
                    input()
