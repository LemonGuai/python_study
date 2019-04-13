from sys import argv
from os.path import exists
script, from_file, to_file = argv

print('您的源文件名为:{from.file}')
if exists(to_file):
    print('您的新文件存在,继续操作请输入回车')
else:
    print('您的新文件不存在,请新建文件')
input()

copy_file = open(from_file)
copy_txt = copy_file.read()

target_file = open(to_file, 'w')
target_file.write(copy_txt)

copy_file.close()
target_file.close()