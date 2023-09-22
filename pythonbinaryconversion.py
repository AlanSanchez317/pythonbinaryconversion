import math

#Alan's work
def decimalToBinary(n):#Made a function for decimal to Binary
    return "{0:b}".format(int(n)) #This specifies that it comes out as binary
   
number = int(input("What is your number?")) #Asks the user what the number is


dTb = str(number) #Turns the number into a string to work in a sentence
print("The Binary of " + dTb + " is:") #Output sentence #1
dTb = int(dTb) #Turns string back into number
print(decimalToBinary(dTb)) #Output sentence #2

#Noelle's Work

hexadecimal = hex(number) #Uses the built in Hex function
print("Here is your hexidecimal:") #Output sentence
print(hexadecimal) #prints out the hexadecimal