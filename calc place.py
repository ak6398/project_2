from tkinter import *
cal=Tk()
operator=""
cal.title("Calculator")
cal.geometry("400x390")
txt_input=StringVar()

def btnClick(numbers):
    global operator
    operator=operator +str(numbers)
    txt_input.set(operator)
    
def btnClearDisplay():
    global operator
    operator=""
    txt_input.set("")
    
def equalsum():
    global operator
    sums=str(eval(operator))
    txt_input.set(sums)
    operator=sums
    
    

txtdisplay=Entry(cal,font=('arial',20,'bold'),text=txt_input,bd=30,insertwidth=4,bg="powder blue",justify="right").grid(row=1,column=0)

btn7=Button(cal,font=('arial',14,'bold'),text="7",command=lambda:btnClick(7),bd=8,padx=16).place(x=6,y=100)
btn8=Button(cal,font=('arial',14,'bold'),text="8",command=lambda:btnClick(8),bd=8,padx=16).place(x=100,y=100)
btn9=Button(cal,font=('arial',14,'bold'),text="9",command=lambda:btnClick(9),bd=8,padx=16).place(x=200,y=100)
add=Button(cal,padx=16,bd=8,fg="black",font=("arial",14,"bold"),text="+",command=lambda:btnClick("+")).place(x=300,y=100)

btn4=Button(cal,font=('arial',14,'bold'),text="4",command=lambda:btnClick(4),bd=8,padx=16).place(x=6,y=170)
btn5=Button(cal,font=('arial',14,'bold'),text="5",command=lambda:btnClick(5),bd=8,padx=16).place(x=100,y=170)
btn6=Button(cal,font=('arial',14,'bold'),text="6",command=lambda:btnClick(6),bd=8,padx=16).place(x=200,y=170)
subb=Button(cal,font=('arial',14,'bold'),text="-",command=lambda:btnClick("-"),bd=8,padx=16).place(x=300,y=170)

btn1=Button(cal,font=('arial',14,'bold'),text="1",command=lambda:btnClick(1),bd=8,padx=16).place(x=6,y=250)
btn2=Button(cal,font=('arial',14,'bold'),text="2",command=lambda:btnClick(2),bd=8,padx=16).place(x=100,y=250)
btn3=Button(cal,font=('arial',14,'bold'),text="3",command=lambda:btnClick(3),bd=8,padx=16).place(x=200,y=250)
mul=Button(cal,font=('arial',14,'bold'),text="*",command=lambda:btnClick("*"),bd=8,padx=16).place(x=300,y=250)

btnc=Button(cal,font=('arial',14,'bold'),text="C",command=btnClearDisplay,bd=8,padx=16).place(x=6,y=330)
btn0=Button(cal,font=('arial',14,'bold'),text="0",command=lambda:btnClick(0),bd=8,padx=16,fg="red").place(x=100,y=330)
btneq=Button(cal,font=('arial',14,'bold'),text="=",command=equalsum,bd=8,padx=16).place(x=200,y=330)
div=Button(cal,font=('arial',14,'bold'),text="/",command=lambda:btnClick("/"),bd=8,padx=16).place(x=300,y=330)

cal.mainloop()