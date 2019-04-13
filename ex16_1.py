from sys import argv

script, file_name = argv

file = open(file_name)

print(f"here's your file {file_name}.")
print(file.read())

print('请再输入您的文件名：')
file_name_2 = input('>')

file = open(file_name_2)
print(file.read())