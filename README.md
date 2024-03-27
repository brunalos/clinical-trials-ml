# Predicting Patient Dropout Rates in Vaccine Clinical Trials

Clinical trials often face challenges in proving the effectiveness of treatments, such as vaccines. One significant issue in successfully executing a trial is participants dropping out, which can extend the trial duration.

To address this problem, I have gathered information from various public datasets to identify the main reasons why people drop out of trials, specifically vaccine trials. It examines factors such as the trial duration, number of participants, trial phase, participants' demographics, geographic location, trial sponsors, and more. By analyzing these factors before initiating a trial, researchers can gain insights into the likelihood of participant dropouts and develop strategies to prevent them.

**Work in Progress**

## Table of Contents
1. [Data Gathering](#1-data-gathering)
2. [Data Preprocessing](#2-data-preprocessing)
3. [Data Analysis and Visualization](#3-data-analysis-and-visualization)
4. [Machine Learning Model Building](#4-machine-learning-model-building)
5. [Python libraries](#5-python-libraries)
[References](#References)


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
- Encode categorical variables into numerical representations using techniques like one-hot encoding, label encoding, binary encoding.

**Normalization and Scaling:**
- Normalize or scale numerical features to ensure uniformity and improve model performance. 

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

For this project, five algorithms were used to make predictions:

1. Linear Regression
2. K Nearest Neighbor
3. Decision Trees
4. Random Forests
5. XGBoost

## 5. Python Libraries

#### Requirements

- Python 3.9.7 
- Jupyter Notebook

#### Installation

```bash
pip install pandas==1.3.3 numpy==1.21.2 seaborn==0.11.2 matplotlib==3.4.3 scikit-learn==0.24.2  xgboost==2.0.3
```

For initial data preprocessing steps, analysis and visualization please refer to: `vaccines.ipynb`.
For ML model building please refer to: `dropout_rates_model.ipynb`.

## References
```
Hutchison, E., Zhang, Y., Nampally, S., Neelufer, I. K., Malkov, V., Weatherall, J., Khan, F., & Shameer, K. (2021). Modeling Clinical Trial Attrition Using Machine Intelligence: A driver analytics case study using 1,325 trials representing one million patients [Preprint]. doi: https://doi.org/10.1101/2021.11.12.21266277

