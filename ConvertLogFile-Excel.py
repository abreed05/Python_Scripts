import os
import re
import csv
import openpyxl

# Define Delete CSV File
def delCSV():
    del_csv = "Windows\\Path\\TO\\CSV"
    if os.path.isfile(del_csv):
        os.remove(del_csv)
# Define Delete XLSX Files
def delXlsx():
    del_xlsx = "Windows\\Path\\To\\xlsx"
    if os.path.isfile(del_xlsx):
        os.remove(del_xlsx)
# Function to fix IP formating in log file
def fixIp():
    path = "Windows\\Path\\To\\Log"
    with open(path, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('IP Address', 'IPAddress')
    with open(path, 'w') as file:
        file.write(filedata)
# Function to fix MAc address in log file
def fixMac():
    path = "Windows\\Path\\To\\log"
    with open(path, 'r') as file:
        filedata = file.read()
    filedata = filedata.replace('MAC Address', 'MACAddress')
    with open(path, 'w') as file:
        file.write(filedata)
# Function to clean up text and data within log file
def fixTxt():
    path = "Windows\\Path\\To\\log"
    with open(path) as f:
        for line in f:
            if not line.isspace():
                clean = re.sub("\s+", ",", line.strip())
                outfile = "Windows\\Path\\To\\log"
                with open(outfile, 'a') as l:
                    l.write(clean + '\n')
                    
# Function to convert the CSV file to XLSX for better data control
def txtToXlsx():
    filepath_in = "Windows\\Path\\To\\CSV"
    filepath_out = "Windows\\Path\\To\\XLSX"
    wb = openpyxl.Workbook()
    ws = wb.active
    with open(filepath_in) as file_xlsx:
        reader = csv.reader(file_xlsx, delimiter=',')
        for row in reader:
            ws.append(row)
    wb.save(filepath_out)

delCSV()
delXlsx()
fixIp()
fixMac()
fixTxt()
txtToXlsx()
