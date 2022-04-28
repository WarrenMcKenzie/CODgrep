import requests
from urllib.parse import urljoin
import urllib.request
import os  

CIFs = list(map(int, input("Enter the CIF numbers with spaces or line breaks between them: ").split()))
idents = list(map(str, input("Enter the names of the files to be retrieved in the same order with spaces or line breaks between them: ").split()))
for i, x in enumerate(CIFs):
    baseUrl = ['http://www.crystallography.net/cod/']
    cifNum = list(str(x))
    cifExt = ['.cif']
    urlComp = baseUrl + cifNum + cifExt
    finalUrl = "".join(urlComp)
    #name of the file
    #minName = input("What is the identity of {}.cif".format(x))
    minName = idents[i]
    numName = int(''.join(map(str, cifNum))) # concatenates cif number
    fileComp = minName + "_" + str(numName) + str(cifExt[0])
    finalName = "".join(fileComp)
    urllib.request.urlretrieve(finalUrl, finalName)
    
print("Finished")
