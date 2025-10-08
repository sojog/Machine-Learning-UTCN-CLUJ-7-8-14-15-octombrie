price = {"apples":10, "milk": 12,"bread": 5}
my_list=[("apples",2),("milk",2)]

print(sum ( price[item]*quantity for item, quantity in my_list) )


print(sum([10, 20, 30]))