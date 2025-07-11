from tkinter import *


root = Tk()
root.title("Calculator")
root.resizable(False,False)



entry=Entry(root,width=25,borderwidth=5,font=('Arial',20))
entry.grid(row=0,column=0,columnspan=4,padx=11,pady=10,ipady=10)



def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,END)
        entry.insert(0,result)
    except:
        entry.delete(0,END)
        entry.insert(0,"Error")



def clear():
    entry.delete(0, END)




def click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current)+str(number))




b1= Button(root,text="1", padx=40,pady=20,font=('Arial',13),  command=lambda: click(1))
b2= Button(root,text="2", padx=40,pady=20,font=('Arial',13),command=lambda: click(2))
b3= Button(root,text="3", padx=40,pady=20,font=('Arial',13),command=lambda: click(3))
div= Button(root,text=" / ",padx=40,pady=20,font=('Arial',13),command=lambda:click("/"))

b4= Button(root,text="4", padx=40,pady=20,font=('Arial',13),command=lambda: click(4))
b5= Button(root,text="5", padx=40,pady=20,font=('Arial',13),command=lambda: click(5))
b6= Button(root,text="6", padx=40,pady=20,font=('Arial',13),command=lambda: click(6))
mul= Button(root,text=" * ",padx=40,pady=20,font=('Arial',13),command=lambda:click("*"))

b7= Button(root,text="7", padx=40,pady=20,font=('Arial',13),command=lambda: click(7))
b8= Button(root,text="8", padx=40,pady=20,font=('Arial',13),command=lambda: click(8))
b9= Button(root,text="9", padx=40,pady=20,font=('Arial',13),command=lambda: click(9))
sub= Button(root,text=" - ",padx=40,pady=20,font=('Arial',13),command=lambda:click("-"))

b0= Button(root,text="0", padx=40,pady=20,font=('Arial',13),command=lambda: click(0))
clear_b = Button(root,text="DEl ",padx=29,font=('Arial',13),pady=20,command=clear)
equal = Button(root,text="=",padx=40,pady=20,font=('Arial',13),command=calculate)
add= Button(root,text="+ ",padx=40,pady=20,font=('Arial',13),command=lambda:click("+"))




b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)


add.grid(row=1, column=3)
sub.grid(row=2, column=3)
mul.grid(row=3, column=3)
div.grid(row=4, column=3)


equal.grid(row=4,column=2)
clear_b.grid(row=4,column=1)




root.mainloop()