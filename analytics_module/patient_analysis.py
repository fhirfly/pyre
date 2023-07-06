from datetime import datetime
import pandas as pd

def calculate_age(birthdate):
    # Get the current date
    current_date = datetime.now()
    birthdate  =  birthdate[0]
    birthdate = datetime.strptime(birthdate , '%Y-%m-%d')
    # Calculate the age based on the difference between the current date and the birthdate
    age = current_date.year - birthdate.year
    
    # Adjust the age if the current month and day are before the birthdate
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1
    
    return age

def calculate_gender_distribution(dfs):
    # Empty list to store all gender data
    all_genders = []

    # Iterate over all dataframes3
    for df in dfs: 
        # Ensure the 'gender' column exists in the dataframe
        if 'gender' in df.columns:
            # Append the gender data to our list
            all_genders.append(df['gender'][0])
        else:
            print('No gender column in one of the dataframes. Please check the input.')

    # Create a new dataframe for the gender distribution
    gender_df = pd.DataFrame(all_genders, columns=['gender'])

    # Calculate and return the distribution
    return gender_df['gender'].value_counts(normalize=True)

def calculate_marital_status_distribution(dfs):
    # Empty list to store all gender data
    all_ms = []

    # Iterate over all dataframes
    for df in dfs: 
        # Ensure the 'gender' column exists in the dataframe
        if 'maritalStatus_text' in df.columns:
            # Append the gender data to our list
            all_ms.append(df['maritalStatus_text'][0])
        else:
            print('No marital status column in one of the dataframes. Please check the input.')

    # Create a new dataframe for the gender distribution
    ms_df = pd.DataFrame(all_ms, columns=['maritalStatus'])

    # Calculate and return the distribution
    return ms_df['maritalStatus'].value_counts(normalize=True)

def calculate_age_distribution(dfs):
    # Empty list to store all ages
    all_ages = []

    # Iterate over all dataframes
    for df in dfs:  
        # Ensure the 'age' column exists in the dataframe
        if 'birthDate' in df.columns:
            # Append the age data to our list
            all_ages.append(calculate_age(df['birthDate']))
        else:
            print('No age column in one of the dataframes. Please check the input.')

    # Create a new dataframe for the age distribution
    age_df = pd.DataFrame(all_ages, columns=['age'])

    # Calculate and return the distribution
    return age_df['age'].value_counts(normalize=True)

def print_age_distribution(patient_frame):
    if patient_frame != None and  patient_frame.__len__() > 0:
        age_distribution = calculate_age_distribution(patient_frame)
        # Convert the Series to a DataFrame for better visualization
        age_distribution_df = pd.DataFrame({'Age': age_distribution.index, 'Distribution': age_distribution.values})
        # Use to_string() to print the DataFrame in a more readable format
        print('Patient Age Distribution:\n')
        age_distribution_df = age_distribution_df.sort_values('Age')
        print(age_distribution_df.to_string(index=False))
    else:
        print("No Patients Exist in the Dataset. Please check your inputs")

def print_gender_distribution(patient_frame):
    # Print the DataFrame in a more readable format
    if patient_frame != None and  patient_frame.__len__() > 0:
        gender_distribution = calculate_gender_distribution(patient_frame)
        # Convert the Series to a DataFrame for better visualization
        gender_distribution_df = pd.DataFrame({'Gender': gender_distribution.index, 'Distribution': gender_distribution.values})
        print('Patient Gender Distribution:\n')
        print(gender_distribution_df.to_string(index=False))
    else:
        print("No Patients Exist in the Dataset. Please check your inputs")

def print_marital_status_distribution(patient_frame):
    if patient_frame != None and  patient_frame.__len__() > 0:
        ms_distribution = calculate_marital_status_distribution(patient_frame)
        ms_distribution_df = pd.DataFrame({'Marital Status': ms_distribution.index, 'Distribution': ms_distribution.values})   
        print('Martial Status Distribution:\n')
        print(ms_distribution_df.to_string(index=False))
    else:
        print("No Patients Exist in the Dataset. Please check your inputs")