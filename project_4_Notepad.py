from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("new-Untitled")
    file=None
    textarea.delete(1.0,END)

def opnfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("All Documents","*.txt")])
    
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) +"Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
        

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Documents","*.txt")])
    if file=="":
        file=None
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        
        root.title(os.path.basename(file)+"-notepad")
        print("file saved")
        
   
  
        
        
     
def close():
    pass
def cut1():
    textarea.event_generate(("<<Cut>>"))
    
def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))
    
def about():
    showinfo("UNTITLED","NOTEPAD BY LENOVO")
    
def close():
    root.destroy()

if __name__=="__main__":
    
    root=Tk()
    root.title("Untitled- Notepad")
    root.geometry("700x500")
    #to create text area
    
    textarea=Text(root,font=("arial",15))
    file=None
    textarea.pack(fill=BOTH,expand=True)
    
    #create a menu bar
    MenuBar=Menu(root)
    filemenu=Menu(MenuBar,tearoff=0)
    
    

    #create a new file
    filemenu.add_command(label="New",command=newfile)
    
    filemenu.add_command(label="open",command=opnfile)

    filemenu.add_command(label="Save",command=save)
    filemenu.add_separator()
    
    filemenu.add_command(label="Exit",command=close)
    
    MenuBar.add_cascade(label="FILE",menu=filemenu)
    
    Editmenu=Menu(MenuBar,tearoff=0)
    Editmenu.add_command(label="cut",command=cut1)
    Editmenu.add_command(label="copy",command=copy)
    Editmenu.add_command(label="paste",command=paste)
    
    
    
    MenuBar.add_cascade(label="EDIT",menu=Editmenu)
    
    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    
    MenuBar.add_cascade(label="HELP",menu=HelpMenu)
    
    root.config(menu=MenuBar)
    
    #adding scrollbar
    scrollbar=Scrollbar(textarea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)
    
    
    
    























    
    
    root.mainloop()