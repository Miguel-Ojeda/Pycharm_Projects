# Script de prueba que extrae las observaciones de un PDF. En este caso las observaciones están en la segunda página.
# Modificación realizada desde PyCharm
# Modificación de Miguel
import PyPDF2
pdfFileObj = open('a.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(1)
texto = pageObj.extractText()
posObs = texto.find("OBSERVACIONES / INCIDENCIAS");
posEn = texto.find(" En ");
print(texto[posObs:posEn])