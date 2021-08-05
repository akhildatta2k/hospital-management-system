from tkinter import *
from tkinter import ttk
import random
import time
from datetime import date
from tkinter import messagebox
import mysql.connector as con






class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        self.nameOfTablets = StringVar()
        self.referenceNo = StringVar()
        self.dose = StringVar()
        self.noOfTablets = StringVar()
        self.lot = StringVar()
        self.issueDate = StringVar()
        self.expireDate = StringVar()
        self.dailyDose = StringVar()
        self.sideEffect = StringVar()
        self.furtherInformation = StringVar()
        self.bloodPressure = StringVar()
        self.storageAdvice = StringVar()
        self.medication = StringVar()
        self.patientId = StringVar()
        self.nhsNumber = StringVar()
        self.patientName = StringVar()
        self.dateOfBirth = StringVar()
        self.patientAddress = StringVar()
        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        # =================DataFrame==============
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)
        # =================Buttons Frame ==================
        Buttonframe = Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        # =================Details Frame ==================
        DetailsFrame = Frame(self.root,bd=10,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1530,height=190)
        # =================DataframeLeft ==================
        labelNameTablet = Label(DataframeLeft,text="Names of Tablet:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelNameTablet.grid(row=0,column=0)

        comNametablet = ttk.Combobox(DataframeLeft,textvariable=self.nameOfTablets,font=("arial",12,"bold"),width=33)
        comNametablet["values"] = ("Aspirine","Corona Vaccine","Dolo650","Cetrizine")
        comNametablet.grid(row=0,column=1)

        labelReference = Label(DataframeLeft,text="Reference No:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelReference.grid(row=1,column=0)
        txtReference = Entry(DataframeLeft,textvariable=self.referenceNo,font=("arial",12,"bold"),width=35,state=DISABLED)
        txtReference.grid(row=1,column=1)
        
        labelDose = Label(DataframeLeft,text="Dose:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelDose.grid(row=2,column=0)
        txtDose = Entry(DataframeLeft,textvariable=self.dose,font=("arial",12,"bold"),width=35)
        txtDose.grid(row=2,column=1)
        
        labelNoOfTablets = Label(DataframeLeft,text="No of Tablets:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelNoOfTablets.grid(row=3,column=0)
        txtNoOfTablets = Entry(DataframeLeft,textvariable=self.noOfTablets,font=("arial",12,"bold"),width=35)
        txtNoOfTablets.grid(row=3,column=1)
        
        labelLot = Label(DataframeLeft,text="Lot:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelLot.grid(row=4,column=0)
        txtLot = Entry(DataframeLeft,textvariable=self.lot,font=("arial",12,"bold"),width=35)
        txtLot.grid(row=4,column=1)
        
        
        labelIssueDate = Label(DataframeLeft,text="Issue Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelIssueDate.grid(row=5,column=0)
        txtIssueDate = Entry(DataframeLeft,textvariable=self.issueDate,font=("arial",12,"bold"),width=35)
        txtIssueDate.grid(row=5,column=1)
        
        labelExpDate = Label(DataframeLeft,text="Expire Date:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelExpDate.grid(row=6,column=0)
        txtExpDate = Entry(DataframeLeft,textvariable=self.expireDate,font=("arial",12,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)
        
        labelDailyDose = Label(DataframeLeft,text="Daily Dose:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelDailyDose.grid(row=7,column=0)
        txtDailyDose = Entry(DataframeLeft,textvariable=self.dailyDose,font=("arial",12,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)
        
        labelSideEffect = Label(DataframeLeft,text="Side Effect:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelSideEffect.grid(row=8,column=0)
        txtSideEffect = Entry(DataframeLeft,textvariable=self.sideEffect,font=("arial",12,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

        labelFurthurInfo = Label(DataframeLeft,text="Furthur Information:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelFurthurInfo.grid(row=0,column=2)
        txtFurthurInfo = Entry(DataframeLeft,textvariable=self.furtherInformation,font=("arial",12,"bold"),width=35)
        txtFurthurInfo.grid(row=0,column=3)
        
        labelBP = Label(DataframeLeft,text="Blood Pressure:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelBP.grid(row=1,column=2)
        txtBP = Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.bloodPressure,width=35)
        txtBP.grid(row=1,column=3)
       
        labelStorageAdvice = Label(DataframeLeft,text="Storage Advice:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelStorageAdvice.grid(row=2,column=2)
        txtStorageAdvice = Entry(DataframeLeft,textvariable=self.storageAdvice,font=("arial",12,"bold"),width=35)
        txtStorageAdvice.grid(row=2,column=3)
        
        labelMedication = Label(DataframeLeft,text="Medication:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelMedication.grid(row=3,column=2)
        txtMedication= Entry(DataframeLeft,textvariable=self.medication,font=("arial",12,"bold"),width=35)
        txtMedication.grid(row=3,column=3)
        
        labelPatientId = Label(DataframeLeft,text="Patient Id:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelPatientId.grid(row=4,column=2)
        txtPatientId = Entry(DataframeLeft,textvariable=self.patientId,font=("arial",12,"bold"),width=35,state=DISABLED)
        txtPatientId.grid(row=4,column=3)
        
        labelNHSNumber = Label(DataframeLeft,text="NHS Number:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelNHSNumber.grid(row=5,column=2)
        txtNHSNumber = Entry(DataframeLeft,textvariable=self.nhsNumber,font=("arial",12,"bold"),width=35,state=DISABLED)
        txtNHSNumber.grid(row=5,column=3)
        
        labelPatientName = Label(DataframeLeft,text="Patient Name:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelPatientName.grid(row=6,column=2)
        txtPatientName = Entry(DataframeLeft,textvariable=self.patientName,font=("arial",12,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)
       
        labelDOB = Label(DataframeLeft,text="Date of Birth:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelDOB.grid(row=7,column=2)
        txtDOB = Entry(DataframeLeft,textvariable=self.dateOfBirth,font=("arial",12,"bold"),width=35)
        txtDOB.grid(row=7,column=3)
        
        labelAddress = Label(DataframeLeft,text="Patient Address:",font=("times new roman",12,"bold"),padx=2,pady=6)
        labelAddress.grid(row=8,column=2)
        txtAddress = Entry(DataframeLeft,textvariable=self.patientAddress,font=("arial",12,"bold"),width=35)
        txtAddress.grid(row=8,column=3)

        # ===============DataframeRight===================
        self.textPrescription = Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.textPrescription.grid(row=0,column=0)
        # ===========================Buttons===============
        prescriptionBtn = Button(Buttonframe, bg="green", fg="white", text="Prescripiton",font=("arial",12,"bold"),width=24,height=2,padx=2,pady=2,command=self.iprescrption)
        prescriptionBtn.grid(row=0,column=0)
        
        prescriptionDataBtn = Button(Buttonframe, bg="green", fg="white", text="Prescripiton Data",font=("arial",12,"bold"),width=24,height=2,padx=2,pady=2,command=self.iPrescriptionData)
        prescriptionDataBtn.grid(row=0,column=1)
        
        updateBtn = Button(Buttonframe, bg="green", fg="white", text="Update",font=("arial",12,"bold"),width=24,height=2,padx=2,pady=2,command=self.update_data)
        updateBtn.grid(row=0,column=2)
        
        deleteBtn = Button(Buttonframe, bg="green", fg="white", text="Delete",font=("arial",12,"bold"),width=24,height=2,padx=2,pady=2,command=self.delete_data)
        deleteBtn.grid(row=0,column=3)
        
        clearBtn = Button(Buttonframe, bg="green", fg="white", text="Clear",font=("arial",12,"bold"),width=24,height=2,padx=2,pady=2,command=self.clear_data)
        clearBtn.grid(row=0,column=4)
        
        exitBtn = Button(Buttonframe, bg="green", fg="white", text="Exit",font=("arial",12,"bold"),width=24,height=2,padx=2,pady=2,command=self.exit_form)
        exitBtn.grid(row=0,column=5)
        # =======================================Table====================================
        # ==================================ScrollBar=====================================
        scroll_x = ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        # ==================================ScrollBar=====================================
        self.hospital_table = ttk.Treeview(DetailsFrame,column=("Name of Tablets","ref","dose","No of Tablets","Lot","Issue Date","Expire Date",
                                                                "Daily Dose","Side Effect","FurthurInfo","bp","storage",
                                                                "Medication","Patient Id","NHS Number","Patient Name","Date of Birth","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.hospital_table.heading("Name of Tablets",text="Tablets Name")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("No of Tablets",text="No of Tablets")
        self.hospital_table.heading("Lot",text="Lot")
        self.hospital_table.heading("Issue Date",text="Iss Date")
        self.hospital_table.heading("Expire Date",text="Exp Date")
        self.hospital_table.heading("Daily Dose",text="Daily Dose")
        self.hospital_table.heading("Side Effect",text="Effect")
        self.hospital_table.heading("FurthurInfo",text="Info")
        self.hospital_table.heading("bp",text="BP")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("Medication",text="Medication")
        self.hospital_table.heading("Patient Id",text="P.Id")
        self.hospital_table.heading("NHS Number",text="NHS Number")
        self.hospital_table.heading("Patient Name",text="P.Name")
        self.hospital_table.heading("Date of Birth",text="DOB")
        self.hospital_table.heading("Address",text="Address")
        self.hospital_table["show"] = "headings"
        
        
        self.hospital_table.column("Name of Tablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("No of Tablets",width=100)
        self.hospital_table.column("Lot",width=50)
        self.hospital_table.column("Issue Date",width=60)
        self.hospital_table.column("Expire Date",width=60)
        self.hospital_table.column("Daily Dose",width=100)
        self.hospital_table.column("Side Effect",width=80)
        self.hospital_table.column("FurthurInfo",width=80)
        self.hospital_table.column("bp",width=70)
        self.hospital_table.column("storage",width=60)
        self.hospital_table.column("Medication",width=100)
        self.hospital_table.column("Patient Id",width=60)
        self.hospital_table.column("NHS Number",width=100)
        self.hospital_table.column("Patient Name",width=100)
        self.hospital_table.column("Date of Birth",width=60)
        self.hospital_table.column("Address",width=100)
        self.hospital_table.pack(fill="both",expand=1)
        self.add_reference_number()
        self.fetch_data()
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        scroll_x  = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y  = ttk.Scrollbar(command=self.hospital_table.yview)
    # ===================================================Functionality Declaration===============================================================================
    def iprescrption(self):
        self.textPrescription.insert(END,"NHS Number:\t\t"+self.nhsNumber.get()+"\n")
        self.textPrescription.insert(END,"Reference Number:\t\t"+self.referenceNo.get()+"\n")
        self.textPrescription.insert(END,"Patient ID:\t\t"+self.patientId.get()+"\n")
        self.textPrescription.insert(END,"Patient Name:\t\t"+self.patientName.get()+"\n")
        self.textPrescription.insert(END,"Date Of Birth:\t\t"+self.dateOfBirth.get()+"\n")
        self.textPrescription.insert(END,"Address:\t\t"+self.patientAddress.get()+"\n")
        self.textPrescription.insert(END,"BP:\t\t"+self.bloodPressure.get()+"\n")
        self.textPrescription.insert(END,"Tablets:\t\t"+self.nameOfTablets.get()+"\n")
        self.textPrescription.insert(END,"NO of Tablets:\t\t"+self.noOfTablets.get()+"\n")
        self.textPrescription.insert(END,"Dose:\t\t"+self.dose.get()+"\n")
        self.textPrescription.insert(END,"Daily Dose:\t\t"+self.dailyDose.get()+"\n")
        self.textPrescription.insert(END,"Issue Date:\t\t"+self.issueDate.get()+"\n")
        self.textPrescription.insert(END,"Expire Date:\t\t"+self.expireDate.get()+"\n")
        self.textPrescription.insert(END,"BP:\t\t"+self.bloodPressure.get()+"\n")
        self.textPrescription.insert(END,"Side Effect:\t\t"+self.sideEffect.get()+"\n")
        self.textPrescription.insert(END,"Any Advice:\t\t"+self.storageAdvice.get()+"\n")
        self.textPrescription.insert(END,"Lot:\t\t"+self.lot.get()+"\n")


        


        
        

        

    def iPrescriptionData(self):
        if self.nameOfTablets.get() == "" or self.referenceNo.get()=="" or self.nhsNumber.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.dose.get() == "" or self.noOfTablets.get()=="" or self.lot.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.issueDate.get() == "" or self.expireDate.get()=="" or self.dailyDose.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.sideEffect.get() == "" or self.furtherInformation.get()=="" or self.bloodPressure.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.storageAdvice.get() == "" or self.medication.get()=="" or self.patientId.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.patientName.get() == "" or self.dateOfBirth.get()=="" or self.patientAddress.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        else:
            try:
                mydb = con.connect(host="localhost",user="root",password="",db="hospital")
                cursor = mydb.cursor()
                tb11=self.nameOfTablets.get()
                tb12=self.referenceNo.get()
                tb13=self.dose.get()
                tb14=self.noOfTablets.get()
                tb15=self.lot.get()
                tb16=self.issueDate.get()
                tb17=self.expireDate.get()
                tb18=self.dailyDose.get()
                tb19=self.sideEffect.get()
                tb21=self.furtherInformation.get()
                tb22=self.bloodPressure.get()
                tb23=self.storageAdvice.get()
                tb24=self.medication.get()
                tb25=self.patientId.get()
                tb26=self.nhsNumber.get()
                tb27=self.patientName.get()
                tb28=self.dateOfBirth.get()
                tb29=self.patientAddress.get()
                cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(str(tb11),str(tb12),str(tb13),str(tb14),str(tb15),str(tb16),str(tb17),str(tb18),str(tb19),str(tb21),str(tb22),str(tb23),str(tb24),str(tb25),str(tb26),str(tb27),str(tb28),str(tb29)))
                messagebox.showinfo("Success","Details Entered Successfully")
                mydb.commit()
                self.fetch_data()
                mydb.close()
            except con.Error as e:
                messagebox.showerror("Not Inserted",e)
    def fetch_data(self):
        try: 
            mydb = con.connect(host="localhost",user="root",password="",db="hospital")
            cursor = mydb.cursor()
            cursor.execute("select * from hospital")
            rows = cursor.fetchall()
            if len(rows) !=0:
                for record in self.hospital_table.get_children():
                    self.hospital_table.delete(record)
                for i in rows:
                    self.hospital_table.insert("",END,values=i)
                mydb.commit()
            mydb.close()
        except con.Error as e:
            messagebox.showerror("Failed",e)
    def add_reference_number(self):
        try: 
            mydb = con.connect(host="localhost",user="root",password="",db="hospital")
            cursor = mydb.cursor()
            cursor.execute("select * from hospital")
            rows = cursor.fetchall()
            rn=0
            if rows !=0:
                for row in rows:
                    rn=int(row[1])
                today = str(date.today())
                self.referenceNo.set(rn+1)
                self.patientId.set("REF0054"+str(rn+1)) 
                self.nhsNumber.set("NHS00845"+str(rn+1))
                self.lot.set("NO")
                self.sideEffect.set("NO")
                self.furtherInformation.set("Not Needed")
                self.bloodPressure.set("120||80")
                self.issueDate.set(today)                              
        except con.Error as e:
            messagebox.showerror("Failed",e)
    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        if cursor_row:
            content = self.hospital_table.item(cursor_row)
            row = content["values"]
            self.nameOfTablets.set(row[0])
            self.referenceNo.set(row[1])
            self.dose.set(row[2])
            self.noOfTablets.set(row[3])
            self.lot.set(row[4])
            self.issueDate.set(row[5])
            self.expireDate.set(row[6])
            self.dailyDose.set(row[7])
            self.sideEffect.set(row[8])
            self.furtherInformation.set(row[9])
            self.bloodPressure.set(row[10])
            self.storageAdvice.set(row[11])
            self.medication.set(row[12])
            self.patientId.set(row[13])
            self.nhsNumber.set(row[14])
            self.patientName.set(row[15])
            self.dateOfBirth.set(row[16])
            self.patientAddress.set(row[17])
        else:
            messagebox.showwarning("Warning","You Must Select The Row")

    def update_data(self):
        if self.nameOfTablets.get() == "" or self.referenceNo.get()=="" or self.nhsNumber.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.dose.get() == "" or self.noOfTablets.get()=="" or self.lot.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.issueDate.get() == "" or self.expireDate.get()=="" or self.dailyDose.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.sideEffect.get() == "" or self.furtherInformation.get()=="" or self.bloodPressure.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.storageAdvice.get() == "" or self.medication.get()=="" or self.patientId.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.patientName.get() == "" or self.dateOfBirth.get()=="" or self.patientAddress.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        else:    
            try:
                mydb = con.connect(host="localhost",user="root",password="",db="hospital")
                cursor = mydb.cursor()
                tb11=self.nameOfTablets.get()
                tb12=self.referenceNo.get()
                tb13=self.dose.get()
                tb14=self.noOfTablets.get()
                tb15=self.lot.get()
                tb16=self.issueDate.get()
                tb17=self.expireDate.get()
                tb18=self.dailyDose.get()
                tb19=self.sideEffect.get()
                tb21=self.furtherInformation.get()
                tb22=self.bloodPressure.get()
                tb23=self.storageAdvice.get()
                tb24=self.medication.get()
                tb25=self.patientId.get()
                tb26=self.nhsNumber.get()
                tb27=self.patientName.get()
                tb28=self.dateOfBirth.get()
                tb29=self.patientAddress.get()
                cursor.execute("UPDATE hospital SET name_of_tablets=%s,dose=%s,no_of_tablets=%s,lot=%s,issue_date=%s,expire_date=%s,daily_dose=%s,side_effect=%s,furthur_information=%s,blood_pressure=%s,storage=%s,medication=%s,patient_id=%s,nhs_number=%s,patient_name=%s,date_of_birth=%s,patient_address=%s WHERE reference_number=%s",(str(tb11),str(tb13),str(tb14),str(tb15),str(tb16),str(tb17),str(tb18),str(tb19),str(tb21),str(tb22),str(tb23),str(tb24),str(tb25),str(tb26),str(tb27),str(tb28),str(tb29),str(tb12)))
                mydb.commit()
                mydb.close()
                self.fetch_data()
                messagebox.showinfo("Success","Updated Successfully")

            except con.Error as e:
                messagebox.showerror("Failed",e)
    def clear_data(self):
        self.nameOfTablets.set("")
        self.dose.set("")
        self.noOfTablets.set("")
        self.lot.set("")
        self.issueDate.set("")
        self.expireDate.set("")
        self.dailyDose.set("")
        self.sideEffect.set("")
        self.furtherInformation.set("")
        self.bloodPressure.set("")
        self.storageAdvice.set("")
        self.medication.set("")
        self.patientId.set("")
        self.nhsNumber.set("")
        self.patientName.set("")
        self.dateOfBirth.set("")
        self.patientAddress.set("")
        self.add_reference_number()
        self.fetch_data()
        self.textPrescription.delete("1.0","200.0")

    def delete_data(self):
        if self.nameOfTablets.get() == "" or self.referenceNo.get()=="" or self.nhsNumber.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.dose.get() == "" or self.noOfTablets.get()=="" or self.lot.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.issueDate.get() == "" or self.expireDate.get()=="" or self.dailyDose.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.sideEffect.get() == "" or self.furtherInformation.get()=="" or self.bloodPressure.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.storageAdvice.get() == "" or self.medication.get()=="" or self.patientId.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        elif self.patientName.get() == "" or self.dateOfBirth.get()=="" or self.patientAddress.get()=="":
            messagebox.showerror("error","all credentials must be needed")
        else:
            try:
                mydb = con.connect(host="localhost",user="root",password="",db="hospital")
                cursor = mydb.cursor()
                tb12=str(self.referenceNo.get())
                cursor.execute("DELETE FROM hospital WHERE hospital.reference_number="+tb12)
                mydb.commit()
                self.fetch_data()
                messagebox.showinfo("Success","Record Deleted")

                mydb.close()
            except con.Error as e:
                messagebox.showerror(e)
    def exit_form(self):
        iexit = messagebox.askyesno("Hospital Management System","Are You Sure You Want To Ext")
        if iexit>0:
            root.destroy()
            return

        



        
root = Tk()
ob = Hospital(root)
root.mainloop()