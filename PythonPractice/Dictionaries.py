myDictionary = {'index1' : 1, 'index2': 2, 'index3': 355} #create dictionary
print(myDictionary)
print(myDictionary['index2'])


#create dictionary w/in dictionary
dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'},
'em_1235': {'fname': 'Mary', 'lname': 'Jones', 'phone': '154-135-4357'} }
print(dic_users['em_1235'])
print(dic_users['em_1235']['phone'])
print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'], dic_users['em_1235']['phone']))
#using format to adjust print script


dic_cats = {
    'Cat1' : 'Charlie',
    'Cat2' : 'Cheeto',
    'Cat3' : 'Marley'
    }
print(dic_cats)
x = dic_cats.get("Cat1")  #use get method to call value of key
print(x)

dic_cats['Cat3'] = 'Jack'  #change value of key
print(dic_cats)
dic_cats['Cat4'] = 'Marley'  #add new key value pair
print(dic_cats)


myPets = {  #create nested dictionary
    "Pet1" : {
        "name" : "Charlie",
         "age" : "5 years",
        "type" : "cat"
        },
    "Pet2" : {
        "name" : "Cheeto",
         "age" : "1 year",
        "type" : "cat"
        },
    "Pet3" : {
        "name" : "Luna",
         "age" : "3 months",
        "type" : "dog"
        }
    }

print(myPets['Pet1'])
print("Pet number 1: {}\nAge: {}\nType: {}".format(myPets['Pet1']['name'], myPets['Pet1']['age'], myPets['Pet1']['type']))


x = ('key1', 'key2', 'key3')
y = 0

newDict = dict.fromkeys(x,y)  #create dictionary using fromkeys()
print(newDict)


