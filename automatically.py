"""#!/usr/bin/env python"""
import homeassistant.remote as remote
import csv, json
from datetime import datetime
import threading
import os
import time
from collections import OrderedDict
from time import sleep
import threading
import ast

    
Datum = time.strftime("%Y-%m-%d")
Time = datetime.now().replace(microsecond=0).isoformat()
#print(Time)

api = remote.API('127.0.0.1', 'YOUR_PASSWORD')
entities = remote.get_states(api)
#print(entities)
tup = ("sourcenodeid", "interval", "previous", "exporting", "management" , "yr", "alarm")
data=  OrderedDict()
for entity in entities:
     if entity.entity_id.startswith('sensor') and all(elem not in entity.entity_id for elem in tup):
         list = remote.get_state(api, entity.entity_id)
         #print(list)
         #print('{}: {}'.format(list.attributes['friendly_name'], list.state))                 
         Eintrag = {list.attributes['friendly_name'] : list.state}
         for key, val in Eintrag.items():
             data[key]= val
         #data.update(Eintrag)

#print('Sensordata from entities:', data)
# Neue CSV-Datei mit dem aktuellen Datum erstellen und Die Keys Werte der sensoren in CSV-Tabelle speichern
os.chdir('/home/pi/Desktop/Data')
filename = Datum + 'Zwave Data.csv'
if not os.path.isfile(filename):
    outfile = open(filename, "w")
    lineKey = ""
    for x in data.keys():
        lineKey+= x + ","
    lineKey = 'Time '+ "," + lineKey[:-1]+"\n" # Delete last character and add new line
    #print('lineKey is:', lineKey)
    outfile = open(filename, "a")
    outfile.write(lineKey)
    outfile.close()
# Die Werte der sensoren in CSV-Tabelle speichern
lineValue = ""
for k,v in data.items():
    lineValue+= v + ","
lineValue = Time + "," + lineValue[:-1] + "\n" 
print( 'this is linevalue with Time: ', lineValue)
outfile = open(filename, "a")
outfile.write(lineValue)
outfile.close()
