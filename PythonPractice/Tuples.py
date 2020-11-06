animal = ('zebra', 'alligator', 'giraffe', 'goat', 'ox') #create tuple (immutable)
listofAnimals = list(animal) #create list to manipulate tuple (make mutable)
print(listofAnimals)

listofAnimals.append("honey badger") #add new animal to list using append
print(listofAnimals)

myString = "Hello there! Welcome."
newString = list(myString) #create list of string
print(newString)
newString = myString.split(" ") #split string by blank spaces
print(newString)

myList = [2,3,4] #create list
print(len(myList))

for i in myList: #i = iteration
    print(i)     #create loop


myList.append(5) #add a 5 with append

for i in myList: #i = iteration
    print(i)

myList2 = ['banana', 'apple', 'papaya', 'mango']
for i in myList2 :
    print(i)

myList2.append('orange')
print(myList2)

myList3 = myList2.copy() #make copy of list
print(myList3)

list1 = ['bob', 'matthew', 'sarah', 'ann']
list2 = [1,2,3,4]

list3 = list1 + list2 #join 2 lists
print(list3)
list3.reverse() #use reverse method to change order

print(list3)


fruits = ('mango', 'cherries', 'apples', 'bananas') #create tuple
for i in fruits: #create for loop
    print(i)

x = fruits.count('mango') #count method to return number of times item appears in tuple
print(x)


mySet = {'dog', 'cat', 'turtle'} #create set
print(mySet)
for i in mySet:
    print(i)

mySet.add('pig') #add item to set
print(mySet)

mySet.remove('turtle') #remove item from set
print(mySet)

mySet2 = {'elephant', 'pig', 'zebra'}
x = mySet.difference(mySet2) #prints item in set that are different from other set
print(x)


#create array
colors = ['blue', 'red', 'yellow', 'orange', 'purple']
print(colors)
