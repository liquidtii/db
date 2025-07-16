from tkinter import *

root = Tk()
root.title("계산기")
root.geometry("500x400")
root.resizable(False, False)

txt = Text(root,height = 2,width = 60,)
txt.pack()
txt.place(x=0,y=40)

a = Text(root,height = 2,width = 6,)
a.pack()
a.place(x=380,y=40)

a.insert(END,0)

def one():
    txt.insert(END,1)
def two():
    txt.insert(END,2)
def tre():
    txt.insert(END,3)
def x():
    txt.insert(END,"*")
def plus():
    txt.insert(END,"+")
def minu():
    txt.insert(END,"-")
def fou():
    txt.insert(END,4)
def fiv():
    txt.insert(END,5)
def six():
    txt.insert(END,6)
def ce():
    txt.delete(1.0,)
def sev():
    txt.insert(END,1)
def egt():
    txt.insert(END,1)
def nigh():
    txt.insert(END,1)
def zer():
    txt.insert(END,1)

one = Button(root, padx=25, pady=25, text="1", command=one)
one.pack()
one.place(x=0,y=100)

two = Button(root, padx=25, pady=25, text="2", command=two)
two.pack()
two.place(x=70,y=100)

tre = Button(root, padx=25, pady=25, text="3", command=tre)
tre.pack()
tre.place(x=140,y=100)

x = Button(root, padx=25, pady=25, text="X", command=x)
x.pack()
x.place(x=210,y=100)

plus = Button(root, padx=25, pady=25, text="+", command=plus)
plus.pack()
plus.place(x=280,y=100)

minu = Button(root, padx=25, pady=25, text="-", command=minu)
minu.pack()
minu.place(x=350,y=100)

fou = Button(root, padx=25, pady=25, text="4", command=fou)
fou.pack()
fou.place(x=0,y=180)#80차이좌우70차이

fiv = Button(root, padx=25, pady=25, text="5", command=fiv)
fiv.pack()
fiv.place(x=70,y=180)

six = Button(root, padx=25, pady=25, text="6", command=six)
six.pack()
six.place(x=140,y=180)

ce = Button(root, padx=25, pady=25, text="CE", command=ce)
ce.pack()
ce.place(x=210,y=180)

sev = Button(root, padx=25, pady=25, text="7", command=sev)
sev.pack()
sev.place(x=0,y=260)

egt = Button(root, padx=25, pady=25, text="8", command=egt)
egt.pack()
egt.place(x=70,y=260)

nigh = Button(root, padx=25, pady=25, text="9", command=nigh)
nigh.pack()
nigh.place(x=140,y=260)

zer = Button(root, padx=25, pady=25, text="0", command=zer)
zer.pack()
zer.place(x=210,y=260)

def func(event):
    a.replace("1.0", END, eval(txt.get(1.0, END)))
 
 
root.bind('<Return>', func)
root.mainloop()
