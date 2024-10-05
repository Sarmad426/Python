# Pandas

Pandas is an open-source data manipulation and analysis library for Python. It provides easy-to-use data structures and functions for working with structured data, making it a powerful tool for data cleaning, exploration, and analysis.

## Where is Pandas Used?

- Data cleaning and preparation
- Data analysis and visualization
- Time series analysis
- Statistical analysis
- Data transformation and aggregation
- Working with structured data such as CSV files, Excel spreadsheets, SQL databases, and more

## Installing Pandas

First make sure that your virtual environment is activated.

```bash
pip install pandas
```

This command will download and install the Pandas library and its dependencies.

### Importing Pandas

```python
import pandas as pd
```

### Creating a DataFrame

A DataFrame is a core data structure in Pandas. It's like a table with rows and columns. You can create a DataFrame from various data sources, such as lists, dictionaries, or external files (e.g., CSV, Excel).

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)
```

### Loading Data from a File

You can load data from external files using Pandas. For example, to load data from a CSV file:

```python
df = pd.read_csv('data.csv')
```

### Data Exploration

You can explore your data by using various methods:

```python
# Display the first few rows of the DataFrame
df.head()

# Get summary statistics
df.describe()

# Select specific columns
df['Column_Name']

# Filter data based on conditions
df[df['Age'] > 30]
```

### Data Manipulation

Pandas provides numerous functions for data manipulation, such as:

```python
# Adding a new column
df['Salary'] = [50000, 60000, 75000]

# Removing a column
df.drop('Salary', axis=1, inplace=True)

# Sorting data
df.sort_values(by='Age', ascending=False)

# Grouping and aggregation
df.groupby('Age').mean()
```

### Data Visualization

Pandas can work seamlessly with other Python libraries like Matplotlib and Seaborn for data visualization.

```python
import matplotlib.pyplot as plt

# Plotting data
df.plot(x='Name', y='Age', kind='bar')
plt.show()
```

### Saving Data

After performing data analysis, you may want to save your results to a file.

```python
df.to_csv('output.csv', index=False)
```

These are just some of the basic operations you can perform with Pandas. The library offers a wide range of functionality, making it an essential tool for data analysis in Python.

For more detailed information, you can refer to the official [Pandas documentation](https://pandas.pydata.org/docs/).

## Pandera

`pip install pandera`

To install pandera.

## Pandas Topics Covered

- Series
- Pandera Types
- list,nested list and dictionary series
- DataFrames
- Pandas read json and html format
- DataFrame Schema
- DataFrame Operations
- Creating csv file using pandas

## Pandas DataFrame operations

- add new column
  - one column
  - two or more column
- delete column
- change data type of column
- map
- apply
  - on one column
  - more than one column
- concatenate
- 1. axis
  - axis = 0 (top to bottom)
  - axis = 1 (left to right)
- describe dataframe
  - `df.info()` # total index, columns names and data type, total fill cells
  - `df.describe()` # mean std, min # statistical properties | apply only numeric columns

## Apply operations on columns

- Extract one column from DataFrame
  - `dataframe['column']`
    - add new column to DataFrame
    - get column with space between columns text `column name`
  - `dataframe.column`
    - cannot add column to DataFrame
    - cannot access column with text space
- Extract two or more columns from DataFrame
  - `dataframe['column1','column2']`
    - pass list into DataFrame
- Delete Column
- Apply Arithmetic operations
