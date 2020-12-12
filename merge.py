from PyPDF2 import PdfFileMerger
import os
#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']
pdf_folder = 'C:/Users/Riyad Hossain/Desktop/portfolio/portfolio/portfolio/result/Chapter3'
result_folder = 'C:/Users/Riyad Hossain/Desktop/portfolio/portfolio/portfolio/result/'
prep_folder = 'prep/'
merger = PdfFileMerger()


folder_names = []
pdf_files = []

for folder in os.listdir(result_folder):
    folder_names.append(folder)

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        pdf_files.append(os.path.join(pdf_folder, file))
        
for folder in folder_names:
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(prep_folder + folder + '.pdf')
merger.close()