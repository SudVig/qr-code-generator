from email import contentmanager
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import qrtools
#filename=filedialog.askdirectory()

import qrcode
global content
content="Your Qr Code ConTent\n Will Appear Here"

def make():
    img=qrcode.make(text.get(1.0,END))
   
    print(len(name.get()))
    if(len(name.get())!=0):
        filename=filedialog.askdirectory()
        img.save(filename+"/"+name.get()+".png")
        messagebox.showinfo("Sucess","Downloaded Successfully")
    else:
        messagebox.showinfo("Please","Enter The Image Name")




root=Tk()
name=StringVar()
label=Label(root,text="\nQr Code\n",font="Tahoma")
label.grid(column=0,row=0)
text=Text(root,height=10)
text.grid(column=0,row=1)
label=Label(root,text="\nEnter The Image Name\n",font="Tahoma")
label.grid(column=0,row=2,sticky="w")
ent=Entry(root,textvariable=name,width=50)
ent.grid(column=0,row=3,sticky="w")
btn=Button(root,text="Generate",font="Tahoma",command=make)
btn.grid(column=0,row=4,sticky="w")
label=Label(root,text="\n\n")
label.grid(column=0,row=5)



root.mainloop()