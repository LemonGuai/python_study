from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")                #提示对所属入的文件名的文件进行数据清除操作
print("if you don't want that, hit CTRL-C(^C).")
print("if you do want that, hit RETURN.")

input("?")

print("opening the file...")
target = open(filename,'w')                              #打开文件,并进行读写操作

print("truncating the file. Goodbye!")      
target.truncate()           #删除文件内容

print("now i'm going to ask you for three lines")
#输入要重新写入文件的内容
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("i'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write('{0}\n{1}\n{2}\n'.format(line1, line2, line3))  #将输入的内容写入文件

print("and finally, we close it.")
target.close() #关闭文件
