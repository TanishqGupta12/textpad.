
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os

root =  Tk()
root.title("code editer ")
root.geometry("500x500")


my_text = Text(root ,width = 250 , height = 250, font = ("Helvetica ",14))
my_text.pack()   

def newfiles():
    my_text.delete("1.0 ", END)
    root.title('New file - TextPad!')
    status_bar.config(text = "New File")

def open_file():
    my_text.delete("1.0 ", END)
    files = [('All Files', '*.*'), ('Text Document', '*.txt')]
    text_file = filedialog.askopenfilename(initialdir = "*/",title= "open...", filetypes = files, defaultextension = files)
    # title bar
    status_bar.config( text= text_file)
    root.title(f'{text_file} - TextPad!')
    # open files
    files = open (text_file, 'r')
    stuff = files.read()
    my_text.insert(END, stuff)

    files.close()


def saveAS():
    files = [('All Files', '*.*'), ('Text Document', '*.txt')]
    file = filedialog.asksaveasfile(mode = "w",initialdir = "*/",title= " Save As...", filetypes = files, defaultextension = files)
    file_text = str(my_text.get(1.0,END))
    # title bar
    status_bar.config( text= file)
    root.title(f'{file} - TextPad!')
    # write file
    file.write(file_text)
    # file close
    file.close()

def save():
    files = [('All Files', '*.*'), ('Text Document', '*.txt')]

    file = filedialog.asksaveasfilename(initialname = "*/", filetypes = files, defaultextension = files)
    file_text = str(my_text.get(1.0,END))
    # write file
    file.write(file_text)
    # file close
    file.close()
    

def terminaleopen():
    # directory =  os.system("C:\Windows\system32\cmd.exe")
    stuff= os.startfile("cmd.exe")
    os.getcwd(stuff)

menubar = Menu(root)

root.config(menu = menubar)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = newfiles)
file.add_command(label ='Open...', command = open_file)
file.add_command(label ='Save', command = save)
file.add_command(label ='Save As', command = saveAS)

file.add_separator()
file.add_command(label ='Exit', command = root.destroy)


    
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Terminal', menu = edit)
edit.add_command(label ='Terminal', command = terminaleopen)




inputtxt = Text(root)
Inputt = inputtxt.get("1.0", "end - 1c")


status_bar = Label (root ,text='Read')
status_bar.pack(fill=X , side= BOTTOM, ipady=5)

inputtxt.pack()

root.mainloop()
 
