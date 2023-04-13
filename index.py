from operator import invert
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import YESNOCANCEL, showinfo
from tkinter.tix import Tree
from tkinter.ttk import Combobox, Treeview



def main():
    root = tk.Tk()
    app = Window(root)
    mytree = ttk.Treeview(root)
    root.mainloop()

def click():
    messagebox.showinfo( "Add Student Information","Do you want add!!")


class Window:
    def __init__(self,user):
        self.user = user
        self.user.title("Ứng Dụng Quản Lý Học Sinh")
        self.user.geometry("1350x750")
        self.user.title("Manager Information Students")
        # // màu nền giao diện
        self.user.config(bg="lightgrey") 
        #============Frame===========
        self.Frame = Frame(self.user)
        self.Frame.pack()
        #============Lable===========
        #title 1
        self.user_title = Label(self.Frame,text="Information Students",
                                font=("arial",40,"bold"),
                                border=11,relief = tk.GROOVE
                                ,bg="lightgrey",foreground="black",width=38)
       #detail1
        self.detail_Frame = LabelFrame(self.user,text="Detail Enter",
                                       font=("arial",18,"bold"),
                                       bg= "lightgrey",fg="black",
                                       border=12,relief = tk.GROOVE)
        self.detail_Frame.place(x = 20,y = 100,width=500,height=530)
        
        #Arial Button 
        self.arial_Frame = LabelFrame(self.user,
                                       font=("arial",20,"bold"),
                                       bg= "lightgrey",fg="black",
                                       border=12,relief = tk.GROOVE)
        self.arial_Frame.place(x=60,y=463,width=410,height=150)
    
        #==LoadDataFrame==
        self.load_data = LabelFrame(self.user,bd=12,bg="lightgrey",relief = tk.GROOVE)
        self.load_data.place(x=530, y=100,width=730,height=530)
        #searchFrame
        self.search_data = LabelFrame(self.load_data,
                                font=("arial",14,"bold"),
                                border=11,relief = tk.GROOVE
                                ,bg="lightgrey",foreground="black")
        self.search_data.place(x=0,y=0,width=700,height=80)
        #=====Database Frame=============
        self.data_Frame = LabelFrame(self.load_data,bd=12,bg="white",relief = tk.GROOVE)
        self.data_Frame.place(x=0, y=100,width=700,height=400)
       #=============Pack============
        self.user_title.pack(side = tk.TOP,fill=tk.BOTH)
        #============Entry===========
        self.studentId = Label(self.detail_Frame,text="Student ID",bd=7,font=("arial",17),bg="lightgrey")
        self.studentId.grid(row=0,column=2,padx=0,pady=4)
        
        self.studentId_input = Entry(self.detail_Frame,bd=7,font=("arial",14))
        self.studentId_input.grid(row=0,column=3,padx=2,pady=2)
        #Name
        self.studentName = Label(self.detail_Frame,text="Student Name",bd=7,font=("arial",17),bg="lightgrey")
        self.studentName.grid(row=1,column=2,padx=0,pady=4)
        
        self.studentName_input = Entry(self.detail_Frame,bd=7,font=("arial",14))
        self.studentName_input.grid(row=1,column=3,padx=2,pady=2)
        #class
        self.studentClass = Label(self.detail_Frame,text="Student Class",bd=7,font=("arial",14),bg="lightgrey")
        self.studentClass.grid(row=2,column=2,padx=0,pady=4)
        
        self.studentClass_input = Entry(self.detail_Frame,bd=7,font=("arial",14))
        self.studentClass_input.grid(row=2,column=3,padx=2,pady=2)
        #BirdDay
        self.brirth = Label(self.detail_Frame,text="Date of birth",bd=7,font=("arial",14),bg="lightgrey")
        self.brirth.grid(row=3,column=2,padx=0,pady=4)
        
        self.brirth_input = Entry(self.detail_Frame,bd=7,font=("arial",14))
        self.brirth_input.grid(row=3,column=3,padx=2,pady=2)
        #place of bird
        self.Place = Label(self.detail_Frame,text="Place of birt",bd=7,font=("arial",14),bg="lightgrey")
        self.Place.grid(row=4,column=2,padx=0,pady=4)
        
        self.Place_input = Entry(self.detail_Frame,bd=7,font=("arial",14))
        self.Place_input.grid(row=4,column=3,padx=2,pady=2)
        #Contact
        self.Contact = Label(self.detail_Frame,text="Contact",bd=7,font=("arial",14),bg="lightgrey")
        self.Contact.grid(row=5,column=2,padx=0,pady=4)
        
        self.Contact_input = Entry(self.detail_Frame,bd=7,font=("arial",14))
        self.Contact_input.grid(row=5,column=3,padx=2,pady=4)
        #Name of contact person
        self.PersonC = Label(self.detail_Frame,text="Name of contact person",bd=7,font=("arial",14),bg="lightgrey")
        self.PersonC.grid(row=5,column=2,padx=0,pady=4)
        
        self.PersonC_input = Entry(self.detail_Frame,bd=7,font=("arial",14))
        self.PersonC_input.grid(row=5,column=3,padx=2,pady=4)
        #commbox Gender
        self.Gender = Label(self.detail_Frame,text="Gender",bd=7,font=("arial",14),bg="lightgrey")
        self.Gender.grid(row=6,column=2,padx=0,pady=4)
        self.Gender = Combobox(self.detail_Frame,font=("arial",14))
        self.Gender['values'] = ("Males","Female")
        self.Gender.grid(row=6,column=3,padx=1,pady=4)
        
        #
        #===============button===================
        #add
        self.btn_add = Button(self.arial_Frame,text="Add",bd=7,font=("arial",14),bg="lightgrey",width=14,command=click)
        self.btn_add.grid(row=0,column=1,padx=1,pady=4)
    
        
        
        
        #Update
        self.btn_update = Button(self.arial_Frame,text="Update",bd=7,font=("arial",14),bg="lightgrey",width=14)
        self.btn_update.grid(row=0,column=2,padx=30,pady=4)
        #Delect
        self.btn_delect = Button(self.arial_Frame,text="Delect",bd=7,font=("arial",14),bg="lightgrey",width=14)
        self.btn_delect.grid(row=1,column=1,padx=1,pady=10)
        #clear
        self.btn_clear = Button(self.arial_Frame,text="Clear",bd=7,font=("arial",14),bg="lightgrey",width=14)
        self.btn_clear.grid(row=1,column=2,padx=30,pady=10)
        #================Search================
        #lable
        self.search_lbl = Label(self.search_data,text="Search",bd=7,font=("arial",14),bg="lightgrey")
        self.search_lbl.grid(row=0,column=0,padx=0,pady=5)
        #input
        self.sear_input = Combobox(self.search_data,font=("arial",14),width=20)
        self.sear_input['values'] = ("Student ID",
                                 "Student Name",
                                 "Student Class",
                                 "Date of birth",
                                 "Place of birt"
                                 "Contact",
                                 "Name of contact person",
                                 "Gender")
        self.sear_input.grid(row=0,column=2,padx=3,pady=5)
        #button
        self.sear_btn = Button(self.search_data,text="Search",bd=7,font=("arial",14),bg="lightgrey",width=13)
        self.sear_btn.grid(row=0,column=4,padx=4,pady=5)
        
        self.show_btn = Button(self.search_data,text="ShowAll",bd=7,font=("arial",14),bg="lightgrey",width=13)
        self.show_btn.grid(row=0,column=5,padx=4,pady=5)
        
        #===========database==================
        self.y_croll = Scrollbar(self.data_Frame,orient= tk.VERTICAL)
        self.x_croll = Scrollbar(self.data_Frame,orient= tk.HORIZONTAL)
        
        #columm
        self.student_table = Treeview(self.data_Frame,columns=(
                                "Student ID",
                                 "Student Name",
                                 "Student Class",
                                 "Date of birth",
                                 "Place of birt",
                                 "Contact",
                                 "Name of contact person",
                                 "Gender"),yscrollcommand= self.y_croll.set,xscrollcommand=self.x_croll.set)
        self.student_table.pack(fill=tk.BOTH,expand=True)
        #heading
        self.student_table.heading("Student ID",text="Student ID")
        self.student_table.heading("Student Name",text="Student Name")
        self.student_table.heading("Student Class",text="Student Class")
        self.student_table.heading("Date of birth",text="Date of birth")
        self.student_table.heading("Place of birt",text="Place of birt")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("Name of contact person",text="Name of contact person")
        self.student_table.heading("Gender",text="Gender")
        
        self.student_table['show'] = 'headings' # ccot dau tien khong con nua
        
        self.student_table.column("Student ID",width=100)
        self.student_table.column("Student Name",width=100)
        self.student_table.column("Student Class",width=100)
        self.student_table.column("Date of birth",width=100)
        self.student_table.column("Place of birt",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("Name of contact person",width=100)
        self.student_table.column("Gender",width=100)
        
        
        #=========config scroll===============
        
        self.y_croll.config(command=self.student_table.yview)
        self.x_croll.config(command=self.student_table.xview)
        
        self.y_croll.pack(side=tk.RIGHT,fill=tk.Y)
        self.x_croll.pack(side=tk.BOTTOM,fill=tk.X)

    
    
        
        
if __name__ == '__main__':
    main()    
        
        
    
