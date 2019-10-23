# Import all needed libraries 
import os
import glob
from bs4 import BeautifulSoup
import pdfkit


# For loop to iterate over all files in the specified directory

for filename in glob.glob("//path/to/html/files/*.htm"):

    # Begin parsing HTML files using BeautifulSoup
    
    f = open(filename, "r")
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    
    # Filter HTML Doc to find Control number 
    
    div = soup.find('div', class_='returns-middle')
    td_list = div.find_all("td")
    
    # Variables for naming converted HTML files 
    
    newName = td_list[1].text
    
    # Change directory to save the converted HTML file
    
    os.chdir("\\\\path\\to\\save\\PDFs")  
    pdfname = "Naming scheme#" + newName + ".pdf"
    
    # Set options for PDF conversion
    options = {
    'zoom': '1.10',
    'margin-top': '0.50in',
    'margin-right': '0.50in',
    'margin-bottom': '0.50in',
    'margin-left': '0.50in',
    }
    
    # Begin logic to determine if file exists
    
    if os.path.isfile(str(pdfname)):
        print(pdfname + "exists")
            
    else:
        pdfkit.from_file(str(filename), str(pdfname), options=options)
