from Tkinter import *
import tkFileDialog as filedialog
from tkFileDialog import askopenfilename
import PyPDF2
from PyPDF2 import PdfFileReader
import webbrowser as wb
import os
def donothing():
   root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files",".pdf"),("all files",".*")))
   fichier = open(root.filename, "wb")
#    wb.open_new(root.filename)
#    pdfRead=PyPDF2.PdfFileReader(fichier)
#    page =pdfRead.getPage(0)
#    pageContent=page.extractText()
   champ_label2 = Label(root,text=fichier.write(" kokokokokok"))
   champ_label2.pack()
   
  
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
