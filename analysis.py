import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("task 3/bank-additional-full.csv", sep=";")

# Display the first 5 rows
print("\n--- FIRST 5 ROWS ---")
print(df.head())

# Display dataset dimensions
print("\n--- DATASET SHAPE ---")
print(df.shape)

# Display column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# Display dataset information
print("\n--- DATASET INFORMATION ---")
df.info()

# Check missing values
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Check duplicate records
print("\n--- DUPLICATE RECORDS ---")
print(df.duplicated().sum())

# Display statistical summary
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe(include="all"))


# ============================================
# DATA CLEANING
# ============================================

print("\n--- UNKNOWN VALUES BEFORE CLEANING ---")

for column in df.select_dtypes(include="str").columns:
    unknown_count = (df[column] == "unknown").sum()
    if unknown_count > 0:
        print(f"{column}: {unknown_count}")

# Remove duplicate records
print("\n--- REMOVING DUPLICATES ---")

df = df.drop_duplicates()

print("Duplicates remaining:", df.duplicated().sum())
print("Dataset shape after cleaning:", df.shape)

# Check subscription outcomes
print("\n--- SUBSCRIPTION OUTCOMES ---")

print(df["y"].value_counts())

print("\n--- SUBSCRIPTION PERCENTAGES ---")

print(df["y"].value_counts(normalize=True) * 100)

# Create outputs folder if it doesn't exist
import os

os.makedirs("outputs3", exist_ok=True)
df.to_csv("outputs3/cleaned_bank_marketing.csv", index=False)

print("\nCleaned dataset exported successfully to outputs3!")

# ============================================
# EXPLORATORY DATA ANALYSIS (EDA)
# ============================================

# Convert subscription outcome into numerical values
df["converted"] = (df["y"] == "yes").astype(int)

# Function to calculate conversion rates
def conversion_summary(column):
    summary = df.groupby(column)["converted"].agg(
        total_contacts="count",
        successful_subscriptions="sum",
        conversion_rate="mean"
    )

    summary["conversion_rate"] = summary["conversion_rate"] * 100

    return summary.sort_values(
        by="conversion_rate",
        ascending=False
    )


# 1. Conversion by Job
job_analysis = conversion_summary("job")

print("\n--- CONVERSION BY JOB ---")
print(job_analysis)

job_analysis.to_csv("outputs/conversion_by_job.csv")


# 2. Conversion by Education
education_analysis = conversion_summary("education")

print("\n--- CONVERSION BY EDUCATION ---")
print(education_analysis)

education_analysis.to_csv("outputs/conversion_by_education.csv")


# 3. Conversion by Contact Method
contact_analysis = conversion_summary("contact")

print("\n--- CONVERSION BY CONTACT METHOD ---")
print(contact_analysis)

contact_analysis.to_csv("outputs/conversion_by_contact.csv")


# 4. Conversion by Month
month_analysis = conversion_summary("month")

print("\n--- CONVERSION BY MONTH ---")
print(month_analysis)

month_analysis.to_csv("outputs/conversion_by_month.csv")


# 5. Conversion by Previous Campaign Outcome
poutcome_analysis = conversion_summary("poutcome")

print("\n--- CONVERSION BY PREVIOUS CAMPAIGN OUTCOME ---")
print(poutcome_analysis)

poutcome_analysis.to_csv("outputs/conversion_by_poutcome.csv")


# 6. Conversion by Number of Campaign Contacts
df["campaign_group"] = df["campaign"].apply(
    lambda x: str(x) if x <= 5 else "6+"
)

campaign_analysis = conversion_summary("campaign_group")

print("\n--- CONVERSION BY CAMPAIGN CONTACTS ---")
print(campaign_analysis)

campaign_analysis.to_csv("outputs/conversion_by_campaign.csv")


# 7. Conversion by Age Group
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 25, 35, 45, 55, 100],
    labels=["17-25", "26-35", "36-45", "46-55", "56+"]
)

age_analysis = conversion_summary("age_group")

print("\n--- CONVERSION BY AGE GROUP ---")
print(age_analysis)

age_analysis.to_csv("outputs/conversion_by_age.csv")


print("\nEDA SUMMARY FILES EXPORTED SUCCESSFULLY!")
# ============================================
# EXPORT FINAL CLEANED DATASET
# ============================================

import os

os.makedirs("outputs3", exist_ok=True)

df.to_csv("outputs3/cleaned_bank_marketing.csv", index=False)

print("\nFinal cleaned dataset exported successfully!")
print("Final dataset shape:", df.shape)
print("File location: outputs3/cleaned_bank_marketing.csv")