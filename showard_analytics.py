''' This module involves fetching data from the web, processing it using appropriate Python collections, and writing the processed data to files.'''

#Standard library imports
import csv
import os
import json

#External library imports
import requests
from collections import Counter
import pandas as pd
import xlrd

#Function to fetch data to a new text file from a URL
def fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url):
    try:
        response = requests.get(txt_url)
        if response.status_code == 200:
        
            # Create folder if it does not exist
            if not os.path.exists(txt_folder_name):
                os.makedirs(txt_folder_name)

            # Write text data to text file
            with open(os.path.join(txt_folder_name, txt_filename), 'w', encoding='utf-8') as file:
                file.write(response.text)
            print("Text data saved successfully.")
        else:
            print(f"Failed to fetch data: {response.status_code}")
    except Exception as e:
        print(f"Error fetching and writing text data: {e}")

# Function to read data from an Excel file (.xls format)
def read_excel_data(excel_folder_name, excel_filename):
    try:

        # Construct the file path
        excel_file_path = os.path.join(excel_folder_name, excel_filename)
        
        # Open the Excel file
        workbook = xlrd.open_workbook(excel_file_path)
        
        # Access a specific sheet
        sheet = workbook.sheet_by_index(0)
        
        # Read and print data from the sheet
        for row_index in range(sheet.nrows):
            row_data = sheet.row_values(row_index)
            print(row_data)
    except Exception as e:
        print(f"Error reading Excel file: {e}")

#Function to read data from an Excel file 
def fetch_and_write_excel_data(excel_folder_name, excel_filename, excel_url):
        
        #Fetch data from URL
        response = requests.get(excel_url)
        if response.status_code == 200:
        
            # Create folder if it does not exist
            if not os.path.exists(excel_folder_name):
                os.makedirs(excel_folder_name)

            # Write data to excel file
            with open(os.path.join(excel_folder_name, excel_filename), 'wb') as file:
                file.write(response.content)
            print("Excel data saved successfully.")
            
            #Call function to read the Excel file
            read_excel_data(excel_folder_name, excel_filename)
        else:
            print(f"Failed to fetch excel data: {response.status_code}")

#Function to fetch data to a new CSV file 
def fetch_and_write_csv_data(csv_folder_name, csv_filename, csv_url):
        
        #Fetch data from URL
        response = requests.get(csv_url)
        if response.status_code == 200:
        
            # Create folder if it does not exist
            if not os.path.exists(csv_folder_name):
                os.makedirs(csv_folder_name)

            # Write data to csv file
            with open(os.path.join(csv_folder_name, csv_filename), 'w', encoding='utf-8') as file:
                file.write(response.text)
            print("csv data saved successfully.")
        else:
            print(f"Failed to fetch csv data: {response.status_code}")

#Function to fetch data to a new json file 
def fetch_and_write_json_data(json_folder_name, json_filename, json_url):
        
        #Fetch data from URL
        response = requests.get(json_url)
        if response.status_code == 200:
        
            # Create folder if it does not exist
            if not os.path.exists(json_folder_name):
                os.makedirs(json_folder_name)

            # Write data to csv file
            with open(os.path.join(json_folder_name, json_filename), 'w', encoding='utf-8') as file:
                file.write(response.text)
            print("json data saved successfully.")
        else:
            print(f"Failed to fetch json data: {response.status_code}")

# Function to process text data
def process_txt_file(txt_folder_name, input_filename, output_filename):
    try:
        input_file_path = os.path.join(txt_folder_name, input_filename)
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            text_data = input_file.read()

        # Count total words
        word_count = len(text_data.split())

        # Convert the Counter object to a string for writing to file
        processed_data = f"Word Count: {word_count}\n{text_data}"

        # Define output file path
        output_file_path = os.path.join(txt_folder_name, output_filename)
            
        # Write processed data to output text file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(processed_data)
            
        print(f"Processed data written to '{output_file_path}'")
    except Exception:
        print("Error processing text file.")

# Function to process excel data
def process_excel_file(excel_folder_name, input_filename, output_filename):
    try:
        # Construct the file paths
        input_file_path = os.path.join(excel_folder_name, input_filename)
        output_file_path = os.path.join(excel_folder_name, output_filename)
        
        # Read input Excel file
        df = pd.read_excel(input_file_path)
        
        # Calculate summary statistics
        summary_stats = df.describe()
        
        # Convert the summary statistics DataFrame to a string for writing to file
        summary_stats_str = summary_stats.to_string()
        
        # Write summary statistics to output text file
        with open(output_file_path, 'w') as output_file:
            output_file.write(summary_stats_str)
        
        print(f"Summary statistics written to '{output_file_path}'")
    except Exception as e:
        print(f"Error processing Excel file: {e}")

 # Function to process csv data
def process_csv_file(csv_folder_name, input_filename, output_filename):
    try:
        input_file_path = os.path.join(csv_folder_name, input_filename)

        # Read input CSV file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Read the header to dynamically determine column names
            header = next(csv_reader)

            # Read data and convert rows to tuples
            data = [tuple(row) for row in csv_reader]

        # Pandas dataframe for analysis
        df = pd.DataFrame(data, columns=header)

        # Calculate summary statistics
        summary_stats = df.describe()

        #convert summary statistics to string
        summary_stats_str = str(summary_stats)

        # Define output file path
        output_summary_path = os.path.join(csv_folder_name, output_filename)

        # Write summary statistics to output text file
        with open(output_summary_path, 'w') as output_file:
            output_file.write(summary_stats_str)
        print(f"Summary statistics saved to '{output_summary_path}'")
    except Exception as e:
        print(f"Error processing CSV file: {e}")

# Function to process json data
def process_json_file(json_folder_name, input_filename, output_filename):
    try:
        input_file_path = os.path.join(json_folder_name, input_filename)
        with open(input_file_path, 'r') as file:
            json_data = json.load(file)
        
        # Print the loaded JSON data to see its structure
        print("JSON Data Structure:")
        print(json_data)
        
        # Check if "people" key exists in the JSON data
        if "people" in json_data:
            people_list = json_data["people"]
            for person in people_list:
                name_value = person["name"]
                craft_value = person["craft"]
                print(f"Name: {name_value}, Craft: {craft_value}")
                
                # Construct formatted information
                json_info = f"Name: {name_value}\nCraft: {craft_value}"
                
                # Define output file path for each person
                output_person_path = os.path.join(json_folder_name, f"{name_value}_{output_filename}")
                
                # Write information to output text file for each person
                with open(output_person_path, 'w') as output_file:
                    output_file.write(json_info)
                
                print(f"Formatted information saved to '{output_person_path}'")
        else:
            print("Error: 'people' key not found in JSON data.")
            return
        
    except Exception as e:
        print(f"Error parsing JSON data: {e}")

def main():
    ''' Main function to demonstrate module capabilities. '''

    #Print my name
    name = "Sarah Howard"
    print(f"Name: {name}")

    #Main url's
    txt_url = 'https://shakespeare.mit.edu/romeo_juliet/full.html'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    json_url = 'http://api.open-notify.org/astros.json'

    #Folder names
    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    #File names
    txt_filename = 'romeoJuliet.txt'
    csv_filename = 'countryscore.csv'
    excel_filename = 'cattle.xls' 
    json_filename = 'astronauts.json' 

    #Function to fetch data from sources and convert to files
    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    #Function to process data in file formats
    process_txt_file(txt_folder_name,'romeoJuliet.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'countryLadderScore.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'cattle.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'astronauts.json', 'results_json.txt')



if __name__ == '__main__':
    main()
