import PyPDF4
import re



def formatPage(page):
	newPage = page.replace('˜',"fi") #PyPDF replaces some groups of characters, so this statement "counter-replaces" the replacement.
	brackets = re.findall(r'\[\d+[,\s\d+]*\]', page) # the following code removes the citation brackets. 
	if brackets:
		for cite in brackets:
			newPage = newPage.replace(cite,'') 
	#pageArray = newPage.split('.')
	return newPage.replace('\n','')

def getIntroduction(pdfReader):
	for 

pdfFileObj = open('CAM4-4-1884.pdf', 'rb')
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)
page1Obj = pdfReader.getPage(0)
page1 = page1Obj.extractText()

page2 = formatPage(page1)
print(page2)



