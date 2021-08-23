print("How old are you?", end=' ') 
#We put an end=' ' at the end of each print line. 
#This tells print to not end the line with a newline character and go to the next line.
#比如终端输出How old are you?之后，你可以直接输入数字，无需另起一行。
age = input ()

print("How tall are you?", end=' ')
height = input ()
print("How much do you weigh?", end=' ')
weight = input ()

print(f"So, you're {age} old, {height} tall and {weight} heavy" )