import PyPDF2

merger=PyPDF2.PdfMerger()

pdfs=["PDF MERGER/2.pdf",]

for filename in pdfs:
    pdffile=open(filename,"rb")
    pdfreader=PyPDF2.PdfReader(filename)
    merger.append(pdfreader)
pdffile.close()
merger.write("merge.pdf")    