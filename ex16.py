from sys import argv
# 需要看视频看作者是如何break the code 
#创建一个test.txt 文件，往里面写东西。就可以看出来问题。

script, filename = argv
print(">>>> this is argv", repr(argv))
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye！") #比较适合直接录视频演示。

target.truncate()
