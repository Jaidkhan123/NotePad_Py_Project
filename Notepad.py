from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled- RPS Notepad")
    file=None
    textarea.delete(1.0,END)    # 1 line 0 character se last tk
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files", "*.*"),
                         ("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "- RPS Notepad")
        textarea.delete(1.0, END)
        f= open(file,"r")
        textarea.insert(1.0, f.read())
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',
                               defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),
                                          ("Text Documents", "*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"- RPS Notepad")
            print("filesaved")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

def quitapp():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("RPS NotePad","NotePad made by Mohammad Jaid\nBtech Cse 5th Sem\nRPS college of Engineering and Technology")

root=Tk()
root.title("RPS notepad")
root.geometry("900x450")

# root.wm_iconbitmap("10.ico")

textarea= Text(root, font="lucida 13")
file=None
textarea.pack(expand=TRUE, fill=BOTH)

# Lets make a menu bar
menubar = Menu(root)
filemenu=Menu(menubar, tearoff=0)

# to open new file

filemenu.add_command(label="new", command=newfile, font="lucida 10")

#to open already existing file
filemenu.add_command(label="open", command=openfile, font="lucida 10")

# to save the current file
filemenu.add_command(label="Save", command= savefile, font="lucida 10")
filemenu.add_command(label="Exit", command=quitapp, font="lucida 10")

filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu, font="lucida 10")

# edit menu starts
editmenu=Menu(menubar, tearoff=0)
editmenu.add_command(label="cut", command=cut, font="lucida 10")
editmenu.add_command(label="copy", command=copy, font="lucida 10")
editmenu.add_command(label="paste", command=paste, font="lucida 10")


menubar.add_cascade(label="Edit", menu=editmenu, font="lucida 10")

#Help menu start
helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="About notepad", command=about, font="lucida 10")

menubar.add_cascade(label="Help", menu=helpmenu, font="lucida 10")


root.config(menu=menubar)

scrollbar=Scrollbar(textarea)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=scrollbar.set)

root.mainloop()