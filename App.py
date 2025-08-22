from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
from tkcalendar import *
import sqlite3
import csv,random
from datetime import *
k=datetime.now()
today_date="Date:"+str(k.day)+"/"+str(k.month)+"/"+str(k.year)
win=Tk()
win.title("Main Page")
win.iconbitmap(r"D:/Python Projects/ATM/Resources/Logo.ico")
win.geometry("1350x690+0+0")
top=Frame(win)
top.pack_propagate(False)
top.configure(height=50,width=1350)
top.place(x=0,y=0)
left=Frame(win)
left.pack_propagate(False)
left.configure(height=640,width=400)
left.place(x=0,y=50)
right=Frame(win)
right.pack_propagate(False)
right.configure(height=640,width=950)
right.place(x=400,y=50)
gender=StringVar()
requ=StringVar()
dis_name=['Ariyalur', 'Chengalpattu', 'Chennai', 'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul', 'Erode', 'Kallakurichi', 'Kanchipuram', 'Kanniyakumari', 'Karur', 'Krishnagiri', 'Madurai', 'Mayiladuthurai', 'Nagapattinam', 'Namakkal', 'Nilgiris', 'Perambalur', 'Pudukkottai', 'Ramanathapuram', 'Ranipet', 'Salem', 'Sivagangai', 'Tenkasi', 'Thanjavur', 'Theni', 'Thoothukudi', 'Tiruchirappalli', 'Tirunelveli', 'Tirupathur', 'Tiruppur', 'Tiruvallur', 'Tiruvannamalai', 'Tiruvarur', 'Vellore', 'Viluppuram', 'Virudhunagar']
def new_user():
    def rec():
        accno='8432'
        for i in range(4):
            a=random.choice(list(range(0,10)))
            accno+=str(a)
        return accno
    for widgets in right.winfo_children():
        widgets.destroy()
    def save():
        con=sqlite3.connect("Main_Server.db")
        c=con.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Bank (Account_Number,Name,DOB,Gender,Address,Phone_Number,Educational_Qua)")
        accno=rec()
        name=na.get()+" "+sna.get()
        gen=gender.get()
        dob1=dob.get()
        edu=eduq.get()
        address=add.get()
        dist=dis.get()
        phone=mobile.get()
        con11=not sna.get().isalpha()
        con1=not na.get().isalpha()
        if  con11 or con1:
            messagebox.showwarning("Alert","Name is invalid\nTry Again")
        else:
            c.execute('select * from Bank where Account_Number=(?) and Name=(?)',(accno,name))
            v=c.fetchall()
            while v!=[]:
                accno=rec()
                c.execute('select * from Bank where Account_Number=(?) and Name=(?)',(accno,name))
                v=c.fetchall()
            c.execute('select * from Bank where Address=(?) and Name=(?)',(address+" - "+dist+" (dt) ",name))
            av=c.fetchall()
            if av!=[]:
                c.execute('select * from Bank where Phone_Number=(?) and Name=(?)',(phone,name))
                av=c.fetchall()
                if av!=[]:
                    messagebox.showwarning("Alert","I think This User is Also Registered\nPlease Ensure the Ledger..")
            else:
                c.execute("insert into Bank values(?,?,?,?,?,?,?)",(accno,name,dob1,gen,address+" - "+dist+" (dt) ",phone,edu))
                con.commit()
                messagebox.showinfo("Success",f"{name} is added Successfully.")
                messagebox.showinfo("Account Number",f"{name} your Acc.no is {accno}")
                letter=name.replace(" ","_")+"Acc"
                c.execute("Create Table if not exists {} (Date,Credit,Debit,Balance)".format(letter))
                na.delete("0",END)
                sna.delete("0",END)
                dob.delete("0",END)
                eduq.delete("0",END)
                mobile.delete("0",END)
                dis.delete("0",END)
                add.delete("0",END)
    Label(right,text="New Account Page",font=("Terminal",22,'underline'),fg='blue').place(x=150,y=20)
    Label(right,text="Account Holder Name:",font=("Courier New Baltic",12,'bold')).place(x=0,y=80)
    na=Entry(right,font=("Courier New Baltic",12,'bold'))
    na.place(x=200,y=80)
    Label(right,text="S/W/D of:",font=("Courier New Baltic",12,'bold')).place(x=0,y=130)
    sna=Entry(right,font=("Courier New Baltic",12,'bold'))
    sna.place(x=200,y=130)
    Label(right,text="Gender:",font=("Courier New Baltic",12,'bold')).place(x=0,y=200)
    Radiobutton(right,text="Male",value="Male",variable=gender,font=("Courier New Baltic",12,'bold')).place(x=200,y=200)
    Radiobutton(right,text="Female",value="Female",variable=gender,font=("Courier New Baltic",12,'bold')).place(x=350,y=200)
    Label(right,text="Date of Birth:",font=("Courier New Baltic",12,'bold')).place(x=0,y=270)
    dob=DateEntry(right,date_pattern='dd/mm/yyyy')
    dob.place(x=200,y=270)
    Label(right,text="Educational Quality:",font=("Courier New Baltic",12,'bold')).place(x=0,y=340)
    eduq=Combobox(right,values=['Below 10th','Below 12th','UG','PG'],font=("Courier New Baltic",12,'bold'))
    eduq.place(x=200,y=340)
    Label(right,text="Phone Number:",font=("Courier New Baltic",12,'bold')).place(x=0,y=410)
    mobile=Entry(right,font=("Courier New Baltic",12,'bold'))
    mobile.place(x=200,y=410)
    Label(right,text="Address:",font=("Courier New Baltic",12,'bold')).place(x=0,y=480)
    add=Entry(right,font=('Courier New Baltic',12,'bold'),width=30)
    add.place(x=150,y=480)
    Label(right,text="District:",font=("Courier New Baltic",12,'bold')).place(x=500,y=480)
    dis=Combobox(right,values=dis_name,font=('Courier New Baltic',12,'bold'))
    dis.place(x=600,y=480)
    dis.set('Select District')
    Button(right,text="Proceed and Save",font=('Courier New Baltic',12,'bold'),relief=GROOVE,command=save).place(x=320,y=550)
def summary():
    for widgets in right.winfo_children():
        widgets.destroy()
    def pres(e):
        num=nu.get()
        con=sqlite3.connect("Main_Server.db")
        c=con.cursor()
        c.execute("Select Name from Bank where Account_Number=(?)",(num,))
        f=c.fetchall()
        if f==[]:
            messagebox.showwarning("Alert","Account Number Doesn't Exists")
        else:
            q=f[0][0].replace(" ","_")+"Acc"
            c.execute("select * from {}".format(q))
            data=c.fetchall()
            treev = ttk.Treeview(right, selectmode ='browse')
            treev.place(x=10,y=250)
            verscrlbar = Scrollbar(right,orient ="vertical", command = treev.yview)
            verscrlbar.place(x=600,y=300)
            treev.configure(xscrollcommand = verscrlbar.set)
            treev["columns"] = ("1", "2", "3","4")
            treev['show'] = 'headings'
            treev.column("1", width = 120, anchor ='c')
            treev.column("2", width = 150, anchor ='c')
            treev.column("3", width = 150, anchor ='c')
            treev.column("4", width = 150, anchor ='c')
            treev.heading("1", text ="Date")
            treev.heading("2", text ="Credit")
            treev.heading("3", text ="Debit")
            treev.heading("4", text ="Balance")
            for i in data:
                treev.insert("", 'end', text ="L1", values =i)
            c.execute("select Balance from {} order by rowid desc LIMIT 1".format(q))
            ass=c.fetchall()
            Label(right,text="Current Balance: "+str(ass[0][0]),font=("Calibri",18,'bold')).place(x=200,y=140)
    Label(right,text="Summary Page",font=("Terminal",22,'underline'),fg='blue').place(x=150,y=20)
    Label(right,text="Account Number:",font=("Courier New Baltic",12,'bold')).place(x=0,y=80)
    nu=Entry(right,font=("Courier New Baltic",12,'bold'))
    nu.place(x=200,y=80)
    nu.bind('<Return>',pres)
def deposit():
    for widgets in right.winfo_children():
        widgets.destroy()
    def pres(e):
        accno=nu.get()
        amount=am.get()
        con=sqlite3.connect("Main_Server.db")
        c=con.cursor()
        c.execute("Select Name from Bank where Account_Number=(?)",(accno,))
        f=c.fetchall()
        if f==[]:
            messagebox.showwarning("Alert","Account Number Doesn't Exists")
        else:
            q=f[0][0].replace(" ","_")+"Acc"
            c.execute("Create Table if not exists {} (Date,Credit,Debit,Balance)".format(q))
        s=messagebox.askyesno("About",f"Please Ensure the Amount and Account.No\n{accno}\t{amount}")
        if s:
            date=dob.get()
            c.execute("select Balance from {} order by rowid desc LIMIT 1".format(q))
            ass=c.fetchall()
            if ass==[]:
                k=0+int(amount)
                c.execute("insert into {} values(?,?,?,?)".format(q),(date,amount,None,k))
                messagebox.showinfo("Balance",f"Your Balance is :{k}")
                con.commit()
            else:
                c.execute("select Balance from {} order by rowid desc LIMIT 1".format(q))
                f=c.fetchall()
                k1=f[0][0]
                k=k1+int(amount)
                c.execute("insert into {} values(?,?,?,?)".format(q),(date,amount,None,k))
                messagebox.showinfo("Balance",f"Your Balance is :{k}")
                con.commit()
    Label(right,text="Deposit Page",font=("Terminal",22,'underline'),fg='blue').place(x=150,y=20)
    Label(right,text="Account Number:",font=("Arial Rounded MT Bold",18,'bold')).place(x=0,y=80)
    nu=Entry(right,font=("Arial Rounded MT Bold",18,'bold'))
    nu.place(x=300,y=80)
    Label(right,text="Date of Birth:",font=("Arial Rounded MT Bold",18,'bold')).place(x=0,y=180)
    dob=DateEntry(right,date_pattern='dd/mm/yyyy',font=("Arial Rounded MT Bold",18,'bold'))
    dob.place(x=300,y=180)
    Label(right,text="Amount:",font=("Arial Rounded MT Bold",18,'bold')).place(x=0,y=280)
    am=Entry(right,font=("Arial Rounded MT Bold",18,'bold'))
    am.place(x=300,y=280)
    am.bind('<Return>',pres)
def withdraw():
    for widgets in right.winfo_children():
        widgets.destroy()
    def pres(e):
        accno=nu.get()
        amount=am.get()
        con=sqlite3.connect("Main_Server.db")
        c=con.cursor()
        c.execute("Select Name from Bank where Account_Number=(?)",(accno,))
        f=c.fetchall()
        if f==[]:
            messagebox.showwarning("Alert","Account Number Doesn't Exists")
        else:
            q=f[0][0].replace(" ","_")+"Acc"
            c.execute("Create Table if not exists {} (Date,Credit,Debit,Balance)".format(q))
        s=messagebox.askyesno("About",f"Please Ensure the Amount and Account.No\n{accno}\t{amount}")
        if s:
            date=dob.get()
            c.execute("select Balance from {} order by rowid desc LIMIT 1".format(q))
            ass=c.fetchall()
            if ass==[]:
                messagebox.showwarning("Balance",f"Insufficient Balance")
                con.commit()
            else:
                c.execute("select Balance from {} order by rowid desc LIMIT 1".format(q))
                f=c.fetchall()
                k1=f[0][0]
                k=k1-int(amount)
                if k>0:
                    c.execute("insert into {} values(?,?,?,?)".format(q),(date,None,amount,k))
                    messagebox.showinfo("Balance",f"Your Balance is :{k}")
                    con.commit()
                else:
                    messagebox.showwarning("Balance",f"Insufficient Balance\nContact Your Branch Manager")
    Label(right,text="Withdraw Page",font=("Terminal",22,'underline'),fg='blue').place(x=150,y=20)
    Label(right,text="Account Number:",font=("Arial Rounded MT Bold",18,'bold')).place(x=0,y=80)
    nu=Entry(right,font=("Arial Rounded MT Bold",18,'bold'))
    nu.place(x=300,y=80)
    Label(right,text="Date of Birth:",font=("Arial Rounded MT Bold",18,'bold')).place(x=0,y=180)
    dob=DateEntry(right,date_pattern='dd/mm/yyyy',font=("Arial Rounded MT Bold",18,'bold'))
    dob.place(x=300,y=180)
    Label(right,text="Amount:",font=("Arial Rounded MT Bold",18,'bold')).place(x=0,y=280)
    am=Entry(right,font=("Arial Rounded MT Bold",18,'bold'))
    am.place(x=300,y=280)
    am.bind('<Return>',pres)
def excel():
    for widgets in right.winfo_children():
        widgets.destroy()
    def pres(e):
        accno=nu.get()
        con=sqlite3.connect("Main_Server.db")
        c=con.cursor()
        c.execute("Select Name from Bank where Account_Number=(?)",(accno,))
        f=c.fetchall()
        if f==[]:
            messagebox.showwarning("Alert","Account Number Doesn't Exists")
        else:
            q=f[0][0].replace(" ","_")+"Acc"
            c.execute("select * from {}".format(q))
            ass=c.fetchall()
            f1=open(f[0][0]+".csv",'w')
            wri=csv.writer(f1,lineterminator="\n")
            wri.writerow(['','','','Account Summary','','',''])
            wri.writerow(['Account Number:','','',accno])
            wri.writerow(['Name:','','',f[0][0]])
            wri.writerow(['','',''])
            wri.writerow(["Date","Credit","Debit","Balance"])
            for i in ass:
                wri.writerow(i)
            wri.writerow(['','',''])
            wri.writerow(['','',''])
            wri.writerow(["Current Balance:","","",i[len(i)-1]])
            f1.close()
        messagebox.showinfo("Success","Exported Successfully")
    Label(right,text="Export Page",font=("Terminal",22,'underline'),fg='blue').place(x=150,y=20)
    Label(right,text="Account Number:",font=("Courier New Baltic",12,'bold')).place(x=0,y=80)
    nu=Entry(right,font=("Courier New Baltic",12,'bold'))
    nu.place(x=200,y=80)
    nu.bind('<Return>',pres)
def update():
    for widgets in right.winfo_children():
        widgets.destroy()
    Label(right,text="Enter The Password to Update",font=('System',38,'bold','underline')).place(x=50,y=150)
    pas=Tk()
    def ask_now():
        def pres(e):
            def save():
                name=na.get()+" "+sna.get()
                gen=gender.get()
                dob1=dob.get()
                edu=eduq.get()
                address=add.get()
                dist=dis.get()
                phone=mobile.get()
                con11=not sna.get().isalpha()
                con1=not na.get().isalpha()
                if  con11 or con1:
                    messagebox.showwarning("Alert","Name is invalid\nTry Again")
                else:
                    con=sqlite3.connect("Main_Server.db")
                    c=con.cursor()
                    c.execute("update Bank set Name=(?),DOB=(?),Gender=(?),Address=(?),Phone_Number=(?),Educational_Qua=(?) where Account_Number=(?)",(name,dob1,gen,address+" - "+dist+" (dt) ",phone,edu,accno))
                    con.commit()
                    messagebox.showinfo("Success","Updated Successfully\nDon't Update without Reason")
            accno=nu.get()
            con=sqlite3.connect("Main_Server.db")
            c=con.cursor()
            c.execute("Select * from Bank where Account_Number=(?)",(accno,))
            f=c.fetchall()
            if f==[]:
                messagebox.showwarning("Alert","Account Number Doesn't Exists")
            else:
                Label(right,text="Account Holder Name:",font=("Courier New Baltic",12,'bold')).place(x=0,y=80)
                na=Entry(right,font=("Courier New Baltic",12,'bold'))
                na.place(x=200,y=80)
                Label(right,text="S/W/D of:",font=("Courier New Baltic",12,'bold')).place(x=0,y=130)
                sna=Entry(right,font=("Courier New Baltic",12,'bold'))
                sna.place(x=200,y=130)
                Label(right,text="Gender:",font=("Courier New Baltic",12,'bold')).place(x=0,y=200)
                Radiobutton(right,text="Male",value="Male",variable=gender,font=("Courier New Baltic",12,'bold')).place(x=200,y=200)
                Radiobutton(right,text="Female",value="Female",variable=gender,font=("Courier New Baltic",12,'bold')).place(x=350,y=200)
                Label(right,text="Date of Birth:",font=("Courier New Baltic",12,'bold')).place(x=0,y=270)
                dob=DateEntry(right,date_pattern='dd/mm/yyyy')
                dob.place(x=200,y=270)
                Label(right,text="Educational Quality:",font=("Courier New Baltic",12,'bold')).place(x=0,y=340)
                eduq=Combobox(right,values=['Below 10th','Below 12th','UG','PG'],font=("Courier New Baltic",12,'bold'))
                eduq.place(x=200,y=340)
                Label(right,text="Phone Number:",font=("Courier New Baltic",12,'bold')).place(x=0,y=410)
                mobile=Entry(right,font=("Courier New Baltic",12,'bold'))
                mobile.place(x=200,y=410)
                Label(right,text="Address:",font=("Courier New Baltic",12,'bold')).place(x=0,y=480)
                add=Entry(right,font=('Courier New Baltic',12,'bold'),width=30)
                add.place(x=150,y=480)
                Label(right,text="District:",font=("Courier New Baltic",12,'bold')).place(x=500,y=480)
                dis=Combobox(right,values=dis_name,font=('Courier New Baltic',12,'bold'))
                dis.place(x=600,y=480)
                de=f[0][1].split()
                na.insert(END,de[0])
                sna.insert(END,de[1])
                gender.set(f[0][3])
                dob.delete("0",END)
                dob.insert(END,f[0][2])
                eduq.insert(END,f[0][len(f[0])-1])
                mobile.insert(END,f[0][len(f[0])-2])
                sql=f[0][4].split("-")
                add.insert(END,sql[0])
                dis.insert(END,sql[1])
                Button(right,text="Proceed and Update",font=('Courier New Baltic',12,'bold'),relief=GROOVE,command=save).place(x=320,y=550)
        Label(right,text="Update Page",font=("Terminal",22,'underline'),fg='blue').place(x=150,y=20)
        Label(win,text="Account Number:",font=("Courier New Baltic",12,'bold')).place(x=0,y=80)
        nu=Entry(win,font=("Courier New Baltic",12,'bold'))
        nu.place(x=200,y=80)
        nu.bind('<Return>',pres)
    def fe(e):
        v=pa.get()=="{:0>2}".format(str(k.month))+"{:0>2}".format(str(k.day)) or pa.get()=="{:0>2}".format(str(k.day))+"{:0>2}".format(str(k.month))
        if v:
            messagebox.showinfo("Success","Password Matched\nYour Are Eligible to Update")
            pas.destroy()
            for widgets in right.winfo_children():
                widgets.destroy()
            ask_now()
        else:
            messagebox.showwarning("Alert","Password Wrong\nTry Again !!!!")
            pas.destroy()
            for widgets in right.winfo_children():
                widgets.destroy()
    pas.geometry("650x500+10+10")
    pas.title("Password")
    Label(pas,text="Enter Password:",font=("Courier",18,'bold')).place(x=10,y=100)
    pa=Entry(pas,font=("Courier",18,'bold'),show="*")
    pa.place(x=280,y=100)
    pa.bind("<Return>",fe)
    pas.mainloop()
def close():
    for widgets in right.winfo_children():
        widgets.destroy()
    Label(right,text="Developed By S.Karthikeyan.",font=("FrankRuehl",24,'bold')).place(x=150,y=150)
    Label(right,text="Thanks For Using This........",font=("FrankRuehl",18,'bold','underline')).place(x=100,y=550)
    messagebox.showinfo("Exit","Developed By S.Karthikeyan")
    win.destroy()
Label(top,text="Welcome to ABC Bank.",font=('Courier',18,'bold','underline'),fg='blue3').place(x=500,y=10)
Label(top,text=today_date,font=('Courier',18,'bold')).place(x=50,y=10)
Button(left,text="New Account",font=('Bell Gothic Std Black',16),relief=GROOVE,command=new_user).place(x=50,y=100)
Button(left,text="View Statement",font=('Bell Gothic Std Black',16),relief=GROOVE,command=summary).place(x=50,y=180)
Button(left,text="Deposit",font=('Bell Gothic Std Black',16),relief=GROOVE,command=deposit).place(x=50,y=260)
Button(left,text="Withdraw",font=('Bell Gothic Std Black',16),relief=GROOVE,command=withdraw).place(x=50,y=340)
Button(left,text="Export to Excel",font=('Bell Gothic Std Black',16),relief=GROOVE,command=excel).place(x=50,y=420)
Button(left,text="Update",font=('Bell Gothic Std Black',16),relief=GROOVE,command=update).place(x=50,y=500)
Button(left,text="Exit",font=('Bell Gothic Std Black',16),relief=GROOVE,command=close).place(x=50,y=580)
win.mainloop()
