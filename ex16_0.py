from sys import argv

script, file_name = argv

print(f"so you want to open the file of {file_name}")
print("if you don't want to open the file,hit CTRL-C")
print("if you want to continue,hit RETURN")
input("?")
txt = open(file_name,'w')

print("let's trunsate the file!")
txt.truncate()

print("now let's input 3 lines.")
line1 = input("line1 is:")
line2 = input("line2 is:")
line3 = input("line3 is:")

print("and write the 3 lines into the txt")
txt.write("{}\n{}\n{}\n".format(line1, line2, line3))