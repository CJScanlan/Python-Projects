num1 = 6**9 #arithmetic operator
print(num1)

x = 7
x*= 3 #assignment operator
print(x)


y = 8
print(x != y) #comparison operator

print(x<=7 and y<=20) #logical operator (and)
print(x<8 or y>10) #logical operator (or)
print(not(x<=21 and y<=8)) #logical operator (not)

z = "mango"
w = "papaya"
t = z
print(z is t) #identity operator (is)
print(w is not t) #identity operator (is not)


join = z +" " + w
print(join)
print("mango" in join) #membership operator (in)
print("apple" not in join) #membership operator (not in)
      
a = 1
b = 2
c = 0
c = a | b
print("line 1 - value of c is ", c)
