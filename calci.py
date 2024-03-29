from tkinter import*
root=Tk()
root.title("Simple Calculator")
root.geometry("312x324")
root.resizable(0,0)
expression=""

def btn_click(item):
    global expression
    expression=expression + str(item)
    input_text.set(expression)

def btn_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    
def btn_clear():
    global expression
    expression=""
    input_text.set("")

input_text=StringVar()
 
#The first thing is to create a frame for the input value
input_frame=Frame(root,width=312,height=50,highlightthickness=1,bg='lightblue')
input_frame.pack(side=TOP)

#once you have the field defined then you need a separete frame for  buttons
butn_frame=Frame(root,width=312,height=272,bg="grey")
butn_frame.pack()
clear=Button(butn_frame,text='c',fg="black",width=34,height=3,command=lambda: btn_clear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide=Button(butn_frame,text="/",fg="black",width=10,height=3,command=lambda: btn_click("/")).grid(row=0,column=3)
Seven=Button(butn_frame,text="7",fg="black",width=10,height=3,command=lambda: btn_click(7)).grid(row=1,column=0,)
Eight=Button(butn_frame,text="8",fg="black",width=10,height=3,command=lambda: btn_click(8)).grid(row=1,column=1,)
Nine=Button(butn_frame,text="9",fg="black",width=10,height=3,command=lambda: btn_click(9)).grid(row=1,column=2)
multi=Button(butn_frame,text="x",fg="black",width=10,height=3,command=lambda: btn_click("*")).grid(row=1,column=3)
four=Button(butn_frame,text="4",fg="black",width=10,height=3,command=lambda: btn_click(4)).grid(row=2,column=0)
five=Button(butn_frame,text="5",fg="black",width=10,height=3,command=lambda: btn_click(5)).grid(row=2,column=1)
six=Button(butn_frame,text="6",fg="black",width=10,height=3,command=lambda: btn_click(6)).grid(row=2,column=2)
add=Button(butn_frame,text="+",fg="black",width=10,height=3,command=lambda: btn_click("+")).grid(row=2,column=3)
one=Button(butn_frame,text="1",fg="black",width=10,height=3,command=lambda: btn_click(1)).grid(row=3,column=0,padx=1)
two=Button(butn_frame,text="2",fg="black",width=10,height=3,command=lambda: btn_click(2)).grid(row=3,column=1,padx=1)
three=Button(butn_frame,text="3",fg="black",width=10,height=3,command=lambda: btn_click(3)).grid(row=3,column=2,padx=1,pady=1)
subtract=Button(butn_frame,text="-",fg="black",width=10,height=3,command=lambda: btn_click("-")).grid(row=3,column=3,padx=1)
zero=Button(butn_frame,text='0',fg="red",width=22,height=3,command=lambda: btn_click(0)).grid(row=4,column=0,columnspan=2)
point=Button(butn_frame,text=".",fg="black",width=10,height=3,command=lambda: btn_click(".")).grid(row=4,column=2)
equal=Button(butn_frame,text="=",fg="black",width=10,height=3,command=lambda:btn_equal()).grid(row=4,column=3)
input_field=Entry(input_frame,font=('arial',20,'bold'),textvariable=input_text,width=50,bg="lightblue",bd=5,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack()

root.mainloop()