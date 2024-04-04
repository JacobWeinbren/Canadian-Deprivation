import csv
import json

# Load CSV data
csv_file_path = "source/can_scores_quintiles_EN.csv"
csv_data = {}

print(f"Loading data from CSV file: {csv_file_path}")
with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Use PRCDDA as key and store rounded quintiles information
        csv_data[row["PRCDDA"]] = {
            "A": round(float(row["Residential instability Scores"]), 2),
            "B": round(float(row["Economic dependency Scores"]), 2),
            "C": round(float(row["Ethno-cultural composition Scores"]), 2),
            "D": round(float(row["Situational vulnerability Scores"]), 2),
            "A_Q": round(float(row["Residential instability Quintiles"])),
            "B_Q": round(float(row["Economic dependency Quintiles"])),
            "C_Q": round(float(row["Ethno-cultural composition Quintiles"])),
            "D_Q": round(float(row["Situational vulnerability Quintiles"])),
        }

# Load GeoJSON data
geojson_file_path = "source/canada.geojson"
print(f"Loading GeoJSON data from file: {geojson_file_path}")
with open(geojson_file_path, mode="r", encoding="utf-8") as geojson_file:
    geojson_data = json.load(geojson_file)

# Update GeoJSON with CSV data
print("Updating GeoJSON features with CSV data...")
for feature in geojson_data["features"]:
    dauid = feature["properties"]["DAUID"]
    if dauid in csv_data:
        feature["properties"].update(csv_data[dauid])

# Save updated GeoJSON
updated_geojson_file_path = "output/updated_canada.geojson"
print(f"Saving updated GeoJSON data to file: {updated_geojson_file_path}")
with open(updated_geojson_file_path, mode="w", encoding="utf-8") as file:
    json.dump(geojson_data, file, ensure_ascii=False)

print("GeoJSON file has been updated with rounded quintile information.")
