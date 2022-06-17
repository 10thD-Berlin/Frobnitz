import imghdr
import os
import re



def check_file(file_path):
    os.chdir(file_path)
    print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    #print(all_file)
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(check_file(file_path+'\\'+f))
            #此处check_file为发现子文件夹后重复调用
            os.chdir(file_path)
        else:
            files.append(file_path+'\\'+f)
            #生成路径+文件名
    return files

file_list = check_file(r"C:\Users\me\Desktop\111")

for data in file_list:
    a = data + "." + str(imghdr.what(data))
    os.rename(data, a)
    #print(a)
