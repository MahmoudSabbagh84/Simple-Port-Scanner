from tkinter import *
from PIL import ImageTk, Image
import socket
import threading

root = Tk()
root.title("Port Scanner")
root.iconbitmap("C:/Users/mahmo/Desktop/Radar.ico")
root.geometry("840x400")

result_label = Label(root,text="Port Status : ", padx= 3, pady =3)
result_label.grid(row = 1, column= 5)

resultbox = Entry(root, borderwidth = 10)
resultbox.grid(row = 1, column = 6, columnspan=2)


  

        


Label1 = Label(root, text = "Welcome to Port Scanner, Please use only on Authorized Networks" , font=("",20),fg="Red", anchor = N)
Label1.grid(row=0,column =0 , columnspan = 10)

Frame1 = LabelFrame(root, text = "Target Information", padx = 25 ,pady = 25, width= 100, height = 400, labelanchor = N)
Frame1.grid(row = 1, column = 0)



port = Entry(Frame1, borderwidth = 5)
port.grid(row=1,column=1)
port_label= Label(Frame1,text = "Port: ", padx=3, pady=3 )
port_label.grid(row=1, column=0)

TargetIP = Entry(Frame1, borderwidth = 5, )
TargetIP.grid(row=0,column=1)
TargetIP_label= Label(Frame1,text = "Target IP: ", padx=9, pady=15 )
TargetIP_label.grid(row=0, column=0)

def portscan():
    p = int(port.get())
    t = TargetIP.get()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((t,p))
        resultbox = Entry(root, borderwidth = 10, bg = "Green")
        resultbox.grid(row = 1, column = 6, columnspan=2)
        resultbox.delete(0,END)
        resultbox.insert(0,"OPEN")
    except:
        resultbox = Entry(root, borderwidth = 10, bg = "Red")
        resultbox.grid(row = 1, column = 6, columnspan=2)
        resultbox.delete(0,END)
        resultbox.insert(0,"CLOSED")


    

scan_btn = Button(root, text= "SCAN", command = portscan, width = 10)
scan_btn.grid(row=2, column = 0, pady=25, columnspan = 1)


root.mainloop()