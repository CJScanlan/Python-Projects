
i = 0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1
    
i = 0
while i < 10:
    print('{} iteration through the loop.'.format(i))
    i += 1
#setting increment is important for while loops, otherwise keeps running



#---------------self practice while loops ----------------------
a = 10
while a > 0:
    print('{} seconds to lift off!'.format(a))
    if a == 5:
        break  #using break statement to stop iteration at 5
    a -= 1

b = 6
while b > 0:
    b -= 1
    if b == 2:
        continue   #using continue statement, iteration does not include 2
    print('{} mississippi'.format(b))

c = 1
while c <= 15:
    print('{} one-thousand'.format(c))
    c += 1
else:    #use else statement within while loop
    print('That\'s all folks!')

#--------------self practice for loops--------------------------
i = 0
for i in range(5): #set range for loop
    print('{} little piggies'.format(i))
    i += 1 

plants = ["spider plant", "peace lily", "devil's ivy", "fiddle-leaf fig"]
for x in plants: 
    print(x)
    if x == "devil's ivy":
        break   #set break statement, stops at x


animals = ["turtles", "cats", "spider monkeys", "pugs", "llamas"]
for x in animals:
    if x == "pugs":
        continue  #stops at x then continues with the next iteration
    print('I like {}!'.format(x))

for i in range (10):
    print(i)
else:  #using else statement within for loop
    print("Ta-da!")
