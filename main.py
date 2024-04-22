import src
import cv2
import tkinter as tk
from PIL import ImageTk
from customtkinter import *
from customtkinter import CTkButton
import datetime


win = CTk()
win.title("HOME")
win.geometry("1080x1710")
bg=ImageTk.PhotoImage(file = r"3.png")
frame = tk.Frame(win)
frame.pack(side="top",expand=True,fill="both")

label1 = tk.Label( frame, image = bg)
label1.place(x = 0, y = 0)

heading = tk.Label( frame, text=" Clicks To Carts : A New Age of Queue-Free Shopping " , font="Helvetica 24 bold",background="#00edf8" )
heading.pack(side="top",pady=10)

'''
Button Functions
'''
def but1_cmd():
    stock = src.Inventory(20)
    c=30
    f=open("stock.txt","w")
    img = cv2.imread(r"4.png", cv2.IMREAD_COLOR)
    cv2.putText(img,"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*Displaying Stock*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- " ,(135,95), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(img,"                     Items                                 Quantity(Nos.)        " ,(135,125), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    f.write(f"*-*-*-*-*-*-*-*-*-*-*-Displaying Stock : {datetime.datetime.now()}*-*-*-*-*-*-*-*-*-*-*- \n")
    f.write("\n                     Items                                 Quantity(Nos.)        \n")
    for item in stock:
        cv2.putText(img,f"                     {item}                 :                {stock[item]}   " ,(135,125+c), cv2.FONT_HERSHEY_TRIPLEX, 0.6, (0, 0, 0), 2)
        f.write(f"                     {item}                 :                {stock[item]}   \n")
        c+=30
    f.flush()
    f.close()
    cv2.putText(img,"                     Press any key to exit ...  " ,(135,65), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    cv2.imshow("START", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("\n\t\t\tStock/Inventory : ",stock)
    tk.messagebox.showinfo(title="CONFIRMATION", message="Stock/Inventory is saved ✅")

def but2_cmd():
    '''shop cmd'''
    def but2_subcmd():
        stock = {}
        credentials = prompt_entry.get().strip()
        f=open(f"stock.txt", "r")
        std_syntax=f.readline()
        std_syntax=f.readline()
        std_syntax=f.readline()
        std_syntax=f.read()
        key=""
        val=""
        for char in std_syntax:
            if char.isalpha()==True:
                key+=char
            if char.isdigit():
                val+=char
            if char=="\n" or char==EOFError:
                stock[key]=int(val)
                key,val="",""
     

        win2.destroy()
        tk.messagebox.showinfo(title=" START ", message=" Confirm to start shopping  ✅")
    
        while True:        
            if src.LiveCheck() == False:
                break
        stock_curr,sale=src.sale(20,stock)
        print("\n\t\t\tCurrent stock : ",stock_curr,"\n\t\t\tSale : ",sale)

        f=open("stock.txt","w")#update stock
        f.write(f"*-*-*-*-*-*-*-*-*-*-*-Displaying Stock : {datetime.datetime.now()}*-*-*-*-*-*-*-*-*-*-*- \n")
        f.write("\n                     Items                                 Quantity(Nos.)        \n")
        for item in stock_curr:
           f.write(f"                     {item}                 :                {stock_curr[item]}   \n")
        f.flush()
        f.close()

        bill=src.Bill(sale)
        print("\n\t\t\tBill : ",bill)

        c=30
        qty,tot_amt=0,0
        f=open(f"{credentials}.txt", "a+")#To generate bill
        img = cv2.imread(r"4.png", cv2.IMREAD_COLOR)
        cv2.putText(img,"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*Displaying Sale*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- " ,(135,95), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        cv2.putText(img,"          Items              Quantity(Nos.)            Price(INR)          Amount       " ,(135,125), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        f.write(f"*-*-*-*-*-*-*-*-*-*-*-Displaying Sale  : {datetime.datetime.now()}*-*-*-*-*-*-*-*-*-*-*- \n")
        f.write("\n          Items                Quantity              Price            Amount       \n")
        for obj in bill: 
            cv2.putText(img,f"         {obj[0]}                   {obj[1]}                 {obj[2]}                   {obj[3]}",(135,125+c), cv2.FONT_HERSHEY_TRIPLEX, 0.6, (0, 0, 0), 2)
            f.write(f"         {obj[0]}                   {obj[1]}                 {obj[2]}                   {obj[3]}\n")
            c+=30 
            qty+=obj[1]
            tot_amt+=obj[3]
        f.write("\n*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")              
        f.write(f"              Total                QTY: {qty} Nos.              AMOUNT(INR) : {tot_amt}  \n")
        f.write("\n*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")              
        f.flush()
        f.close()
        cv2.putText(img,"                     Press any key to exit ...  " ,(135,65), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        cv2.imshow("SALE", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        tk.messagebox.showinfo(title="THANK YOU", message="Thankyou for shopping with us! 🫡")


        

    win2 = CTkToplevel(win)
    win2.title("Shopping Tracker")
    win2.geometry("1080x720")
    bg2=ImageTk.PhotoImage(file = r"1.png")
    frame2 = tk.Frame(win2)
    frame2.pack(side="top",expand=True,fill="both")

    label1 = tk.Label( frame2, image = bg2)
    label1.place(x = 0, y = 0)

    heading = tk.Label( frame2, text=" Clicks To Carts : A New Age of Queue-Free Shopping " , font="Helvetica 24 bold",background="#03284a",fg="#e6f7ff")
    heading.pack(side="top",pady=10)

    title = tk.Label( frame2, text=" Enter Credentials " , font="Helvetica 24 bold",background="#012849",fg="#e6f7ff" )
    title.pack(side="top",pady=10)

    prompt_label = tk.Label(frame2, text=" Enter Your Name / ID ",font="Helvetica 18 bold",background="#29465e",fg="#e6f7ff")
    prompt_label.pack(pady=20)

    prompt_entry = CTkEntry(frame2,bg_color="#143d56",height=50,width=200,corner_radius=20)
    prompt_entry.pack(pady=20)

    but=CTkButton(frame2,height=60,width=175,text=" S T A R T \n S H O P P I N G ",font=("Avenir", 22 ,"bold"),bg_color="#4e6075",hover_color="#80d4ff",text_color=("White"),corner_radius=60,command=but2_subcmd)
    but.pack(pady=50)
    win2.mainloop()

def but3_cmd():
    tk.messagebox.showinfo(title="THANK YOU", message="Thankyou! Vist again 🖤")
    win.destroy()
    exit(0)




but1=CTkButton(frame,height=60,width=175,text=" I N V E N T O R Y \n C H E C K ",font=("Avenir", 22 ,"bold"),bg_color="#01e3ec",hover_color="#00aaff",text_color=("White"),corner_radius=60,command=but1_cmd)
but1.pack(pady=50)

but2=CTkButton(frame,height=60,width=175,text=" S T A R T \n S H O P P I N G ",font=("Avenir", 22 ,"bold"),bg_color="#37d8e4",hover_color="#00aaff",text_color=("White"),corner_radius=60,command=but2_cmd)
but2.pack(pady=50)

but3=CTkButton(frame,height=60,width=175,text=" E X I T ",font=("Avenir", 22 ,"bold"),bg_color="#9dd2bd",hover_color="#00aaff",text_color=("White"),corner_radius=60,command=but3_cmd)
but3.pack(pady=50)



win.mainloop()