
# Job Market Analysis Project

## Project Overview
This project uses web scraping to collect and analyze job postings from an online job listings website.  
It demonstrates how real-world job data can be extracted, structured, and analyzed using Python.

---

## Implementation

### Data Collection
- The data is collected using the `requests` library to access the website  
- HTML content is parsed using `BeautifulSoup`  
- Extracted information includes:
  - Job Titles
  - Company Names  

---

### Data Processing
- Extracted data is stored in a Pandas DataFrame  
- Data is structured into columns: Job and Company  

---

### Data Analysis
- Calculate total number of job postings  
- Count number of jobs per company using `value_counts()`  
- Identify the top 5 companies with the most job postings  

---

### Data Visualization
- A bar chart is created using `matplotlib`  
- The chart displays the top companies based on job frequency  
- X-axis represents company names  
- Y-axis represents number of job postings  

---

## Tools & Technologies
- Python  
- Requests  
- BeautifulSoup  
- Pandas  
- Matplotlib  

---

## Project Files
- job_market.py
- requirements.txt
- README.md  
