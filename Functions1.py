# 1) Write a function that takes a list of words and an integer n and returns the list of words
# that are longer than n 
def myListOfWords(n, listOfWords):
    words=[]
    for x in listOfWords:
        if len(x)>n:
            words.append(x)
    print(words)
    return words
myListOfWords(5,["Fish","Vegetables","Barney","Ted","Lily"])

wordLen=[]
def mapWordsToInt(x):
    
    for y in x:
        z=len(y)
        wordLen.append(z)
        return wordLen,x
x,y = mapWordsToInt(["HIMYM", "Friends", "TBBT", "B99", "The Office", "Modern Family"])
print(y,x)


def my_reduce(listOfInt):
    sum=0
    for x in listOfInt:
        sum= sum + x
    print(sum)
    return sum
my_reduce([1,2,3,4,5,6,6,7,8])

def my_reduce(listOfInt):
    total = listOfInt[0]
    for x in range(1,len(listOfInt)):
        total = total - listOfInt[x]
    print(total)
    return total
# my_reduce([1,2,3,4,5,6,6,7,8])

def stringToDict():
    str1 = input("Enter a string: ")
    print(str1)
    mydict = {
        "a" : str1.count("a"),
        "e" : str1.count("e"),
        "i" : str1.count("i"),
        "o" : str1.count("i"),
        "u" : str1.count("u"),
    }
    print(mydict)
    return mydict
stringToDict()

def my_filter(z):
    evenNum = []
    for x in z:
        if x%2==0:
            evenNum.append(x)
    return evenNum
print("Even numbers are:", my_filter([2,3,72,45,1,43,97,13,22,44]))

def my_filter(z):
    mulOf3 = []
    for x in z:
        if x%3==0:
            mulOf3.append(x)
    return mulOf3
print("Even numbers are:", my_filter([9,3,72,45,1,43,97,13,22,44]))