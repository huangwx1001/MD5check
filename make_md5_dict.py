# !/usr/bin/python3
#-*-coding:utf-8-*-

import hashlib
import os

runpath = os.path.dirname(os.path.realpath(__file__)) + "\\"
def get_md5(str):
    str_md5 = hashlib.md5(str.encode('utf-8')).hexdigest()
    return str_md5

fg = open(runpath + 'md5_result.txt','w')
with open(runpath + 'rockyou.txt','r',encoding='utf-8') as fr:
    a = 2461910
    for line in fr.readlines()[a:]:
        print(f'{line.strip()}    :    {a}')
        a += 1
        restule_md5 = get_md5(line)
        content = restule_md5 + "|" + line + "\n"
        fg.write(content)
fr.close()
fg.close()
print("done")
