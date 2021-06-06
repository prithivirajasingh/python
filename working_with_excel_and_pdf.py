import csv
import PyPDF2
import re
import openpyxl

file = open('find_the_link.csv','r',encoding='utf-8')
cr = csv.reader(file)
data_lines = list(cr)

text = ''
for index,items in enumerate(data_lines):
#     print(items[index])
    text = text + items[index]

print(text)

file = open('Find_the_Phone_Number.pdf','rb')
pattern = r'\d\d\d.\d\d\d.\d\d\d\d'
pr = PyPDF2.PdfFileReader(file)

for page_num in range(pr.numPages):
    pdfpage = pr.getPage(page_num)
    content = pdfpage.extractText()
    match = re.findall(pattern, content)
#     print(match)
    if match != []:
        print('Page: ' + str(page_num + 1))
        print(match)
        break
