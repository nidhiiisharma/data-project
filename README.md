# data-project
This project shows a basic ETL pipeline and data exploration workflow.

## What this project does
1. Reads raw CSV data
2. Cleans missing and incorrect values
3. Creates a new column (total value)
4. Saves the cleaned data
5. Explores the cleaned data in a Jupyter notebook with simple plots

## Files
- scripts/etl.py: the ETL script
- data/data.csv: original data
- data/clean_data.csv: cleaned output
- notebook/data_cleaning.ipynb: notebook for exploration

## Tools
Python, Pandas, Jupyter, Matplotlib, Seaborn

## ETL Pipeline

The ETL pipeline is implemented in `src/etl.py`:

- **Extract**: Loads raw CSV and JSON files from the data folder  
- **Transform**: Cleans the data by removing missing and invalid values and creates a new column  
- **Load**: Saves the cleaned dataset as `clean_data.csv`  