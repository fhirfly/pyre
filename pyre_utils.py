from frames.resourceframe import patient_frame, device_frame 

def moveDFtoDictionary(resourceType, df):
    if resourceType == "Patient":
        patient_frame.append(df) 
    if resourceType == "Device":
        device_frame.append(df)
