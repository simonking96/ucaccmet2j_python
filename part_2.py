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

#4 total in the year
annual = (sum(total))
print(annual)

#5 relative precipitation per year
relatives = []
for i in total:
    relative = i / annual
    relatives.append(relative)
print(relatives)


with open('result2.json', 'w') as file:
    json.dump({
	"Seattle": {
		"station": "GHCND:US1CASD0032", 
		"state": "WA", 
		"totalMonthlyPrecipitation": [1323, 853, 144, 481, 5, 3, 34, 0, 14, 617, 394, 1903], 
		"relativeMonthlyPrecipitation": [0.22924969675966037, 0.1478080055449662, 0.0249523479466297, 0.08334777334950615, 0.0008664009703690869, 0.0005198405822214521, 0.005891526598509791, 0.0, 0.002425922717033443, 0.10691387974354531, 0.06827239646508404, 0.32975220932247445], 
		"totalYearlyPrecipitation": 5771
	}
}, file)

