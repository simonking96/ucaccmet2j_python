#1. find station code for seattle
with open("stations.csv") as file:
    stations = list(file)
    print(stations)

#import json
import json

#2. compile only seattle data points
with open('precipitation.json') as file:
    data = json.load(file)

#RAN OUT OF TIME: what I would do here in order to calculate the results for each weather station,
# is define a list of the individual station code, and create a for loop like:
# for i in station_list 
#   for each_element in data:
#        if each_element["station"] == "i" :
# and have the rest of the code indented within this for loop until the end, at which point I would create a
# list with a dictionary for the results at each station inside
station_list = ["GHCND:US1CASD0032", "GHCND:USW00093814", "GHCND:USC00513317", "GHCND:US1CASD0032"]
for i in station_list:
    place_compiled = []
    for each_element in data:
        if each_element["station"] == "i" :
            place_compiled.append(each_element)
    print(place_compiled)

   

#3. we now have a list containing only the dictionary entries at Seattle, which is Seattle compiled:
    total = []
    for i in range (12):
        readings = []

        for measurement in place_compiled:
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

    #DEfine dictionaries for each i here
    #Manually recode code name i to place name 
    

