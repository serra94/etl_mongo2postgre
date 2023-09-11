#!/bin/bash

echo "Start Load"

sleep 5

echo "Load Collections"

sleep 5

collections=(

    "CheckPoints" 
)

for collection in "${collections[@]}"
do
  mongoimport --host localhost --port 27017 --db etl_mongo_to_postgre --collection "$collection" --type json --file "/collections_data/$collection.json" --jsonArray
done
