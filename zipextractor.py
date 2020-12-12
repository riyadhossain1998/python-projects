import os
import zipfile

zip_folder = 'C:/Users/Riyad Hossain/Desktop/portfolio/portfolio/portfolio/zips/'
#zip_directory = 'C:/Users/Riyad Hossain/Desktop/portfolio/portfolio/portfolio/zips/Chapter3.zip'
extract_directory = 'C:/Users/Riyad Hossain/Desktop/portfolio/portfolio/portfolio/result/'
path_to_zip_file = 'C:/Users/Riyad Hossain/Desktop/portfolio/portfolio/portfolio/result/C5/Chapter3.pdf'

all_file = []


for file in os.listdir(zip_folder):
    if file.endswith(".zip"):
        all_file.append(os.path.join(zip_folder, file))

for i in all_file:
    with zipfile.ZipFile(i, 'r') as zip_ref:
        list_of_files = zip_ref.namelist()
        if i[-6] == '1':                              
            zip_ref.extractall(extract_directory + i[-13:-4])               # Files from zip extracted
        else:
            zip_ref.extractall(extract_directory + i[-12:-4]) 
        



#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']




