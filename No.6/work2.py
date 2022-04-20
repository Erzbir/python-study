import datetime
import hashlib
import os
import os.path
import pickle
import uuid

salt_1 = "$%&^*$(#*%#*@(943234243kjcasn"    # 盐值


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
    if user_accout in os.listdir('/Users/erzbir/test/'):
        print("\t\t\t\t\t\t\t!!!!!!用户已存在!!!!!!")
        input()
        return False
    user_passwd = input("输入密码:")
    passwd_sure = input("确认密码:")
    user_passwd_hash = hash_passwd(user_passwd)
    if passwd_sure == user_passwd:
        print("\n\t\t\t\t\t\t\t\t*********注册成功*********\n")
        input()
        uid = '编号:' + datetime.datetime.strftime(datetime.datetime.now(), '%Y, %m, %d') + uuid.uuid4().hex
        users_ins_login = [user_accout, user_passwd_hash]
        users_ins = ['用户名:' + user_accout, '密码:' + user_passwd_hash, '编号:' + uid]
        os.mkdir("/Users/erzbir/test/" + user_accout)
        pic_save(users_ins, "/Users/erzbir/test/" + user_accout + '/' + user_accout + ".info")
        pic_save(users_ins_login, "/Users/erzbir/test/" + user_accout + '/' + user_accout + ".login")
        pets(user_accout)
        return users_ins
    else:
        print('两次密码不一致')
        return False


# 登陆
def sign_in():
    login_ac = input("输入用户名:")
    if login_ac not in os.listdir('/Users/erzbir/test/'):
        print("\t\t\t\t\t\t\t!!!!!!没有此用户!!!!!!")
        return False
    user_up = pic_read("/Users/erzbir/test/" + login_ac + '/' + login_ac + ".login")
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
    create_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y年 %m月 %d日 %H时 %M分 %S秒')
    article_own = ['文章名:' + article_name, '文章创建者:' + article_user, '创建日期:' + create_time]
    os.mkdir('/Users/erzbir/test/' + article_user + '/articles/')
    pic_save(article_own, '/Users/erzbir/test/' + article_user + '/' + 'articles' + '/' + article_name + '.info')
    print("\n\t\t\t\t\t\t\t\t*********创建成功*********\n")
    return article_name


# 读取文章信息
def article_info_read(article_user, article_name):
    if article_name + '.info' not in os.listdir('/Users/erzbir/test/' + article_user + '/articles/'):
        print("\t\t\t\t\t\t\t!!!!!!读取失败!!!!!!")
        return False
    file = pic_read('/Users/erzbir/test/' + article_user + '/' + 'articles' + '/' + article_name + '.info')
    print(file)
    print("\n\t\t\t\t\t\t\t\t*********信息读取成功*********\n")
    return True


# 写入文章内容
def article_write(article_user, article_name):
    if article_name + '.txt' not in os.listdir('/Users/erzbir/test/' + article_user + '/articles/'):
        print("\t\t\t\t\t\t\t!!!!!!文章不存在!!!!!!")
        return False
    file = open('/Users/erzbir/test/' + article_user + '/' + 'articles' + '/' + article_name + '.txt', "wb")
    while True:
        txt = input()
        if txt == '\\0':
            break
        file.write((txt + '\n').encode())
        file.flush()
    file.close()
    print("\n\t\t\t\t\t\t\t\t*********写入成功*********\n")
    return True


# 读取文章内容
def article_read(article_user, article_name):
    if article_name + '.txt' not in os.listdir('/Users/erzbir/test/' + article_user + '/articles/'):
        print("\t\t\t\t\t\t\t!!!!!!文章不存在!!!!!!")
        return False
    file = open('/Users/erzbir/test/' + article_user + '/' + 'articles' + '/' + article_name + '.txt', 'rb')
    print(file.read().decode('utf-8'))
    file.close()
    print("\n\t\t\t\t\t\t\t\t*********内容获取成功*********\n")
    return True


# 创建宠物
def pets(article_user):
    os.mkdir('/Users/erzbir/test/' + article_user + '/pet/')
    feeling = 50
    level = 1
    pet_name = input("输入宠物名:")
    pet = [level, feeling]
    pet_plist = ['level:' + str(level), 'feeling:' + ':' + str(feeling)]
    pic_save(pet, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
    pic_save(pet_plist, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
    print("\n\t\t\t\t\t\t\t\t*********宠物生成成功*********\n")
    input()
    return pet


# 宠物管理系统
def pet_manage(article_user, pet_name, *seles):
    if pet_name + '.info' not in os.listdir('/Users/erzbir/test/' + article_user + '/pet/'):
        print("\t\t\t\t\t\t\t!!!!!!没有此宠物!!!!!!")
        return False
    pet_info = pic_read('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
    pet_plist = pic_read('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
    while True:
        sele = input("\t\t\t\t\t\t\t\tview, feed, play,exit\n输入:")
        if sele == 'exit':
            print("\n\t\t\t\t\t\t\t\t!!!!!!已退出!!!!!!")
            break
        elif sele == 'view' or seles == 'view':
            print("\t\t\t\t\t\t\t\t\t", end='')
            print("宠物信息如下:")
            for stata in pet_plist:
                print("\t\t\t\t\t\t\t\t\t", end='')
                print(stata)
        elif sele == 'feed':
            foods = input("\t\t\t\t\t\t\t\t选择食物 apple cake tomato:")
            if foods == 'apple':
                pet_info[1] += 5
                pet_info[0] += 0.5
                pet_plist[0] = 'level:' + str(pet_info[0])
                pet_plist[1] = 'feeling:' + str(pet_info[1])
                print("\n\t\t\t\t\t\t\t\t!!!!!心情+5，等级+0.5!!!!!\n")
                os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
                os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
                pic_save(pet_info, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
                pic_save(pet_plist, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
            elif foods == 'cake':
                pet_info[1] += 10
                pet_info[0] += 0.5
                pet_plist[0] = 'level:' + str(pet_info[0])
                pet_plist[1] = 'feeling:' + str(pet_info[1])
                print("\n\t\t\t\t\t\t\t\t!!!!!心情+10，等级+0.5!!!!!\n")
                os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
                os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
                pic_save(pet_info, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
                pic_save(pet_plist, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
            elif foods == 'tomato':
                pet_info[1] += 0
                pet_info[0] += 0.5
                pet_plist[0] = 'level:' + str(pet_info[0])
                pet_plist[1] = 'feeling:' + str(pet_info[1])
                print("\n\t\t\t\t\t\t\t\t\t!!!!!心情+0，等级+0.5!!!!!\n")
                os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
                os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
                pic_save(pet_info, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
                pic_save(pet_plist, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
            else:
                print("\t\t\t\t\t\t\t!!!!!!请重新输入!!!!!!")
        elif sele == 'play':
            pet_info[1] += 10
            pet_info[0] += 1
            pet_plist[0] = 'level:' + str(pet_info[0])
            pet_plist[1] = 'feeling:' + str(pet_info[1])
            print("\n\t\t\t\t\t\t\t\t!!!!!心情+20，等级+1!!!!!\n")
            os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
            os.remove('/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
            pic_save(pet_info, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.info')
            pic_save(pet_plist, '/Users/erzbir/test/' + article_user + '/pet/' + pet_name + '.plist')
        else:
            print("\t\t\t\t\t\t\t!!!!!!请重新输入!!!!!!")
    return True


while True:
    print("\t\t\t\t\t\t\t\t\t", end='')
    print("sign in(登陆)\n\t\t\t\t\t\t\t\t\tsign up(注册)\n\t\t\t\t\t\t\t\t\texit(退出)")
    login_selc = input('请输入选项:')
    if login_selc == 'exit':
        break
    elif login_selc == 'sign up':
        user = input("输入用户名:")
        sign_up(user)
    elif login_selc == 'sign in':
        user = sign_in()
        input()
        if user:
            while True:
                print(
                    "\t\t\t\t\t\t\t~~~~~~~~~~~~~选项~~~~~~~~~~~~~~:\n\t\t\t\t\t\t\t\t\t\tcreate\n\t\t\t\t\t\t\t\t\t\tcat "
                    "state\n\t\t\t\t\t\t\t\t\t\tedit\n\t\t\t\t\t\t\t\t\t\tview "
                    "txt\n\t\t\t\t\t\t\t\t\t\tself\n\t\t\t\t\t\t\t\t\t\tpet\n\t\t\t\t\t\t\t\t\t\texit\n")
                selec = input("输入选项:")
                if selec == 'exit':
                    break
                elif selec == 'create':
                    name = input("输入文章名:")
                    article_create(user, name)
                    input()
                elif selec == 'cat state':
                    name = input('输入文章名:')
                    article_info_read(user, name)
                    input()
                elif selec == 'edit':
                    name = input('输入文章名:')
                    article_write(user, name)
                    input()
                elif selec == 'view txt':
                    name = input('输入文章名:')
                    article_read(user, name)
                    input()
                elif selec == 'pet':
                    pet_ownname = input('输入宠物名称:')
                    pet_manage(user, pet_ownname)
                    a = input()
                elif selec == 'self':
                    info = pic_read("/Users/erzbir/test/" + user + '/' + user + ".info")
                    s = input("是否查看宠物(yes,no):")
                    if s == 'yes':
                        pet_ownname = input('输入宠物名称:')
                        pet_manage(user, pet_ownname, 'view')
                        print(info)
                        input()
                    elif s == 'no':
                        print(info)
                    else:
                        print("\t\t\t\t\t\t\t!!!!!!请重新输入!!!!!!")
                else:
                    print("\t\t\t\t\t\t!!!!!!请重新输入!!!!!!")
                    input()
    else:
        print("\t\t\t\t\t\t\t!!!!!!请重新输入!!!!!!")
