# Exercise 38. Doing Things to Lists
# 北京时间2021年8月21日  周六00:48 明天爬山准备睡了

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
print(">>> ", stuff) # 这里我们可以看到stuff的输出结果是['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop()函数默认移除列表的一个元素，默认最后一个元素，并且返回该元素的值。
    print("Adding: ", next_one) # 最后一个元素是boy，赋值给next_one
    stuff.append(next_one) 
    print(">>> ", repr(stuff)) # 这里用append函数，把next_one 加到stuff这个list，输出结果为['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy']
    print(f"There are {len(stuff)} items now.")
    
print("There we go: ", stuff)    

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! Fancy 其中list[-1],表示list的最后一个元素
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!

