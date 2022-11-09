# Write a Python program to find all such numbers which are divisible by 7 but are not a 
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed on 
# screenone after other separated by _.
# for i in range(2000,3200):
#     if i%7==0 and i%5!=0:
#         print(i, end="_")

# Write a Python program to accept the user's first and last name and then print them in the 
# reverse order with a space between first name and last name.
# fname = input("Enter first name:")
# lname = input("Enter last name")
# fullname = fname+lname
# print(fullname)
# str=""
# str2=""
# for i in fname:
#     str=i+str
# for j in lname:
#     str2=j+str2
# print(str2)
# fullreverse= str2+str
# print(fullreverse)

# Accept number from user and print all prime numbers between 1 and given number.
# n = int(input("Enter a number: "))
# if n>0:
#     flag=1
#     for x in range(2,n+1):
#         flag=1
#         for i in range(2,x):
#             if x%i==0:
#                 flag=0
#                 break
#         if flag==1:
#             print(x)
# else:
#     print("Number is negative")

# Write a program to print the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# n=int(input("Enter height: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ", end="")
#     print("\r")
# for i in range(n,0,-1):
#     for j in range(0,i-1):
#         print("* ",end="")
#     print("\r")

# Salary structure of a company for various categories of employees is as follows:For
# class I employees, basic salary is 25K. Home Rent Allowance and Dearness Allowance is 30% and 121% 
# of basic salary. For class II employees, basic salary is 20K. Home Rent Allowance(HRA)and Dearness 
# Allowance(DA)is 25% and 121% of basic salary. For class III employees, basic salary is 15K and Home 
# Rent Allowance and Dearness Allowance is 20% and 121% of basic salary.Total salary is calculated as 
# basic + HRA +DA. Working experience of employee is considered whilegiving hike in salary. If class I 
# employee has more than 10 yrs of experience, his/her salary will be increased by 5K in basic. 
# However, if class II employee has more than 10 years of experience, he can get hike of 3000/-
# in basic. For class III employee,having more than 5 years of experience, he can get hike of 2000/-in 
# basic. Write a python program to calculate salary of an employee when its class and experience is 
# givenby user. (use if-elif conditional statements)

# emp_class = int(input("Enter class of employee: "))
# emp_exp = int(input("Enter employee experience: "))
# if emp_class==1:
#     bas_sal= 25000
#     if emp_exp>=10:
#         bas_sal+=5000
#     hra = bas_sal*30/100
#     da = bas_sal*121/100
# elif emp_class==2:
#     bas_sal= 20000
#     if emp_exp>=10:
#         bas_sal+=3000
#     hra = bas_sal*30/100
#     da = bas_sal*121/100
# elif emp_class==3:
#     bas_sal= 20000
#     if emp_exp>=5:
#         bas_sal+=2000
#     hra = bas_sal*30/100
#     da = bas_sal*121/100
# total_sal = bas_sal + hra + da
# print(total_sal)

# Write a python program to accept two numbers ‘m’ and ‘n’ from user. Print square of each 
# odd number from m ton. Whenever the number is multiple of 3,skip it and whenever a number is multiple 
# of 7 end the program.
m = int(input("Enter a number: "))
n = int(input("Enter a number: "))
if m<n:
    for x in range(m,n+1):
        if x%2!=0 and x%7!=0:
            if x%3==0:
                continue
            print(x**2)
else:
    print("The first number should be smaller.")

