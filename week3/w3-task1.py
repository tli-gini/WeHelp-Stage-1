import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as request 
import json
import csv
from collections import defaultdict

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"


def main():
    mrts = []
    with request.urlopen(src1) as response:
        data1=json.load(response) 
        spots=data1["data"]["results"]

    with request.urlopen(src2) as response:
        resp2=json.load(response) 
        data2=resp2['data']
        
        for data in data2:
            station = data['MRT'] 
            if station not in mrts:
                mrts.append(data['MRT'])
        # print(mrts)

    with open("spot.csv","w",encoding="utf-8") as file:   
        writer = csv.writer(file)

        for spot in spots:
            stitle = spot["stitle"]
            longitude = spot["longitude"]
            latitude = spot["latitude"]
            serial_number = spot["SERIAL_NO"]
            img_urls = spot["filelist"] 

            normalized_img_urls = img_urls.replace('.JPG', '.jpg')

            urls = normalized_img_urls.split('.jpg')
            first_url = urls[0] + '.jpg'

            for address in data2:
                if serial_number == address["SERIAL_NO"]:
                    addr = address["address"]
                    addr = addr[5:8]
                    writer.writerow([stitle, addr, longitude, latitude, first_url])

    with open("mrt.csv","w",encoding="utf-8") as file:  
        writer = csv.writer(file)
        stations_with_attractions = []

        for data in data2:
            station = data["MRT"]
            sn = data["SERIAL_NO"]
            for spot in spots:
                if spot["SERIAL_NO"] == sn:
                    stitle = spot["stitle"]
                    stations_with_attractions.append((station, stitle))
        
        print(len(stations_with_attractions))

        aggregated = defaultdict(list)

        for key, value in stations_with_attractions:
            aggregated[key].append(value)

        result = [[key] + values for key, values in aggregated.items()]
        # print(result)
        

        for station_info in result:
            writer.writerow(station_info)
        
                
                


main()
