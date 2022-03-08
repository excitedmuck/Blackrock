# """"
# BlackRocks!!
# """ 
from tkinter import *
import backend
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger 
def summarise():
    filename = entcol9[0].get()
    path_text = entcol1[0].get()
    backend.folder_summariser(path_text,filename)
def page_handler(pagen):
    pag = pagen.get().split(",")
    l = []
    for i in pag:
        l.append(int(i))
    return l
def extract():
    filename = entcol9[1].get()
    pageno = entcol3[0]
    pageo = pageno.get().split(",")
    file = entcol1[1].get().split("/")[-1]
    path = (entcol1[1].get().split("/")[1:-1])
    filepath = ''
    for i in path:
        filepath += "/"+i
    pages = []
    for i in pageo:
        try:
            pages.append(int(float(i)))
        except:
            "fd"
    backend.extract_page_pdf(filepath, entcol1[1].get(), pages,filename)
def multiextract():
    filename = entcol9[2].get()
    skipfile = entcol5[0]
    folder = entcol1[2].get()
    pageno1 = entcol3[1]
    filenameadd = entcol7[0].get()
    folderlist = os.listdir(folder)
    folderpdf = []
    pdfs =[]
    for p in folderlist:
        if p.endswith(".pdf"):
            pdfs.append(p)
            folderpdf.append(folder+p)
        else:
            pass
    pdflistcc = folderpdf
    if skipfile.get()!="":
        folderpdf = []
        skip = int(skipfile.get())
        i = 0        
        for l in pdflistcc:
            pdfs.append(l)
            folderpdf.append(pdflistcc[i+skip])
    else:
        pass
    backend.multiple_extract(folderpdf, pdfs, page_handler(pageno1),folder,filename,filenameadd)
def gather():
    path = entcol1[3].get()
    textstring = entcol3[2].get()
    skipfilefol = entcol5[1].get()
    filetype_text = entcol7[0].get()
    foldername = entcol9[3].get()
    backend.file_type_extractor(filetype_text,path,textstring,skipfilefol,foldername)
class windowclass:    
    def __init__(self,title):
        self.window = Tk()
        self.window.title(title)
    def modify_label(self,column_no, labels):
        rangerow = len(labels) 
        for t in range(rangerow):
            if labels[t] != "":
                v = Label(self.window, text = labels[t])
                v.grid(row = t, column = column_no)
            else:
                pass
    def modify_entry(self,column_no,entry,wid):
        t = 0
        d =[]
        for t in range(len(entry)):
            if entry[t] !="":
                vv=StringVar()
                d.append(vv)
                e=Entry(self.window,textvariable=vv,width = wid)
                e.grid(row=t,column=column_no)
            else:
                pass
        return d
    def modify_button(self,column_no, buttons, command):
        i = 0
        for t in range(len(buttons)):
            b4 = Button(self.window, text = buttons[t], width =12, command = command[t])
            b4.grid(row=t, column =column_no)
        pass
window1e = windowclass("Blackrocks")
window1e.modify_label(0,["Summarise folder", "Extract PDF Pages","Multiple PDF Extract", "Consolidate Files"])
window1e.modify_label(2,["", 'Page No.','Page No.','String',"",""])
window1e.modify_label(4,["","","Skip","Skip"])
window1e.modify_label(6,["","","Add name","Extension"])
window1e.modify_label(8,["File name", "File name","File name","Folder name"])
entry1 = ["hello","ewrw","asdfdsf","sdf"]
entry3 = ["", "hello","ewrw","asdfdsf"]
entry5 = ["","","Skip1","Skip2"]
entry7 = ["","","Filenameadd","Extension"]
entry9 = ["File name", "File name","File name","Folder name"]
entcol1 = window1e.modify_entry(1,entry1,20)
entcol3 = window1e.modify_entry(3,entry3,3)
entcol5 = window1e.modify_entry(5,entry5,3)
entcol7 = window1e.modify_entry(7,entry7,3)
entcol9 = window1e.modify_entry(9,entry9,6)
command = [summarise,extract,multiextract,gather]
window1e.modify_button(10,["summarise","extract","multi-extract","gather"], command)

# pyinstaller --onefile --windowed frontend.py
# export PYTHONPATH="${PYTHONPATH}:/Users/yashvinishukla/Library/Python/3.8/bin"
# import sys
# sys.path.append('/Users/yashvinishukla/Library/Python/3.8/bin')
