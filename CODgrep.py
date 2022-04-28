import requests
from urllib.parse import urljoin
import urllib.request
import os  

# CIFs and Idents takes the numbers of the identified CIF files and the names you have assigned them.
# For this reason it's easiest to create the list of files you need in Excel or something similar,
# so that you can just copy/paste an entire column/row. This should be OS independent and saves to
# your default download folder

CIFs = list(map(int, input("Enter the CIF numbers with spaces or line breaks between them: ").split())) #
idents = list(map(str, input("Enter the names of the files to be retrieved in the same order with spaces or line breaks between them: ").split()))

for i, x in enumerate(CIFs):

    # location of the file 
    
    baseUrl = ['http://www.crystallography.net/cod/']
    cifNum = list(str(x))
    cifExt = ['.cif']                                   # url extension
    urlComp = baseUrl + cifNum + cifExt                 # assembles URL from parts
    finalUrl = "".join(urlComp)                         # merges full URL
    
    # name of the file
    
    minName = idents[i]                                 # pulls the mineral name from idents
    numName = int(''.join(map(str, cifNum)))            # concatenates cif number
    fileComp = minName + str(numName) + str(cifExt[0])  # assembles file name from parts
    finalName = "".join(fileComp)                       # merges full filename
    urllib.request.urlretrieve(finalUrl, finalName)     # downloads and saves the file
