#Sales data Analysis Project
This project analyzez sales data using Python.

## Features 
- Load dataset using pandas
- Calculate sales statistics
- Identify highest and lowest selling product 
- Generate sales bar chart

## Technologies used
- Python
- pandas
- Matplotlib
- vs code

## output
- Total sales
- Average sales
- Highest selling product 
- Lowest selling product
- sales chart visualization

## How to Run
Install libraries:
pip install pandas matplotlib openpyxl
Run the program 
python main.py

## Security & Sandbox (Week 3)

To ensure safe execution, the project runs inside a Docker container.

Security features:
- Code execution isolated using Docker
- Only required libraries installed (pandas, matplotlib, openpyxl)
- Prevents unauthorized access to the host system

Run using Docker:

docker build -t statbotpro .
docker run statbotpro