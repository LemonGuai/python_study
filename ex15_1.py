print('请输入您要打开的文件名:')

file_name = input('>')
file = open(file_name)
print(file.read())

file.close()
