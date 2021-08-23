print("Mary had a little lamb. ")
print("Its fleece was white as {}." .format('snow')) # str.format(),format()括号里的值会直接赋给curly braces{}

print("And everywhere that Mary went. ")
print("." * 10)# this will print ten dot

end1 = "C"#把string c 直接赋给end1
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 +end3 + end4+ end5 + end6, end=' ')#这个逗号不能移除，否则会出现SyntaxError: invalid syntax。end=' '，引号需打一个空格键，否则cheese和burger会连在一起。
print(end7 + end8 +end9 + end10+ end11 + end12)