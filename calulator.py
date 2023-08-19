from tkinter import *
import ast
root=Tk()

#add numbers to the entry widget
i=0
def get_number(num):
   global i
   display.insert(i,num)
   i+=1

def get_operations(operators):
    global i
    display.insert(i,operators)
    i+=len(operators)

def clear_all():
    display.delete(0,END)

def calculate():
    entire_string=display.get()
    '''Pass the string from display widget to AST(Abstract Syntax tree) module, 
    this module have methods to which we can pass all type of expressions'''
    try:
        node=ast.parse(entire_string,mode="eval")
        result=eval(compile(node,'<string>','eval'))
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"")

display=Entry(root)
display.grid(row=1,columnspan=6)

'''Creating 10 buttons for number 0-9
for 1-9 we are creating using for loop and for 0 we are separately creating outside loop
'''
numbers=[1,2,3,4,5,6,7,8,9]
counter=0
for x in range(3):
    for y in range(3):
        button_text=numbers[counter]
        button=Button(root,text=button_text,width=3,height=2,command=lambda text=button_text: get_number(text))
        button.grid(row=x+2,column=y)
        counter += 1
button=Button(root,text="0",width=3,height=2,command=lambda text=0: get_number(text))
button.grid(row=5,column=1)

'''
Creating oprators
Crate a list with all the operators on the calculator 
Loop through the list to create button for each calculator
'''
operations=['+','-','*','/','*3.14','%','(','**',')','**2']
count=0
for x in range(4):
    for y in range(3):
        #we only want to make 10 buttons since there are 10 operations
        if count<len(operations):
            button=Button(root,text=operations[count],width=3,height=2,command=lambda text=operations[count]:get_operations(text))
            button.grid(row=x+2,column=y+3)
            count+=1

'''creating all clear button
creating = button
Delete button
'''
Button(root,text='AC',width=3,height=2,command=clear_all).grid(row=5,column=0)
Button(root,text='=',width=3,height=2,command=calculate).grid(row=5,column=2)
Button(root,text='<-',width=3,height=2,command=lambda :undo()).grid(row=5,column=4)

root.mainloop()