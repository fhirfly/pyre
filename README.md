# pyre
Pyre is a Python Analytics Package for Healthcare that assumes FHIR as its input format.  It contains libraries for loading FHIR Resources into Panda Dataframes.
Lists of DataFrames are created for each FHIR Resource (eg. Patient, Encounter, Observation)
FHIR Resouce inputs are stored in NDJSON format (See Bulk FHIR) in the inputs directory and data is loaded into Pyre.
Pyre also contains built in analtics functions for common Population Health Criteria,  Pull Requests are welcome for new functions.

#Requirements:

```pip install pandas, ndjson```

#To Start a Pyre:

```python pyre.py```

#Load Additional Data

Copy an ndjson file into the data directory.  Only NDJSON format is supported.  Your file must be named accodingly (Patient.ndjson, Encounter.ndjson, Observation.ndjson, and so on) for it to work properly.
Keep in mind while dealing with NDJSON that Each line in the NDJSON file is a FHIR resource.  Do not mix multiple Resources in a single file.

