from script_crypting import *
from tkinter import *

check_ = False
def C():
    global check_
    check_=True
    root_.destroy()
    return check_
def D():
    global check_
    root_.destroy()
def button():
    global check_
    global results
    text_ = text.get()
    if check_:
        results = crypting(text_)
    else:
        results = decrypting(text_)
    root.destroy()
#---------------------------------------------------------------------------------------------------------------------
root_=Tk()
root_.title('Crypting')
root_.configure(bg='#252525')
root_.columnconfigure(0,weight=1)
root_.columnconfigure(1,weight=1)
root_.columnconfigure(2,weight=1)
Button(root_,text='Crypting',padx=50,pady=25,bg='#151515',highlightthickness=0,fg='#FFFFFF',command=C).grid(row=0,column=0,padx=50,pady=50)
Button(root_,text='Decrypting',padx=50,pady=25,bg='#151515',highlightthickness=0,fg='#FFFFFF',command=D).grid(row=0,column=1,padx=50,pady=50)
root_.mainloop()
#---------------------------------------------------------------------------------------------------------------------
root =Tk()
root.title('Crypting')
root.configure(bg='#252525')
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
Label(root,text="text:",bg='#252525',fg='#FFFFFF',font=('',25)).grid(row=0,column=0,padx=25,pady=25)
text = Entry(root,bg='#2C2C2E',highlightthickness=0,highlightbackground='black',fg='#FFFFFF',font=('',20))
text.grid(row=0,column=1,padx=50,pady=25)
Button(root,text='Done',padx=50,pady=25,bg='#151515',highlightthickness=0,fg='#FFFFFF',command=button).grid(row=1,column=1,padx=50,pady=50)
root.mainloop()
#--------------------------------------------------------------------------------------------------------------------
root__= Tk()
root__.configure(bg='#252525')
root__.title('Results')
Label(root__,text=results,font=('',25),fg='#FFFFFF',bg='#252525').pack(padx=50,pady=50)
root__.mainloop()
print(results)