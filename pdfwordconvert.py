from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# Meminta input nama file PDF
pdf_file = input("Masukkan nama file PDF: ")

# Membuka file PDF
with open(pdf_file, 'rb') as pdf:
    # Membuat parser PDF
    parser = PDFParser(pdf)
    # Membuat PDF document
    doc = PDFDocument(parser)
    # Membuat resource manager
    rsrcmgr = PDFResourceManager()
    # Membuat string IO
    outfp = StringIO()
    # Membuat converter
    device = TextConverter(rsrcmgr, outfp, laparams=LAParams())
    # Membuat interpreter
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Selesaikan pembacaan setiap halaman PDF
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
    # Tutup file
pdf.close()

# Membuat file Word baru
with open(pdf_file.replace('.pdf', '.docx'), 'w') as word_file:
    # Menulis teks ke file Word
    word_file.write(outfp.getvalue())
    word_file.close()
outfp.close()

