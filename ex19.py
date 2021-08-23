#Exercise 19. Functions and Variables
# def 函数特别好用，避免出现重复的代码。这里定义了cheese_and_crackers之后，line 10 之后可以直接套用，直接出现4个print

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes_of_crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 800)
