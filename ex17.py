from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"copying from {from_file} to {to_file}") #提示要进行的操作

# we could do these two on one line, how?
in_file = open(from_file)    #打开原文件
indata = in_file.read()     #将原文件中的数据提取

print(f"the input file is {len(indata)} bytes long")    #提示原文件的数据长度

print(f"does the output file exist?{exists(to_file)}")   #判断新文件是否存在,并提示
print("ready, hit RETURN to continue, CTRL-C to abort") #确定操作
input()                                                 #选择操作

out_file = open(to_file, 'w')                         #打开新文件,并选择读写操作
out_file.write(indata)                                #将原文件数据导入新文件

print("alright, all done")                            #提示操作完成

out_file.close()                                      #关闭打开的文件
in_file.close()