# package hehehe
weight = input("what is the weight of your package: ")

try:
    weight = float(weight)
except:
    print("thanks for playing")
    quit()


# you might be able to use a case statement... it looks like you don't need to worry
# about puuting in weight > 2 and weight <= 6 the first if statement takes care of that part
if weight <= 2:
    print("your charge is $1.50")
elif weight <= 6:
    print("your charge is $3")
elif weight <= 10:
    print("your charge is $4")
# presumably there should be some upper wieight limit
else:
    print("your charge is $4.75")

# print(weight)
