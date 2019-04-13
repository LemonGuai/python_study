from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")


# 打开输入的文件名的文件
current_file = open(input_file)

print("first let's print the whole file:\n")
# 读取文件内所有内容并输出
print_all(current_file)

print("now let's rewind, kind of like a tape.")
# 指针回到文件开头
rewind(current_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)