#IMPORTS

from tkinter import *
import functools as ft
app = Tk()

app.title("Calculator")

#FUNCTIONS


#Error checks the character being inputted to ensure equations remain logical
def number_input(num):
    if len(math["text"]) > 0:
        #if the current inputs length is bigger than 0, it identifies double operators and deletes them
        if math["text"][-1] in ["+","*","//"] and num in ["+","*","//"]:
            return
        else:
            #Checks for any number after a 0 after an operator
            if num == "0" and math["text"][-1] in ["+","-","*","//"]:
                return
            else:
                math["text"]= math["text"] + num
    #if the current inputs length is less than 0, it checks for starting equations with 0s or operators        
    elif num not in ["+","*","//"]:
        if num != "0":
            math["text"]= math["text"] + num
            answer["text"] = answer["text"][:-999]



def clear_func(amount):
    #clears the function by 1 or max depending on button pressed
    math["text"]= math["text"][:-(amount)]
    if amount == 999:
        answer["text"]=answer["text"][:-(amount)]



def calculate():
    #calculates the number
    try:
        #turns equation into int to solve, then back into string
        answer["text"] = str(eval(math["text"]))
        #doesnt send the answer back into the equation if it is equal to 0 
        if answer["text"] != "0":
            math["text"] = answer["text"]
        else:
            math["text"]= math["text"][:-(999)]
    except:
        pass




#The code that creates all of the buttons and windows
app.configure(bg="#9cf7ca")
math = Label(app,text="",width=12, bg = "#9cf7ca")
answer = Label(app,text="",width=5,bg = "#9cf7ca")
one=Button(app,text="1",relief=RIDGE,bd=5,command=ft.partial(number_input,"1"),width = 5,bg = "cyan")
two=Button(app,text="2",relief=RIDGE,bd=5,command=ft.partial(number_input,"2"),width = 5,bg = "cyan")
three=Button(app,text="3",relief=RIDGE,bd=5,command=ft.partial(number_input,"3"),width = 5,bg = "cyan")
four=Button(app,text="4",relief=RIDGE,bd=5,command=ft.partial(number_input,"4"),width = 5,bg = "cyan")
five=Button(app,text="5",relief=RIDGE,bd=5,command=ft.partial(number_input,"5"),width = 5,bg = "cyan")
six=Button(app,text="6",relief=RIDGE,bd=5,command=ft.partial(number_input,"6"),width = 5,bg = "cyan")
seven=Button(app,text="7",relief=RIDGE,bd=5,command=ft.partial(number_input,"7"),width = 5,bg = "cyan")
eight=Button(app,text="8",relief=RIDGE,bd=5,command=ft.partial(number_input,"8"),width = 5,bg = "cyan")
nine=Button(app,text="9",relief=RIDGE,bd=5,command=ft.partial(number_input,"9"),width = 5,bg = "cyan")
zero=Button(app,text="0",relief=RIDGE,bd=5,command=ft.partial(number_input,"0"),width = 20,bg = "cyan")
plus = Button(app,text="+",relief=RIDGE,bd=5,command=ft.partial(number_input,"+"),width = 5,bg = "cyan")
minus = Button(app,text="-",relief=RIDGE,bd=5,command=ft.partial(number_input,"-"),width = 5,bg = "cyan")
multiply = Button(app,text="x",relief=RIDGE,bd=5,command=ft.partial(number_input,"*"),width = 5,bg = "cyan")
divide = Button(app,text="//",relief=RIDGE,bd=5,command=ft.partial(number_input,"//"),width = 5,bg = "cyan")
clear = Button(app,text="C",relief=RIDGE,bd=5,command=ft.partial(clear_func,1),width = 5,bg = "cyan")
clearall = Button(app,text="CE",relief=RIDGE,bd=5,command=ft.partial(clear_func,999),width = 5,bg = "cyan")
equal = Button(app,text="=",relief=RIDGE,bd=5,command=calculate,width= 5,height=3,bg = "cyan")



#The code that formats the buttons onto the window
math.grid(row=0,column=0,columnspan=3)
answer.grid(row=0,column=3,columnspan=4)
one.grid(row=1,column=0)
two.grid(row=1,column=1)
three.grid(row=1,column=2)
four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)
seven.grid(row=3,column=0)
eight.grid(row=3,column=1)
nine.grid(row=3,column=2)
zero.grid(row=4,column=0,columnspan=3)
plus.grid(row=1,column=3)
minus.grid(row=2,column=3)
multiply.grid(row=3,column=3)
divide.grid(row=4,column=3)
clear.grid(row=1,column=4)
clearall.grid(row=2,column=4)
equal.grid(row=3,column=4,rowspan=4)

app.mainloop()
