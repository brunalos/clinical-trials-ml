# Import Python modules

from pytrials.client import ClinicalTrials
import pandas as pd


# Function to retrieve information of interest from https://clinicaltrials.gov/


def get_clinical_trials(search_terms, target_fields, max_no_studies, target_format):
    """
    Retrieves information from clinical trials based on specified parameters.

    Parameters:
    - search_terms: Keywords to search for in clinical trials.
    - target_fields: List of fields to retrieve for each study.
    - max_no_studies: Maximum number of studies to retrieve.
    - target_format: Desired format for the retrieved data (e.g. ".csv").

    Returns:
    List containing information of interest from clinical trials.
    """

    ct = ClinicalTrials()

    clinical_trials = ct.get_study_fields(
        search_expr=search_terms,
        fields=target_fields,
        max_studies=max_no_studies,
        fmt=target_format
    )

    return clinical_trials


# Define the information to retrieve from clinical trials


search_terms = "Vaccine"
target_fields = ["NCTId", "Phase", "Condition",
                 "EnrollmentCount", "OverallStatus"]
max_no_studies = 1000
target_format = "csv"

# Call the function and retrieve the information of interest


vaccine_trials = get_clinical_trials(
    search_terms, target_fields, max_no_studies, target_format)

# Create a DataFrame using the retrieved information
# The first list in the result represents column labels


df = pd.DataFrame(vaccine_trials[1:], columns=vaccine_trials[0])

# Save the DataFrame to a CSV file


df.to_csv('./data/vaccine_trials.csv')