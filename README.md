
# Prediction of Patient Dropout Rates

**Work in Progress**

## 1. Data Gathering:

### Access ClinicalTrials.gov Data:

To access data from ClinicalTrials.gov, the recommended method is through their API. Refer to the [ClinicalTrials.gov API documentation](https://clinicaltrials.gov/data-api/api) for detailed information on available endpoints and parameters.

Alternatively, you can leverage the Python module `pytrials` ([PyPI: pytrials](https://pypi.org/project/pytrials/)). Please refer to the `ClinicalTrials_API.py` file for implementation details.

### Obtain AACT Database:

Download the AACT (Aggregate Analysis of ClinicalTrials.gov) database from the official website: [Aggregate Analysis of ClinicalTrials.gov (AACT)](https://aact.ctti-clinicaltrials.org/download). Follow the instructions provided on the website to obtain the database in a suitable format.

## 2. Merge Data:

Utilize unique identifiers, such as NCT IDs, to match data obtained from ClinicalTrials.gov with the AACT database. The AACT database typically includes additional information not available through the Clinical Trials API.

## 3. Data Analysis:

### Explore and Analyze:

Leverage data analysis tools such as Pandas and Numpy to explore the combined dataset. Uncover insights, patterns, and trends that contribute to understanding patient dropout rates.

## 4. Data Visualization:

Utilize visualization libraries such as Matplotlib and Seaborn to generate insightful charts and graphs representing the analysis results.

## 5. Data Preprocessing:
Clean the data, handle missing values, and convert categorical variables into a suitable format for machine learning models.

