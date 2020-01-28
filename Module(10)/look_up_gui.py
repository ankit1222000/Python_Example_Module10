import pickle
#from tkinter import *
import random
import tkinter
class contact:
    def __init__(self,n,e,p):
        self.name=n
        self.phone=p
        self.email=e
    def get(self,n,e,p):
        self.name=n
        self.phone=p
        self.email=e
    def set(self):
        print("name: ",self.name)
        print("phone number: ", self.phone)
        print("email: ", self.email)

def add(c):
    j=0
    global d
    global l
    print("Enter Data")
    window = tkinter.Tk()
    window.title("Look Up")
    window.geometry("500x400")
    l1=tkinter.Label(window,text="Name  ").grid(row=0,column=0)
    name = tkinter.Entry(window).grid(row=0,column=1)
    l2=tkinter.Label(window, text="Contact  ").grid(row=1, column=0)
    phone = tkinter.Entry(window).grid(row=1,column=1)
    l3=tkinter.Label(window, text="Email  ").grid(row=2, column=0)
    email = tkinter.Entry(window).grid(row=2,column=1)
    c.get(name, email, phone)           #object
    d1=dict()
    l.append(j)
    d1[j]=c
    d[j] = d1
def write(file_write,c):
    global d
    for i in l:
        d=pickle.dump(d[i],file_write)
        #file_write.write(str(d[i]))
    file_write.close()
def read(file_read):
    global r
    file_read=open("update.txt","rb")
    d2=dict()
    d2=pickle.load(file_read)
    print(d2[0].name)
    print(d2[0].phone)
    print(d2[0].email)
def update(file_write,c):
    j=0
    d=dict()
    l=[]
    file_write = open("update.txt", "wb")
    print("Enter new Data")
    name = input("enter name ")
    phone = input("enter phone ")
    email = input("enter email ")
    c.get(name, email, phone)
    d1 = dict()
    l.append(j)
    d1[j] = c
    d[0] = d1
    for i in l:
        d = pickle.dump(d[i], file_write)
        # file_write.write(str(d[i]))
    file_write.close()
    c.set()
    file_write.close()
c=contact("","","")
d=dict()
l=[]
r=0
file_write=open("object.txt","wb")
file_read=open("object.txt","rb")
print("add data before writing")
while(True):
    print("1. Write File ")
    print("2. Read File ")
    print("3. Update File ")
    print("4. Add Data")
    print("5. Exit")
    i=int(input("Enter Choice "))
    if i==1:
        update(file_write,c)
    elif i==2:
        read(file_read)
    elif i==3:
        update(file_write,c)
    elif i==4:
        add(c)
    elif i==5:
        exit(0)
window.mainloop()