#!/bin/bash

echo "Start Load"

sleep 5

echo "Load Collections"

sleep 5

collections=(

    "ClientCollection"
    "DriverCollection"
    "LocationCollection"
    "ProductCollection" 
    "VehicleCollection"
    
)

for collection in "${collections[@]}"
do
  mongoimport --host localhost --port 27017 --db montogre --collection "$collection" --type json --file "/collections_data/$collection.json" --jsonArray
done
