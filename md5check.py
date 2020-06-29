# !/usr/bin/python3
#-*-coding:utf-8-*-

import hashlib
import os
import string
import random
import sys

runpath = os.path.dirname(os.path.realpath(__file__)) + "\\"

#把字符串转换MD5串
def get_md5(str):
    str_md5 = hashlib.md5(str.encode('utf-8')).hexdigest()
    return str_md5

'''
匹配字典猜解
wordlist表示字典
md5string表示需要猜解的md5串
'''
def check_wordlist(wordlist,md5string):
    i = 1
    with open(wordlist,'r',encoding='UTF-8') as f:
        readfile = f.read().splitlines()
        for line in readfile:
            print (f'{i}/{len(readfile)}')
            i += 1
            md5_code = line.split("|")[0]
            #print(md5_code)
            if( md5string == md5_code):
                print ("密码是：" + line.split("|")[1])
                return True
    return False

def scan_dict(file_path):
    for file_path, sub_dirs, filenames in os.walk(file_path):
        print (sub_dirs)
        return filenames

'''
尝试随机匹配3-15长度的随机密码
cnt表示尝试次数
md5string表示md5串
'''
def check_rand(cnt,md5string):
    a = 1
    fuhao = ":@#$*,.!"
    while a < cnt :
        len = random.randint(3,15)
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits + fuhao, len))
        ran_md5 = get_md5(ran_str)
        if (ran_md5 == md5string):
            print ("密码是：" + ran_str)
            return True
        a = a + 1
        print (f'{a}/{cnt}')
    return False


md5 = input("请输入需要32位的MD5串：")
if(md5):
    if(len(md5) != 32 ):
        print(f"您输入的字符长度为{len(md5)},非32位md5串，退出运行！")
        sys.exit(1)
    md5 = md5.lower()
    passwdfile_path = runpath + "dict\\"

    passwdfile_list = scan_dict(passwdfile_path)
    for passwdfile in passwdfile_list:
        #print(passwdfile)
        passwdfile = passwdfile_path + passwdfile
        ret = check_wordlist(passwdfile,md5)
        if (ret):
            sys.exit(0)
    if(not ret):
        cnt = 100
        ret = check_rand(cnt,md5)
        if (not ret):
            print("密码没有猜解出来哦。。。")
else:
    print("没有输入MD5串，退出运行！")
    sys.exit(1)
#md5 = "46f94c8de14fb36680850768ff1b7f2a"

