from tkinter import *
root=Tk()
root.title('Calculator')
f1=Frame(root)
f1.pack(fill=X)
Buttons=[['1','2','3','+'],['4','5','6','-'],['7','8','9','*'],['.','0','/']]
e_s=StringVar()
e = Entry(f1,width=21,state = 'readonly',textvariable = e_s,font=(None,'15')).grid(row=0,column=0,columnspan=4)
r=1
for i in Buttons:
    c=0
    for j in i:
        a=Button(f1,text=j,width=7,command=lambda s=e_s, q=j: s.set(s.get() + q)).grid(row = r, column = c)
        c+=1    
    r+=1
eq=Button(f1,text="=",width=32,command= lambda s=e_s: s.set(eval(s.get()))).grid(row=5,column=0,columnspan=4)
clr=Button(f1,text="C",width=7,command= lambda s=e_s: s.set("")).grid(row=4,column=3)
root.mainloop()
