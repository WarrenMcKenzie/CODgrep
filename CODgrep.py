import requests
from urllib.parse import urljoin
import urllib.request
import numpy as np
import os  
import re
import time

CIFs = list(map(int, input("Enter the CIF numbers with spaces or line breaks between them: ").split()))
for i, x in enumerate(CIFs):
    baseUrl = ['http://www.crystallography.net/cod/']
    cifNum = list(str(x))
    cifExt = ['.cif']
    urlComp = baseUrl + cifNum + cifExt     
    finalUrl = "".join(urlComp)             # Assembles the final URL
    
    if np.size(CIFs) > 60                   # Flood control, per crystallography.net API
        time.sleep(10)                      # documentation for SQL queries
    
    # Name is pulled from the .cif information page
    
    nameExt = ['.html']                     # The COD is set up so the difference is the extension
    urlComp = baseUrl + cifNum + nameExt
    finalUrlName = "".join(urlComp)
    namePull = requests.get(finalUrlName, 'html.parser')
    nameText = namePull.text # renders page
    nameFlat = "".join(nameText.split())    # Makes everything a monolithic block of text
    minName = re.search(r'Mineralname</th><td>(.*?)</td>', nameFlat).group(1) # Pulls the mineral name
    
    numName = int(''.join(map(str, cifNum))) # concatenates cif number
    fileComp = minName + "_" + str(numName) + str(cifExt[0])
    finalName = "".join(fileComp)
    urllib.request.urlretrieve(finalUrl, finalName)
    
print("Finished")
