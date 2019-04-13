from sys import argv

script, filename = argv     # 获取用户输入

txt = open(filename)        # 打开一个以filename参数中存放的值为文件名的文件,并赋给txt

print(f"here's your file {filename}:")  # 提示这是打开的file名
print(txt.read())                       # 读取file中的全部内容,并输出

# print("type the filename again:")       # 提示重新输入文件名
# file_again = input(">")                 #提示符,标出文件名

# txt_again = open(file_again)            #再次打开file

# print(txt_again.read())                 #再次读取file中的全部内容,并输出