# Lists all the attributes of a python file
# import sqlite3
import os
import pandas
import shutil
from PyPDF2 import PdfFileReader, PdfFileWriter
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
def folder_summariser(path,filename):
    l = []
    for folder, f, files in os.walk(path):
        for file in files:
            d = {}
            d["Filename"] = os.path.join(file)
            d["Filepath"] = os.path.join(folder,file)
            l.append(d)
    Data = pandas.DataFrame(l)
    f = filename + ".xlsx"
    Data.to_excel(path+"/"+f)
def extract_page_pdf(path,pdf,pages, filename):      
    pdf = PdfFileReader(pdf)
    pdfWriter = PdfFileWriter()
    for page_num in pages:
        pdfWriter.addPage(pdf.getPage(page_num-1))
    v = path+"/"+filename+".pdf"
    with open(v, 'wb') as f:
        pdfWriter.write(f)
        f.close()
def multiple_extract(folderpdf,pdfs,pages,path,filename,filenameadd):
    if filenameadd != "":
        pdfWriter = PdfFileWriter() 
        for file, filee in zip(folderpdf,pdfs):
            texted = io.BytesIO() #creating the new next page file with file name.
            can = canvas.Canvas(texted, pagesize=letter)
            can.drawString(100, 10, filee)
            can.save()
            texted.seek(0)
            newtext = PdfFileReader(texted)
            pdfed = PdfFileReader(file)
            for page_num in pages:
                page = pdfed.getPage(page_num-1)
                page.mergePage(newtext.getPage(0))
                pdfWriter.addPage(pdfed.getPage(page_num-1))
        filename =path+'/'+filename+".pdf"
        with open(filename, 'wb') as f:
            pdfWriter.write(f)
            f.close()
    else:
        pdfWriter = PdfFileWriter()  
        for p in pdfs:                
            pdfed = PdfFileReader(p)        
            for page_num in pages:
                pdfWriter.addPage(pdfed.getPage(page_num-1))
        l=''
        for i in pages:
            l=l+str(i) 
        filename =path+"/"+filename+".pdf"
        with open(filename, 'wb') as f:
            pdfWriter.write(f)
            f.close()
def file_type_extractor(ext, path, text,skip,foldername):
    targ = foldername
    os.mkdir(path+targ)
    targg= "/" +targ+"/"
    file_list = []
    path_list = []
    l = []
    originn = []
    targett = []
    for paath, directories, files in os.walk(path):        
            for file in files:    
                file_list.append(os.path.join(file))
                path_list.append(os.path.join(paath,file))
                if text != "":                    
                    if file.endswith(ext) and text in file:
                        d = {} 
                        d["Filename"] = os.path.join(file)
                        d["Filepath"] = os.path.join(paath,file)
                        l.append(d)
                        i = file_list.index(file)
                        originn.append(path_list[i])
                        targett.append(path+targg+file)
                    else:
                        pass
                else:
                    if file.endswith(ext):
                        d = {} 
                        d["Filename"] = os.path.join(file)
                        d["Filepath"] = os.path.join(paath,file)
                        l.append(d)
                        i = file_list.index(file)
                        originn.append(path_list[i])
                        targett.append(path+targg+file)
                    else:
                        pass
    i = 0
    vv= []
    if skip !="":
        skiped=int(skip)
        v = originn[0:len(originn):skiped]
        b = targett[0:len(originn):skiped]
        ll = l[0:len(originn):skiped]
    else:
        v = originn[0:len(originn)]
        b = targett[0:len(originn)]
        ll = l[0:len(originn)]
    for a, c in zip(v,b):
        shutil.copyfile(a, c)
    Data = pandas.DataFrame(ll)
    target = path+targg
    Data.to_excel(target + "Folder summary.xlsx")

# Function 5
# """ E. Excel Extract """
# def excel_extract: