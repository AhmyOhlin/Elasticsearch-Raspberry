import csv
from datetime import datetime
import os
import time
from collections import OrderedDict
from time import sleep

    
Datum = time.strftime("%Y-%m-%d")
Time = datetime.now().replace(microsecond=0).isoformat()

data = {'Stromzaehler Strom L1 [A]': '0.0','Stecker Energy': '2.37', '1OG Ultraviolet': '0.0','Stecker EG  Energie [kWh]': '4.3'}

filename = Datum + 'SOF.csv'
if not os.path.isfile(filename):
    outfile = open(filename, "w")
    lineKey = ""
    for x in data.keys():
        lineKey+= x + ","
    lineKey = 'Time '+ "," + lineKey[:-1]+"\n" # Delete last character and add new line
    outfile = open(filename, "a")
    outfile.write(lineKey)
    outfile.close()
    
#check first line of  fieldnames
with open(filename,'r') as myFile:
    reader = csv.DictReader(myFile)
    fieldnames = reader.fieldnames
    print(len(fieldnames), fieldnames)
    myFile.close()

#Compare the values with their  keys (fieldnames)
with open(filename,'a') as outfile:
    writer = csv.DictWriter(outfile, fieldnames)
    row = {}
    for fieldname in fieldnames:
        row[fieldname] = data.get(fieldname, "n/a")
    row["Time "] = Time
    writer.writerow(row)
 