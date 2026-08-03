# Vegetable Dataset Processing using MapReduce (Python)

## Project Overview

This project implements a **MapReduce-based Vegetable Dataset Processing
System** using Python. It includes Mapper, Partitioner, Sorter, Reducer,
and a Master program to process a vegetable dataset.

## Project Structure

    VegetableDatasetProject/
    ├── VegetableDataset.csv
    ├── VegetableMapper.py
    ├── VegetablePartitioner.py
    ├── VegetableSorter.py
    ├── VegetableReducer.py
    ├── VegetableMaster.py
    └── README.md

## Technologies

-   Python 3.x
-   VS Code
-   CSV Dataset

## Workflow

1.  Mapper
2.  Partitioner
3.  Sorter
4.  Reducer

## Run

``` bash
cd "C:\Big Data\week 2"
python VegetableMaster.py VegetableDataset.csv
```

## Features

-   Python MapReduce implementation
-   Modular code
-   Vegetable dataset processing
-   Easy to understand


# Superstore Sales Data Analysis

## Project Overview

This project performs exploratory data analysis (EDA) on the **Sample Superstore** dataset using Python. It analyzes sales data, identifies missing values, visualizes business insights, and prepares the dataset for further machine learning tasks.

## Features

* Loads the Superstore dataset
* Displays the first five records
* Shows dataset information
* Checks for missing values
* Calculates average sales using NumPy and SciPy
* Groups sales by product category
* Creates a bar chart of category-wise sales
* Creates a scatter plot of Sales vs Profit
* Splits the dataset into training and testing sets

## Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* SciPy
* Google Colab

## Project Structure

```
Superstore-Sales-Analysis/
│
├── superstore_py.py
├── samplesuperstore - samplesuperstore.csv
├── README.md
```

## Dataset

**Dataset Name:** Sample Superstore

The dataset contains information about:

* Orders
* Customers
* Products
* Categories
* Sales
* Profit
* Discounts
* Regions
* Shipping Details

## Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

## How to Run

### Google Colab

1. Upload `superstore_py.py`.
2. Upload `samplesuperstore - samplesuperstore.csv` when prompted.
3. Run all cells.

### Local System

Place both files in the same folder and run:

```bash
python superstore_py.py
```

## Output

The program generates:

* Dataset preview
* Dataset information
* Missing value report
* Average sales
* Category-wise sales summary
* Bar chart of Sales by Category
* Scatter plot of Sales vs Profit
* Training and testing dataset sizes

## Future Enhancements

* Sales prediction using Machine Learning
* Interactive dashboards with Plotly
* Customer segmentation
* Profit forecasting
* Regional sales analysis
* Time-series sales trends

## Author

**Chan T**

## License

This project is intended for educational and academic purposes.


## Author

Chan T
