from PyPDF2 import PdfWriter

f = PdfWriter()
pdfs = []

n = int(input("How many pdf do you want to merge\n")) 

for i in range(0,n):
  name= input((f"Enter the name the pdf {i + 1} : "))
  pdfs.append(name)

for pdf in pdfs:
  f.append(pdf)

f.write("Merged_pdf.pdf")
f.close()