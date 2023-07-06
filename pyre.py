import pandas as pd
from analytics_module import patient_analysis
from datetime import datetime
from pandas import json_normalize
import kindling
import ndjson
from frames.fhirframe import fhir_frame, patient_frame    

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

    with open('./data/Patient.ndjson', encoding='utf-8') as f:
        start_date = datetime.now()
        print(start_date)
        data = ndjson.load(f)
        patient_id = 0
        for line in data:
            # json_data is the JSON object
            df = json_normalize(line)
            flat = kindling.flatten_fhir(line)
            df = pd.json_normalize(flat)

            # Store column names and index
            columns = df.columns
            index = df.index

            # Create a meta frame as a dictionary
            patient_frame[patient_id] = df
            patient_id = patient_id + 1
        
        end_date = datetime.now()
        time_elasped = end_date - start_date
        print("Loading data took: " + str(time_elasped))
        return True

if __name__ == "__main__":
    main()