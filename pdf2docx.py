from pdf2docx import Converter
pdfFile = "pdfFile.pdf"
docxFileName = "nameOfDocxFile.docx"
cv = Converter(pdfFile)
cv.convery(docxFileName)
cv.close()