
num1 = 12
key = False

if num1 == 12:
    if key:  #nested if statement
        print('Num1 is equal to Twelve and they have the key!')
    else:
        print('num1 is equal to twelve and they do NOT have the key!')
elif num1 < 12:  #for else if
    print('Num1 is less than Twelve!')
else:
    print('Num1 is NOT equal to Twelve!')

    
a = 6
b = 7
c = True

if a == 6:
    if c:
        print('A is equal to 6 and c is true.')
    else: print('A is equal to 6 but c is not true!')
elif a < 6:
    print('A is less than 6.')
else:
    print('A is not equal to 6!')


print(bool(a))  #evaluates any value, most are True. any string is true except if it is empty.
                #any number is true unless 0


x = 3
print(isinstance(x, str))  #isinstance() determines if an object is a certain data type. Returns a boolean value
print(isinstance(x, int))
