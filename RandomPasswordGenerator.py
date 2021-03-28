import random

allLowerCase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
allUpperCase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
allNumbers = [0,1,2,3,4,5,6,7,8,9]
allSymbols = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","[","]","\\","|",",",":",";","?","/",">",".","<","`","~","\"","}"," "]


def createRandomPass():
    gennum = input("Please enter the number of characters for your password: ")
    randpass = random.sample(allLowerCase + allUpperCase + allNumbers + allSymbols, int(gennum))
    randpassstrings = [str(x) for x in randpass]
    l = ''.join(randpassstrings)
    print(l)

createRandomPass()
