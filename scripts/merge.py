import os
import json

# Set the directory containing the GeoJSON files
directory = "source/buildings"

# Create an empty list to store the features
features = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".geojson"):
        file_path = os.path.join(directory, filename)

        # Open the GeoJSON file and load its contents
        with open(file_path, "r") as file:
            print("Reading", file_path)
            geojson_data = json.load(file)

            # Extract the features and append them to the list
            features.extend(geojson_data["features"])

# Create a new GeoJSON object with the merged features
merged_geojson = {"type": "FeatureCollection", "features": features}

# Save the merged GeoJSON to a file
output_file = "output/merged.geojson"
with open(output_file, "w") as file:
    json.dump(merged_geojson, file)

print(f"Merged GeoJSON saved to {output_file}")
