from tkinter import *
from textblob import TextBlob
import textblob
def  clearAll():
    word1_feild.delete(0,END)
    word2_feild.delete(0,END)
def correction():
    input_Word=word1_feild.get() 
    blobObj=TextBlob(input_Word)
    corrected_Word=str(blobObj.correct())
    word2_feild.insert(10,corrected_Word)
if __name__=="__main__":
    root=Tk()
    root.configure(background="lightgreen")
    root.geometry("400x150")
    root.title("spellingCorrector")
    headlabel=Label(root,text="Welcome To The Spelling Correcction App",fg="black",bg="red")
    headlabel.grid(row=0,column=1)
    label1=Label(root,text="Input Word",fg="black",bg="dark green")
    label2=Label(root,text="Corrected Word",fg="black",bg="dark green")
    label1.grid(row=1,column=0)
    label2.grid(row=3,column=0,padx=10)
    word1_feild=Entry()
    word2_feild=Entry()
    word1_feild.grid(row=1,column=1,padx=10,pady=10)
    word2_feild.grid(row=3,column=1,padx=10,pady=10)
    button1=Button(root,text="Correction",bg="red",fg="black",command=correction)
    button1.grid(row=2,column=1)
    button2=Button(root,text="Clear",bg="red",fg="black",command=clearAll)
    button2.grid(row=4,column=1)
    root.mainloop()