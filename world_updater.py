import csv
import json
import os
import subprocess
import time

def process_csv(csv_file_path):
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            country_code = row[0]  # Assuming the first column is the country code
            properties = {f'property_{i}': value for i, value in enumerate(row[1:], start=1)}
            update_geojson(country_code, properties)

def update_geojson(country_code, properties):
    geojson_file_path = find_geojson_file(country_code)
    if geojson_file_path:
        with open(geojson_file_path, 'r') as file:
            geojson = json.load(file)
        feature = geojson  # Assuming only one feature per file
        for key, value in properties.items():
            feature['properties'][key] = value
        with open(geojson_file_path, 'w') as file:
            json.dump(geojson, file, indent=4)
    else:
        print(f"GeoJSON file for country code {country_code} not found.")

def find_geojson_file(country_code):
    directories = ['world/Countries', 'world/Territories']
    for directory in directories:
        for filename in os.listdir(directory):
            if filename.startswith(country_code):
                return os.path.join(directory, filename)
    return None

def commit_and_push_changes(branch_name):
    subprocess.run(['git', 'checkout', '-b', branch_name])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', f'Update GeoJSON files based on CSV input'])
    subprocess.run(['git', 'push', 'origin', branch_name])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python update_geojson.py <path-to-csv-file>")
        sys.exit(1)
    csv_file_path = sys.argv[1]
    process_csv(csv_file_path)
    branch_name = f"update-geojson-{int(time.time())}"
    commit_and_push_changes(branch_name)