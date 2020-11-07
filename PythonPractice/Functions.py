
#-----------Creating function with loops---------------
mySentence = 'I love the color'

color_list = ['yellow','blue','green','red','teal']

def color_function():
    for i in color_list:
        print("{} {}!".format(mySentence,i))


color_function()


#---------------Function with parameter------------------
string = "loves the color"

color_list = ['yellow','blue','green','red','teal']

def color_function2(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name,string,i)
        lst.append(msg)   #set up list so returns array to program
    return lst

def get_name():
    go = True
    while go:  #while go is true - execute loop
        name = input('What is your name? ')
        if name == '':
            print('You need to provide your name!')
        elif name == 'Sally':
            print('Sally, you may not use this software.')
        else:
            go = False #stops loop
    lst = color_function2(name)
    for i in lst:   #set up iteration loop so each element of list is printed
        print(i)


get_name()




#---------------Function self practice-------------------
txt = "is the name of your pet"

def pet_name():
    go = True
    while go:
        p_name = input('What is your pet\'s name?')
        if p_name == '':
            print('Please enter a name!')
        elif p_name == 'Luna':
            print('MY pet\'s name is also Luna!')
            go = False
        else:
            go = False
            print('{} {}'.format(p_name,txt))

pet_name()




#-------------------Lambda function--------------------------
x = lambda y: (y+2)/17*12
print(x(13)) #calls lambda function x with argument 13


#------- format function ----------------
print('binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}'.format(8))




