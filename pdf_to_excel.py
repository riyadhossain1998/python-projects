#pip install tika, xlwt
#pip install tabula, openpyxl
#pip install pandas, xlrd

from tika import parser
from tabula import read_pdf , convert_into#
import pandas as pd
import math
def main():
    tabula()

def tika(): # General Text
    
    raw = parser.from_file("PDF_TEST.pdf")
    print(raw['content']) # Content of pdf

def tabula():
    #table1 = read_pdf("test.pdf", pages=1, guess=False)
    #table2 = convert_into("test.pdf", "test1.csv", output_format="csv")
    table3 = pd.read_csv("nourish.csv", thousands=',')
    table31 = pd.DataFrame(table3)
    #print(table31.columns)
    #df = pd.DataFrame(table1)
    name_list = []
    id_list = []
    for i in table31['Id # Name']: # Splitting this column
        try:
            text = i
            
            id_list.append(text[0:3])
            name_list.append(text[4:])
        
            #print(num[4:])
            
        except:
            break
    date = table31['Order Dt'][0]
    total_value = table31['Value'][len(name_list)-1] 
    total_qty = table31['Order Qty'][len(name_list)-1]

    table32 = table31.drop(columns=['Order Dt', 'Id # Name', 'Unnamed: 2']) # Dropping NaN/Incorrect columns 
    table33 = pd.DataFrame(list(zip(id_list,name_list)), 
              columns=['ID','Name']) # Splitting 'Id # Name' into two columns
    table34 = pd.concat([table33, table32], axis=1) # merging table33 and table32 id and name to the rest of the data 
    
    # Reformatting commas using lambda functions
    table34['Value'] = table34.apply(lambda x: "{:,}".format(x['Value']), axis=1) 
    table34['Order Qty'] = table34.apply(lambda x: "{:,}".format(x['Order Qty']), axis=1) 
    
    # Removing Decimal places (2.0 to 2)
    table34['Ord #'] = table34['Ord #'].map('{0:g}'.format)
    table34['Unit'] = table34['Unit'].map('{0:g}'.format) 
    table34['Nod'] = table34['Nod'].map('{0:g}'.format)
    

    table34.to_excel('excel_test.xlsx') #  loop to write to different sheets
    print(date)
    print(total_qty, total_value)
    print(table34)
if __name__ == "__main__":
    main()
