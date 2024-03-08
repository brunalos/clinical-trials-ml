# Predicting Patient Dropout Rates in Vaccine Clinical Trials

**Work in Progress**

## 1. Data Gathering:

### Accessing ClinicalTrials.gov Data:

To access data from ClinicalTrials.gov, the recommended method is through their API. Detailed information on available endpoints and parameters can be found in the [ClinicalTrials.gov API documentation](https://clinicaltrials.gov/data-api/api).

Alternatively, you can utilize the Python module `pytrials` ([PyPI: pytrials](https://pypi.org/project/pytrials/)). Please refer to the `ClinicalTrials_API.py` file for implementation details.

### Obtaining AACT Database:

Download the AACT (Aggregate Analysis of ClinicalTrials.gov) database from the official website: [Aggregate Analysis of ClinicalTrials.gov (AACT)](https://aact.ctti-clinicaltrials.org/download). Follow the instructions provided on the website to obtain the database in a suitable format. The AACT database typically includes additional information not available through the Clinical Trials API.

## 2. Data Preprocessing:

**Data Integration:**
- Merge multiple datasets using the 'nct_id'.

**Handling Missing Values:**
- Identify and rectify missing values through techniques such as imputation or removal.

**Data Cleaning:**
- Remove duplicate records where necessary.
- Rename columns for improved clarity.
- Eliminate unnecessary columns.
- Standardize data formats as needed.

**Data Encoding:**
- Encode categorical variables into numerical representations using techniques like one-hot encoding or label encoding.

**Normalization and Scaling:**
- Normalize or scale numerical features to ensure uniformity and improve model performance. Techniques include Min-Max scaling or Standardization.

**Data Splitting:**
- Split the dataset into training and testing sets for machine learning models.

## 3. Data Analysis and Visualization:

### Exploration and Analysis:

Uncover insights, patterns, and trends that contribute to understanding patient dropout rates in vaccine clinical trials.

For example:
- Visualize the distribution of clinical trials by phase.
- Identify the most frequently reported reasons for patients discontinuing their participation in vaccine clinical trials.
- Determine the most prevalent conditions/diseases in vaccine clinical trials.
- Determine the prevalence of vaccines utilized as interventions in clinical trials.
- Summarize participants' progress in the study, including the count of those who started and completed the trial.
- Identify the most prevalent adverse events in vaccine clinical trials.
- Summarize the types of adverse events experienced by participants, whether serious or not.

## 4. Machine Learning Model Building:

For this project, four algorithms were used to make predictions:

1. Linear Regression
2. K Nearest Neighbor
3. Decision Trees
4. Random Forests

## References
```
Hutchison, E., Zhang, Y., Nampally, S., Neelufer, I. K., Malkov, V., Weatherall, J., Khan, F., & Shameer, K. (2021). Modeling Clinical Trial Attrition Using Machine Intelligence: A driver analytics case study using 1,325 trials representing one million patients [Preprint]. doi: https://doi.org/10.1101/2021.11.12.21266277

