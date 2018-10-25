from tkinter import *
from tkinter import filedialog
import os
import shutil

from tkinter.filedialog import askopenfilename
root=Tk()

def fun():
     root.fileName = askopenfilename(filetypes=(("c++ files", "*.cpp"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
     print(root.fileName)
     print(type(root.fileName))

     pathSrc=root.fileName;
     
     #os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

     shutil.move(pathSrc, "/home/sonorous/Desktop/Tester/fileusingkinter.txt")



root.geometry("1000x1000")
topFrame=Frame(root)
topFrame.pack()

bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
menu=Menu(root)

root.config(menu=menu)

subMenu=Menu(menu)

menu.add_cascade(label="file",font="vendata 10",menu=subMenu)
subMenu.add_command(label="open project",font="vendata 10",command=fun)


editMenu=Menu(menu)
menu.add_cascade(label="config", font="vendata 10",menu=editMenu)
editMenu.add_command(label="c++",font="vendata 10")


labelHead=Label(topFrame,text="Container Testing Platform",font="vendata 30")
labelHead.grid(row=0,column=1,columnspan=2)

button1=Button(topFrame,text="open",fg="red",font="vendata 20 ", command=fun)
button2=Button(topFrame,text="compile",fg="blue",font="vendata 20")

button1.grid(row=1,column=0,columnspan=2)
button2.grid(row=1,column=2,columnspan=2)


T = Text(bottomFrame, height=50, width=150)
T.grid(row=3,columnspan=10)
T.tag_configure('bigfoo', font=('vendata', 10, 'bold'))
T.insert(END,"hello world\n la la la\n",'bigfoo')

file=open('/home/sonorous/Desktop/Tester/fileusingkinter.txt','r')

fileData=file.read()
fileData=str(fileData)
print(fileData)
T.insert(END,fileData,'bigfoo')


root.mainloop()
