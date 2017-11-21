import homeassistant.remote as remote
import csv, json
from datetime import datetime
import threading
import os
import time
import collections
orderedDict = collections.OrderedDict()
from collections import OrderedDict
from time import sleep
import threading

    
Datum = time.strftime("%Y-%m-%d")
Time = datetime.now().replace(microsecond=0).isoformat()

def timer():
    threading.Timer(1600,timer).start()
    Datum = time.strftime("%Y-%m-%d")
    Time = datetime.now().replace(microsecond=0).isoformat()
 
    api = remote.API('127.0.0.1', 'password')
    entities = remote.get_states(api)
    for entity in entities:
        print(entity)
        print()        
        Luftfeuchtigkeit = remote.get_state(api, 'sensor.keller_relative_humidity')
        Luftfeuchtigkeitdata = {Luftfeuchtigkeit.name : Luftfeuchtigkeit.state}
        #print (Luftfeuchtigkeitdata)

        Temperatur = remote.get_state(api, 'sensor.keller_temperature')
        Temperaturdata = {Temperatur.name: Temperatur.state}
        #print (Temperaturdata)


        Helligkeit = remote.get_state(api, 'sensor.keller_luminance')
        Helligkeitdata = {Helligkeit.name: Helligkeit.state}
        #print (Helligkeitdata)
        
        
        Bewegungsmelder = remote.get_state(api, 'sensor.keller_Burglar')
        Bewegungsmelderdata = {Bewegungsmelder.name : Bewegungsmelder.state}
        #print (Bewegungsmelderdata)
        
        
        Luftfeuchtigkeit_EG = remote.get_state(api, 'sensor.eg_relative_humidity')
        Luftfeuchtigkeitdata_EG = {Luftfeuchtigkeit_EG.name : Luftfeuchtigkeit_EG.state}
        #print (Luftfeuchtigkeitdata)

        Temperatur_EG = remote.get_state(api, 'sensor.eg_eg_temperatur_c')
        Temperaturdata_EG = {Temperatur_EG.name: Temperatur_EG.state}
        #print (Temperaturdata)


        Helligkeit_EG = remote.get_state(api, 'sensor.EG_Luminance')
        Helligkeitdata_EG = {Helligkeit_EG.name: Helligkeit_EG.state}
        #print (Helligkeitdata)
        
        
        Bewegungsmelder_EG = remote.get_state(api, 'sensor.EG_Burglar')
        Bewegungsmelderdata_EG = {Bewegungsmelder_EG.name : Bewegungsmelder_EG.state}
        #print (Bewegungsmelderdata)
        
        
        Stecker_EG_Leistung = remote.get_state(api, 'sensor.fibaro_system_fgwpef_wall_plug_gen5_power_2')
        Stecker_EG_Leistungdata = {Stecker_EG_Leistung.name: Stecker_EG_Leistung.state}
        print (Stecker_EG_Leistung)
        
        
        Stecker_EG = remote.get_state(api, 'sensor.fibaro_system_fgwpef_wall_plug_gen5_energy')
        Steckerdata_EG = {Stecker_EG.name : Stecker_EG.state}
        print (Stecker_EG)
        
        
        

    data= Luftfeuchtigkeitdata,Temperaturdata, Helligkeitdata, Bewegungsmelderdata, Luftfeuchtigkeitdata_EG,Temperaturdata_EG, Helligkeitdata_EG,Bewegungsmelderdata_EG,Stecker_EG_Leistungdata,Steckerdata_EG


    filename = Datum + '_test_V2.csv'
    if not os.path.isfile(filename):
        outfile = open(filename, "w")
        line = ""
        for x in data:
            print('x is', x)
            print('x.keys is ',x.keys())
            for key in x.keys():
                print('key is ',key)
                line+= key + ","
        line = 'Time '+ "," + line[:-1]+"\n" # Delete last character and add new line
        print('line is:', line)
        outfile = open(filename, "a")
        outfile.write(line)
        outfile.close()

    lineValue = ""
    for y in data:
        print(y.values())
        for value in y.values():
            print(value)
            lineValue+= value + ","
    lineValue = Time + "," + lineValue[:-1] + "\n" # Delete last character and add new line 
    print( 'this is linevalue with Time: ', lineValue)
    outfile = open(filename, "a")
    outfile.write(lineValue)
    outfile.close()
timer()

