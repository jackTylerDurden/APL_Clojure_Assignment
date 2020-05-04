from tkinter import *
from tkinter import ttk

class MyForm:
    def __init__(self,window):        
        firstNameLabel = Label(window,text="First Name").grid(row=0,column=0)
        self.firstNameTextfield = Entry(window)
        self.firstNameTextfield.grid(row=0,column=1)
        lastNameLabel = Label(window, text="Last Name").grid(row=1,column=0)
        self.lastNameTextfield = Entry(window)
        self.lastNameTextfield.grid(row=1,column=1)
        btn = ttk.Button(window,command=self.submitButtonClick,text="Submit").grid(row=2,column=0)        

    def submitButtonClick(self):        
        msg="Thank you "+self.firstNameTextfield.get()+" for filling out this form"
        popup = Tk()
        popup.title("Submission Message")
        w = 400     # popup window width
        h = 200     # popup window height
        sw = popup.winfo_screenwidth()
        sh = popup.winfo_screenheight()
        x = (sw - w)/2
        y = (sh - h)/2
        popup.geometry('%dx%d+%d+%d' % (w, h, x, y))
        label = Label(popup,text=msg,width=120,height=10)
        label.pack()
        B1 = ttk.Button(popup,text="OK",command=popup.destroy,width=10)
        B1.pack()
        popup.mainloop()    

window = Tk()
MyForm(window)
window.title("Python Homework")
window.geometry('400x400')
window.mainloop()

