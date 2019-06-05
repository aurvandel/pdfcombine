from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader

pdfs = ['1.pdf', '2.pdf', '3.pdf', '4.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as fout:
    merger.write(fout)

