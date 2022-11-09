from tkinter import*
# def iCalc(source,side):
#     storeObj = Frame(source,borderwidth=4,bd=4,bg="powder blue")
#     storeObj.pack(side=side,expand=YES,fill=BOTH)
#     return storeObj
# def button(source,side,text,command=None):
#     storeObj = Button(source,text=text,command=command)
#     storeObj.pack(side=side,expand=YES,fill=BOTH)
#     return storeObj
# class app(Frame):
#     def __init__(self):
#         Frame.__init__(self)
#         self.option_add('*Font','arial 20 bold')
#         self.pack(expand=YES,fill=BOTH)
#         self.master.title('Calculator')

#         display = StringVar()
#         Entry(self,relief=RIDGE,textvariable=display,
#         justify='right'
#         ,bd=30,bg="powder blue").pack(side=TOP,expand=YES,fill=BOTH)
        
#         for clearButton in (["C"]):
#             erase = iCalc(self,TOP)
#             for ichar in clearButton:
#                 button(erase, LEFT, ichar, lambda
#                         storeObj=display, q=ichar:storeObj.set(''))
#         for numButton in ("789/", "456", "123-", "0.+"):
#             FunctionNum = iCalc(self,TOP)
#             for iEquals in numButton:
#                 button(FunctionNum,LEFT,iEquals,lambda
#                 storeObj=display,q=iEquals:storeObj.set(storeObj.get() + q))
#         EqualButton = iCalc(self,TOP)
#         for iEquals in "=":
#             if iEquals == "=":
#                 btniEquals = button(EqualButton, LEFT, iEquals)
#                 btniEquals.bind('<ButtonRelease-1>',lambda e, s=self, 
#                                 storeObj=display:s.calc(storeObj),'+')
#             else:
#                 btniEquals = button(EqualButton, LEFT, iEquals,
#                                     lambda storeObj=display,s='%s'% iEquals:storeObj.set
#                                     (storeObj.get()+s))
#     def calc(self, display):
#         try:
#             display.set(eval(display.get()))
#         except:
#             display.set("ERROR")
# if __name__ == '__main__':
#     app().mainloop()

# root = Tk()
# root.geometry("300x300+300+100")
# root.title("Practical")

# def welcome():
#     name = input.get()
#     welcome_message.config(text=f"Welcome, {name}")
#     pass

# name_label = Label(text="Enter a Name: ", font=("Arial", 14, "bold"))
# name_label.pack()

# input = Entry(font=("Arial", 20, "bold"))
# input.pack()

# button = Button(text="Click Me", command=welcome)
# button.pack()

# welcome_message = Label(text="", font=("Arial", 24, "bold"))
# welcome_message.pack()

# root.mainloop()



root = Tk()
root.geometry("300x300+300+100")
root.title("Pass Or Fail")

def validate_marks():
    message = ""
    percent = int(input1.get())
    if percent >= 75:
        message = "Pass"
    else: 
        message = "Fail"

    label2.config(text=message)
    
    
label1 = Label(text="Enter your Percentage: ", font=("Arial", 20))
label1.pack()

input1 = Entry(font=("Arial", 20, "bold"))
input1.pack()

button = Button(text="Validate", font=("Arial", 20), command=validate_marks)
button.pack()

label2 = Label(text="", font=("Arial", 20, "bold"))
label2.pack()

root.mainloop()
                