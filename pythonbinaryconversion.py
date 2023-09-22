import math

def decimalToBinary(n):
    return "{0:b}".format(int(n))
   
dTb = int(input("What is your number?"))


dTb = str(dTb)
print("The Binary of " + dTb + " is:")
dTb = int(dTb)
print(decimalToBinary(dTb))