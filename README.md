Superstore Sales Data Analysis
 Project Overview
This project performs Exploratory Data Analysis (EDA) on a Superstore sales dataset using Python. The analysis focuses on understanding sales performance, product categories, customer/order information, delivery time, discounts, and profit.
The project is implemented using a Jupyter Notebook/Google Colab environment.
 Objectives
•	Load and explore the Superstore dataset.
•	Understand the structure and characteristics of the data.
•	Check for missing values.
•	Convert order and shipping dates into proper datetime format.
•	Calculate delivery time in days.
•	Analyze sales by product category.
•	Visualize sales using charts.
•	Examine important business-related variables such as Sales, Quantity, Discount, and Profit.
 Technologies Used
•	Python
•	Pandas – Data loading, cleaning, manipulation, and analysis
•	NumPy – Numerical operations
•	Matplotlib – Data visualization
•	Seaborn – Statistical/data visualization
•	Google Colab / Jupyter Notebook
The notebook imports Pandas, NumPy, Matplotlib, and Seaborn.
 Dataset
The project uses a Superstore sales dataset containing 10,194 records and 21 original columns. The dataset includes information such as:
•	Row ID
•	Order ID
•	Order Date
•	Ship Date
•	Ship Mode
•	Customer ID
•	Customer Name
•	Segment
•	Country/Region
•	City
•	State/Province
•	Postal Code
•	Region
•	Product ID
•	Category
•	Sub-Category
•	Product Name
•	Sales
•	Quantity
•	Discount
•	Profit
The notebook additionally creates a Delivery Days column, making the analyzed dataset 22 columns wide.
 Data Processing
The notebook converts Order Date and Ship Date into datetime format and calculates delivery duration using:
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days
This allows delivery performance to be analyzed from the order and shipping dates.
 Data Quality Check
Missing values are checked using:
df.isnull().sum()
The notebook output shows 0 missing values across the analyzed columns.
Sales Analysis
The project groups sales by product category using:
category_sales = df.groupby('Category')['Sales'].sum()
The resulting total sales are:
Category	Total Sales
Furniture	754,747.7613
Office Supplies	731,893.3140
Technology	839,893.2790
Technology has the highest total sales among the three categories in the notebook results.
 Visualization
A bar chart is created to visualize total sales for each product category:
category_sales.plot(kind='bar', figsize=(8,5))
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.show()
This provides a simple visual comparison of sales performance across Furniture, Office Supplies, and Technology.
 Project Structure
Superstore-Sales-Analysis/
│
├── Superstore.ipynb
├── samplesuperstore - samplesuperstore.csv
└── README.md
▶️ How to Run
Google Colab
1.	Open Superstore.ipynb in Google Colab.
2.	Upload the Superstore CSV dataset.
3.	Make sure the CSV path in the notebook matches the uploaded file.
4.	Run the notebook cells from top to bottom.
5.	View the generated analysis and visualizations.
Jupyter Notebook
Install the required libraries:
pip install pandas numpy matplotlib seaborn
Then open:
jupyter notebook Superstore.ipynb
 Key Features
•	Dataset exploration
•	Data type inspection
•	Missing-value analysis
•	Date conversion
•	Delivery-time calculation
•	Category-wise sales analysis
•	Sales visualization
•	Statistical/data exploration

