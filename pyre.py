import os
from datetime import datetime
import pandas as pd
import ndjson
from pandas import json_normalize

#Part of this module
import kindling
import pyre_utils
from frames.fhirframe import fhir_frame, patient_frame, device_frame    
from analytics_module import patient_analysis

def main():
    # Load data
    data = load_data()
    if data == True:
        # Display user prompt
        while True:

            print("\nPlease select an option:")
            print("1. Calculate Patient Age Distribution")
            print("2. Calculate Patient Gender Distribution")
            print("3. Calculate Patient Martial Status Distribution")
            print("4. Quit")

            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                result = patient_analysis.print_age_distribution(patient_frame)
            elif choice == '2':
                result = patient_analysis.print_gender_distribution(patient_frame)
            elif choice == '3':
                result = patient_analysis.print_marital_status_distribution(patient_frame)
            elif choice == '4':
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Data Load Error. Exiting the program...")

def load_data():
   # Implement your data loading logic here
   # Return a list of Pandas DataFrames
   # Load the FHIR dataset
   start_date = datetime.now()
   print("Start Data load at: " + str(start_date))
   #Load data for each NDSON file in the data directory
   for file in os.listdir('./data/'):
        with open('./data/' + file, encoding='utf-8') as f:
            print("loading file: " + './data/' + file)    
            resourceType = file.split('.')[0]        
            try:
                data = ndjson.load(f)
                i = 0
                for line in data:            
                    flat = kindling.flatten_fhir(line)
                    df = pd.json_normalize(flat)
                    # Create a meta frame as a dictionary
                    pyre_utils.moveDFtoDictionary(resourceType, df)
                    i = i + 1
                print('loaded: ' + str(i) + ' ' + resourceType + ' files')                   
            except:
                print("Error loading data file: " + str(file))
                return False
   end_date = datetime.now()
   time_elasped = end_date - start_date
   print("Loading data took: " + str(time_elasped))
   return True

#Main function
if __name__ == "__main__":
    main()