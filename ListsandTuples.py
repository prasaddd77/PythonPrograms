
# 1) Write a python program to create a list where number of elements are taken 
# from user. Further add even numbers from list and odd numbers from list. These two sum values 
# should be returned as a tuple.
# l=[]
# n = int(input("How many elements in the list?: "))
# sum=0
# add=0
# for i in range(n):
#     x=int(input("Enter the elements: "))
#     l.append(x)
# for i in l:
#     if i%2==0:
#         sum+=i
#     elif i%2!=0:
#         add+=i
# t = (sum,add)
# print("The sums of even and odd elements in the list are:", t)


# 2) Given two lists: one containing song name and other containing number 
# of downloads, display the songs that are most popular to least popular. Output should be in the 
# format:“Song_name: downloaded number_of_times”
# song = ["Blinding Lights", "As It Was", "Out of Time", "Light Switch", "No Time To Die"]
# downloads = [290,350,500,150,300]
# tuplelist=[]
# i=0
# for j in range(5):
#     tuplelist.append((downloads[i], song[j]))
#     i=i+1
# for i in range(len(tuplelist)):
#     for j in range(len(tuplelist)-i-1):
#         if tuplelist[j][0] < tuplelist[j+1][0]:
#             temp = tuplelist[j]
#             tuplelist[j] = tuplelist[j+1]
#             tuplelist[j+1] = temp
# for i in tuplelist:
#     print(i[1]+":"+str(i[0]))

# 3) For a given list a = ['abc', 'xyz', 'aba', '1221','bhgsskknb','aa', ‘program'], write a 
# program to count the number of strings where the string length is two or more and the first and 
# last character are same from a given list of strings
# a = ['abc', 'xyz', 'aba', '1221','bhgsskknb','aa', 'program']
# print(a)
# strcount=0
# for i in a:
#     x=i[0]
#     if(i.endswith(x) and (len(i))>= 2):
#         strcount+=1
# print('''The number of strings where the string length is two or more 
#          and the first and last character are same is:''', strcount)


# 4) Write a python program to print tuple of website suffixes (e.g. (com, edu, net, in) 
# from given list ["www.yahoo.com", "www.tsec.edu", "www.asp.net", "www.abcd.in"]
# sites= ["www.yahoo.com", "www.tsec.edu", "www.asp.net", "www.abcd.in"]
# webtuple=()
# for i in sites: 
#     x=i.find(".",i.find(".")+1)
#     newtuple=(i[x+1:],)
#     webtuple+=newtuple
# print("Website Suffixes are:", webtuple)

# 5) : Given the lists list1=['x','y','z']list2=[2,3,4,5,6,7,8]list3=[1,2,3]Write List 
# comprehensions to produce the following Lists a.['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 
# 'zz', 'zzz', 'zzzz'] b.['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] c.[[2], [3], [4], 
# [3], [4], [5], [4], [5], [6]] d.[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] e.[(1, 1), (2, 1), (3, 1), 
# (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

list1=['x','y','z']
list2=[2,3,4,5,6,7,8]
list3=[1,2,3]
print("\nList 1", list1, "--Following are the list comprehension products from list--")
listcomp1 = [l*i for l in list1 for i in range(1,5)]
print("(1) ", listcomp1)

listcomp2 = [l*i for i in range(1,5) for l in list1]
print("(2) ", listcomp2)

print("\nList 2", list2, "--Following are the list comprehension products from list--")
listcomp3 = [[list2[i]+j] for i in range(3) for j in range(3) ]
print("(3) ", listcomp3)

listcomp4 = [[list2[i]+j for i in range(4)] for j in range(4)]
print("(4) ", listcomp4)

print("\nList 3", list3, "--Following are the list comprehension products from list--")
listcomp5 = [(y,x) for x in list3 for y in list3]
print("(5) ", listcomp5)



