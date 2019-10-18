


import math
import requests
import json





root2 = math.sqrt(2)
x = 26.872828
y = 75.801798
f = float(1/111)
F = float(1/111.3)
arr = []
# z is the distance 
z = 0.5
inc = 0.5
radius = 5
while(z<= radius):
    point_1 = (x+f*z,y)
    point_2 = (x, y+ F*z)
    point_3 = (x-f*z,y)
    point_4 = (x,y-F*z)
    point_5 = (x + (f*z)/root2, y + (F*z)/root2)
    point_6 = (x + (f*z)/root2, y - (F*z)/root2)
    point_7 = (x - (f*z)/root2, y + (F*z)/root2)
    point_8 = (x - (f*z)/root2, y - (F*z)/root2)
    z = z+ inc
    arr.append(point_1)
    arr.append(point_2)
    arr.append(point_3)
    arr.append(point_4)
    arr.append(point_5)
    arr.append(point_6)
    arr.append(point_7)
    arr.append(point_8)

serviceable = []
unserviceable = []

url1 = 'https://www.swiggy.com/dapi/restaurants/search?lat={}&lng={}&str=pasta%20cucina'

for coordinate in arr:
    x = coordinate[0]
    y = coordinate[1]
    r = requests.get(url= url1.format(x,y))
    data = r.json()
    restaurants = data["data"]["restaurants"][0]["restaurants"]
    found = 0
    for restaurant in restaurants[0:5]:
        if (restaurant["name"]== 'Pasta Cucina'):
            #print(restaurants.index(restaurant))
            found = 1
            break
    if(found == 0): 
        unserviceable.append({"lat": x,"lng": y})
    elif(found == 1):
        serviceable.append({"lat": x,"lng": y})





data = {'serviceable': serviceable, 'unserviceable': unserviceable}
# To write to a file:
f = open("output.json", "w")
f.write("var json_data = ")
f.close()


with open("output.json", "a") as f:
    json.dump(data, f)

# To print out the JSON string (which you could then hardcode into the JS)
#json.dumps(data)    
        

import webbrowser, os
webbrowser.open('file://' + os.path.realpath("map.html"))