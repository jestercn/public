import PyPDF2
import os
print("*"*50)
print("PDF文件按页码截取部分页面")
print("*"*50)
fname = input('请输入文件名 :> ')
pdfFileObj = open(fname,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfWriter = PyPDF2.PdfFileWriter()
start = int(input('请输入开始页码:>'))-1
end = int(input('请输入结束页码:>'))
for num in range(start,end):
    pageObj= pdfReader.getPage(num)
    pdfWriter.addPage(pageObj)
pdfOutput = open('result.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
pdfFileObj.close()
os.system("pause")