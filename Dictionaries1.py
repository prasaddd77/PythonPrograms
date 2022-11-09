# 1) Give two list named as students and their marks. 
# Create a dictionary which will contain student name as key and marks as its value
# student = ["Prasad", "Yash", "Nahush", "Mokshit", "Archit"]
# marks = [100,88,94,96,95]
# dict = {}
# dict[student[0]] = marks[0]
# dict[student[1]] = marks[1]
# dict[student[2]] = marks[2]
# dict[student[3]] = marks[3]
# dict[student[4]] = marks[4]
# print(dict)

# 2) Create a dictionary for employee record. Each employee record stores empno, ename,
#  number of hours worker as an overtime for a week. If total number of overtime hours are 10 or 
# more, add overtime salary of 500 Rs per hour for that employee in his record otherwise if the 
# overtime hours are less than 10, then add overtime salary of 250 Rs per hour for that employee 
# in his record. If no overtime is done then no overtime salary is paid.

# emp1 = {"empno":77,"ename":"Prasad Ranjane","noofhours":8,"Salary":1000}
# if emp1["noofhours"] >=10:
#     for i in range(10, emp1["noofhours"]+1):
#         emp1["Salary"]+=500
#     print("The incremented salary of the employee is:", emp1["Salary"])
# elif emp1["noofhours"] < 10 and emp1["noofhours"] > 0:
#     emp1["Salary"]+=250
#     print("The incremented salary of the employee is:", emp1["Salary"])
# elif emp1["noofhours"] == 0:
#         print("Overtime hours are zero. No extra salary added.")


x = (1,1,2,3,2,4,5,4,6,7,10)
print(type(x))
y=tuple(set(x))
d={}
print(y)
for i in y:
    d.update({i:x.count(i)})
print(d)


