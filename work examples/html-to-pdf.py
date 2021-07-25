# Import all needed libraries, OS, Glob, BeautifulSoup, PDFKit
import os
import glob
from bs4 import BeautifulSoup
import pdfkit

# pdfConversion function. Code used to actually convert the HTML File 
def pdfConversion():
	os.chdir("Windows\\Path\\To\\Where\\To\\Create\\PDF")  
	pdfname = "DSW PO# " + newName + ".pdf"
    
    # Set options for PDF conversion
	options = {
	'zoom': '1.10',
	'margin-top': '0.50in',
	'margin-right': '0.50in',
	'margin-bottom': '0.50in',
	'margin-left': '0.50in',
	}
    
    # Begin logic to determin if file exists
    
	if os.path.isfile(str(pdfname)):
		print(pdfname + " exists")
            
	else:
		pdfkit.from_file(str(filename), str(pdfname), options=options)

# For loop to iterate over each html file specified in the glob filepath

for filename in glob.glob("Windows/Path/To'html_files/*.htm"):
	# open file for reading
	with open(filename, "r") as f:
		contents = f.read()
	# Convert html to BeautifulSoup Object
	soup = BeautifulSoup(contents, 'lxml')
	# Filter through HTML Soup object to find PO#
	divTag = soup.find_all('div', class_='returns-middle')
	# Create empty list
	pos = []
	# for loop to find all matching TD's within the div with class of returns-middle
	for tag in divTag:
		tdTags = tag.find_all("td")[1]
		# For loop to add found td's to an empty list called pos
		for tag in tdTags:
			pos.append(tag)
	# check length of list, if greater than or equal to 2 follow if branch 
	x = len(pos)
	if x >= 2:
		for item in pos:
			newName = item
			pdfConversion()

	else:
		newName = tdTags.text
		pdfConversion()
