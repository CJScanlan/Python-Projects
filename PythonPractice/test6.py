

def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2



def compute():
    go = True
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            go = False
        except ValueError as e:
            print("{}:  \n\nYou did not provide a numeric value!".format(e))
        except:
            print("\n\nOops, you provided invalid input, program will close now!")
    print("{} + {} = {}".format(var1,var2,var3))


    


if __name__ == "__main__":
    compute()



def values():
    x = input("Please enter the first numeric value: \n")
    y = input("Please enter the second numeric value: \n")
    return x,y

def addSum():
    x,y = values() #calls value function to collect inputs
    try:
        sum = int(x) + int(y)
        print("{} + {} = {}.\n".format(x,y,sum))
    except:
        print("You did not enter a numeric value.")
    finally:
        print("Continue with the program.")


addSum()
