"""
A csv converter 
Module for converting CSV files to JSON format.
It will read a CSV file, parse its contents, and create a JSON representation of the data.

It will work by using the built-in csv and json libraries in Python.
"""
import csv
import json
import os
from datetime import datetime

def csv_to_json(csv_file_path):
    data = [] # List to hold the rows as dictionaries

    try:
        # Read the CSV file and convert each row to a dictionary
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
        return
    
    # Generate JSON file path with timestamp
    dir_path = os.path.dirname(csv_file_path)
    base_name = os.path.basename(csv_file_path)
    name_without_ext = os.path.splitext(base_name)[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_file_name = f"{name_without_ext}_{timestamp}.json"
    json_file_path = os.path.join('./data/json', json_file_name)
    
    try:
        # Write the data to a JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"JSON file created: {json_file_path}")
    except FileNotFoundError:
        print(f"Error: Unable to write to '{json_file_path}'. Check the directory path.")

# to ensure the module can be run as a script
if __name__ == "__main__":
    try:
        # if run as a script, convert a sample CSV file to JSON
        sample_csv = './data/csv/example.csv'
        csv_to_json(sample_csv)
    except Exception as e:
        print(f"An error occurred: {e}")