# PAN Number Validation Project

## Overview

A Python and Pandas project to clean and validate Indian Permanent Account Numbers (PANs) based on predefined formatting rules.

**Tools:** Python, Pandas, Regular Expressions (Regex)

## Data Cleaning & Validation

- Removed duplicates, missing values, and empty strings.
- Standardized text by trimming whitespace and converting letters to uppercase.
- Validated PAN format (`AAAAA1234A`), character types, adjacent duplicates, and consecutive sequences.

## Results

| Metric | Count |
|---|---:|
| Original Records | 10,000 |
| Records After Cleaning | 9,025 |
| Valid PANs | 3,186 |
| Invalid PANs | 5,839 |
| Missing PANs | 965 |
| Empty PANs | 2 |
| Incomplete PANs (Length < 10) | 1,006 |
| Missing or Incomplete PANs | 1,971 |
| Valid Rate (Cleaned Data) | 35.3% |
| Invalid Rate (Cleaned Data) | 64.7% |

*Valid and invalid counts are based on the cleaned dataset. Missing and incomplete counts are based on the original dataset and overlap with other categories.*

## Conclusion

Of the 9,025 cleaned records, **3,186 passed the implemented validation checks**, while **5,839 were classified as invalid**.

This project demonstrates practical skills in data cleaning, string manipulation, and rule-based validation using Python and Pandas.
