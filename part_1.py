#1. find station code for seattle
with open("stations.csv") as file:
    stations = list(file)
    print(stations)

#import json
import json

#2. compile only seattle data points
with open('precipitation.json') as file:
    data = json.load(file)

    seattle_compiled = []
    for each_element in data:
        if each_element["station"] == "GHCND:US1CASD0032" :
            seattle_compiled.append(each_element)
    print(seattle_compiled)

   

#3. we now have a list containing only the dictionary entries at Seattle, which is Seattle compiled:
total = []
for i in range (12):
    readings = []

    for measurement in seattle_compiled:
        month_per_measurement = (measurement["date"].split("-")[(1)])
        int_mpm = int(month_per_measurement)
        
        if int_mpm == i+1:
            readings.append(measurement["value"])

    
    total.append(sum(readings))

print(total)












#here, you'll be able to use the data variable,
#which contains the data from precipitation.json
