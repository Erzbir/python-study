import os
import sys
from os import path


def scanner_file(url):
    dir_list = os.listdir(url)
    for filename in dir_list:
        real_url = path.join(url, filename)

        if path.isfile(real_url):
            print(path.abspath(real_url))
        elif path.isdir(real_url):
            scanner_file(real_url)


a = input("位置:")
scanner_file(a)


# if __name__ == '__main__':
#     if len(sys.argv) <= 1:
#         print("对不起，该脚本必须要传递一个路径参数！！！")
#     else:
#         scanner_file(sys.argv[1])
