from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
def submit():
    username=e_username.get();
    password=e_password.get();
    type=e_type.get();
    if(username==""or password==""or type==""):
        Messagebox.showinfo("login status","ALL FIELDS ARE REQUIRED")
    else:
        con=mysql.connect(host='localhost',user='root',password='saranya15',database='sm')
        cursor=con.cursor()
        cursor.execute("insert into login values('"+username+"','"+password+"','"+type+"')")
        cursor.execute("commit")
        e_username.delete(0,'end')
        e_password.delete(0,'end')
        e_type.delete(0,'end')
        Messagebox.showinfo( "login status","submited successfully")
        con.close;
    root.destroy()
    return
root=Tk()
root.title("MINIPROJECT")
root.geometry("800x800")
bg=PhotoImage(file="C:/Users/ELCOT/Pictures/Promo-Facebook-Facebook marketplace.png")
login=Label(root,image=bg)
login.place(x=0,y=0)
login=Label(root,text="REGISTER HERE",bg="yellow",font=('italic'))
login.place(x=150,y=0)
#lbl.pack()
username=Label(root,text="USERNAME:")
username.place(x=20,y=30)
e_username=Entry()
e_username.place(x=150,y=30)
password=Label(root,text="PASSWORD:")
password.place(x=20,y=60)
e_password=Entry()
e_password.place(x=150,y=60)
type=Label(root,text="TYPE:")
type.place(x=20,y=90)
#Radiobutton(root,text="STUDENT",value=1).place(x=150,y=90)
#Radiobutton(root,text="STAFF",value=2).place(x=250,y=90)
e_type=Entry()
e_type.place(x=150,y=90)
login=Button(root,text="LOGIN",bg="yellow",command=submit,width=20,height=2)
login.place(x=150,y=200)
root.mainloop()
########################
def registration():
        registrationid = e_registrationid.get();
        Firstname = e_Firstname.get();
        Lastname=e_Lastname.get();
        Gender=e_Gender.get();
        dob = e_dob.get();
        email = e_email.get();
        address = e_address.get();
        city=e_city.get();
        mobile_no=e_mobile_no.get();
        if(registrationid==""or Firstname==""or Lastname==""or Gender==""or dob==""or email==""or address==""or city==""or mobile_no==""):
            Messagebox.showinfo("registration status","ALL FIELDS ARE REQUIRED")
        else:
            con=mysql.connect(host="localhost", user="root", password="saranya15", database="sm")
            cursor = con.cursor()
            cursor.execute("insert into registration values('"+registrationid+"','"+Firstname+"','"+Lastname+"','"+Gender+"','"+dob+"','"+email+"','"+address+"','"+city+"','"+mobile_no+"')")
            cursor.execute("commit")
            e_Firstname.delete(0,'end')
            e_Lastname.delete(0,'end')
            e_Gender.delete(0,'end')
            e_dob.delete(0,'end')
            e_email.delete(0,'end')
            e_address.delete(0,'end')
            e_city.delete(0,'end')
            e_mobile_no.delete(0,'end')
            Messagebox.showinfo("registration status","SAVED SUCESSFULLY")
            con.close();
            window.destroy()
            return
window=Tk()
window.title("MINIPROJECT")
window.geometry("1000x800")
bg=PhotoImage(file="C:/Users/ELCOT/Pictures/10_ways_course registration_students (1) (1).png")
registration=Label(window,image=bg)
registration.place(x=0,y=0)
lbl=Label(window,text="REGISTER HERE",background="yellow",font=('italic'))
lbl.pack()
registrationid=Label(window,text="REGISTRATION ID:")
registrationid.place(x=20,y=30)
e_registrationid=Entry(window)
e_registrationid.place(x=150,y=30)
Firstname=Label(window,text="FIRST NAME:")
Firstname.place(x=20,y=80)
e_Firstname=Entry(window)
e_Firstname.place(x=150,y=80)
Lastname=Label(window,text="LAST NAME:")
Lastname.place(x=20,y=130)
e_Lastname=Entry(window)
e_Lastname.place(x=150,y=130)
Gender=Label(window,text="GENDER:")
Gender.place(x=20,y=180)
e_Gender=Entry(window)
e_Gender.place(x=150,y=180)
dob=Label(window,text="DOB:")
dob.place(x=20,y=230)
e_dob=Entry()
e_dob.place(x=150,y=230)
email=Label(window,text="EMAIL:")
email.place(x=20,y=280)
e_email=Entry()
e_email.place(x=150,y=280,width=200)
address=Label(window,text="ADDRESS:")
address.place(x=20,y=330)
e_address=Entry(window)
e_address.place(x=150,y=330,width=200)
city=Label(window,text="CITY:")
city.place(x=20,y=380)
e_city=Entry(window)
e_city.place(x=150,y=380)
mobile_no=Label(window,text="MOBILE NUMBER:")
mobile_no.place(x=20,y=430)
e_mobile_no=Entry(window)
e_mobile_no.place(x=150,y=430)
registration=Button(window,text="NEXT",bg="yellow",font=('bold'),command=registration)
registration.place(x=200,y=600)
window.mainloop

#########################################################
window1=Tk()
window1.geometry("1000x800")
window1.title("MINIPROJECT")
bg=PhotoImage(file="C:/Users/ELCOT/Pictures/Computer-Tech-Wallpaper-21-4368x2912.png")
course=Label(window1,image=bg)
course.place(x=0,y=0)
lbl=Label(window1,text=" COURSE REGISTRATION",background="skyblue",font=('italic'))
lbl.place(x=150,y=0)
lbl.pack()
courseid=Label(window1,text="COURSE ID:")
courseid.place(x=20,y=30)
e_courseid=Entry(window1)
e_courseid.place(x=150,y=30)
coursestream=Label(window1,text="COURSE STREAM:")
coursestream.place(x=20,y=80)
e_coursestream=Entry(window1)
e_coursestream.place(x=150,y=80)
coursetype=Label(window1,text="COURSE TYPE:")
coursetype.place(x=20,y=130)
e_coursetype=Entry(window1)
e_coursetype.place(x=150,y=130)
coursename=Label(window1,text="COURSE NAME:")
coursename.place(x=20,y=180)
e_coursename=Entry(window1)
e_coursename.place(x=150,y=180)
coursetime=Label(window1,text="COURSE TIME:")
coursetime.place(x=20,y=230)
e_coursetime=Entry(window1)
e_coursetime.place(x=150,y=230)
courseduration=Label(window1,text="COURSE DURATION:")
courseduration.place(x=20,y=280)
e_courseduration=Entry(window1)
e_courseduration.place(x=150,y=280)
coursefee=Label(window1,text="COURSE FEE:")
coursefee.place(x=20,y=330)
e_coursefee=Entry(window1)
e_coursefee.place(x=150,y=330)
feetype=Label(window1,text="FEE TYPE:")
feetype.place(x=20,y=380)
e_feetype=Entry(window1)
e_feetype.place(x=150,y=380)
def course():
    
        courseid= e_courseid.get();
        coursestream=e_coursestream.get();
        coursetype= e_coursetype.get();
        coursename=e_coursename.get();
        coursetime=e_coursetime.get();
        coursefee=e_coursefee.get();
        courseduration=e_courseduration.get();
        feetype=e_feetype.get();
        if( courseid==""or  coursestream==""or coursetype==""or coursename==""or coursetime=="" or coursefee=="" or courseduration=="" or feetype==""):
            Messagebox.showinfo("course status","ALL FIELDS ARE REQUIRED")
        else:
            con=mysql.connect(host="localhost", user="root", password="saranya15", database="sm")
            cursor = con.cursor()
            cursor.execute("insert into course values('"+courseid+"','"+coursestream+"','"+coursetype+"','"+coursename+"','"+coursetime+"','"+coursefee+"','"+courseduration+"','"+feetype+"')")
            cursor.execute("commit")
            e_courseid.delete(0,'end')
            e_coursestream.delete(0,'end')
            e_coursetype.delete(0,'end')
            e_coursename.delete(0,'end')
            e_coursetime.delete(0,'end')
            e_coursefee.delete(0,'end')
            Messagebox.showinfo("course status"," YOUR REGISTRATION HAS BEEN RECORDED SUCESSFULLY")
            con.close();
        window1.destroy()
        return  
course=Button(window1,text="SUBMIT",bg="white",font=('bold'),command=course)
course.place(x=500,y=500)
window1.mainloop()
#####################################
