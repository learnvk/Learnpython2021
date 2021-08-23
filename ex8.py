formatter = "{} {} {} {} "

print(formatter.format(1,2,3,4)) #这个很好理解，就是把1，2，3，4这4个数的值赋给了{} {} {} {}。
#只要明白了ex7.py 那么这个也是很好理解。
print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))