import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from os import listdir

pdfs = [f for f in listdir()]
for file in pdfs:

    pdfname = file
    pdf = open(pdfname, 'rb')
    parsedpdf = PyPDF2.PdfFileReader(pdf)
    pages = parsedpdf.numPages
    count = 0
    text = ""

    while count < pages:
        pagecontent = parsedpdf.getPage(count)
        count += 1
        text += pagecontent.extractText()

    if text != "":
        text = text
    else:
        text = textract.process(fileurl, method='tesseract',language=ptbr)

    tokens = word_tokenize(text)
    lixo = ['(',')',';',':','[',']',',','.']
    stop_wordspt = stopwords.words('portuguese')
    stop_wordsen = stopwords.words('english')
    words = [word for word in tokens if not word in stop_wordspt and not word in stop_wordsen and not word in lixo]
    print(words)
