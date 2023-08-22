# Pyre: Python Analytics for FHIR-based Healthcare Data
Pyre is a specialized analytics package designed for healthcare data in Python. It exclusively works with the FHIR (Fast Healthcare Interoperability Resources) format, simplifying the process of loading FHIR resources into Pandas DataFrames.

## Key Features:
- Load FHIR Resources Efficiently: Pyre streamlines the process of importing various FHIR resources (like Patient, Encounter, Observation) into individual Pandas DataFrames.

- NDJSON Support: Pyre leverages the NDJSON format (as recommended by Bulk FHIR) for input. Simply store your FHIR resources in .ndjson files within the inputs directory, and Pyre will handle the rest.

- Built-in Analytics Functions: Pyre offers a suite of built-in analytics functions tailored for common Population Health criteria. Plus, the community is encouraged to contribute with more!
## Requirements:
Ensure you have the necessary packages installed:

```pip install pandas ndjson```

## Getting Started:
To initiate Pyre, run:
```python pyre.py```

## Loading Additional Data:
To add more data to Pyre:

- Copy your .ndjson file(s) into the data directory.

- Ensure your file adheres to the naming convention corresponding to the FHIR resource (e.g., Patient.ndjson, Encounter.ndjson).

- Remember, only the NDJSON format is supported. Each line in your NDJSON file should represent a distinct FHIR resource. Avoid mixing multiple resources within a single file.

## Contribute:
We welcome and appreciate contributions! If you have an analytics function or any other enhancement in mind, feel free to submit a Pull Request.

