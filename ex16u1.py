from sys import argv

#创建一个test.txt 文件，往里面写东西。就可以看出来问题。

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye！") #比较适合直接录视频演示。

target.truncate() # With truncate(), you can declare how much of the file you want to remove, based on where you're currently at in the file.

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it." )
target.close()
