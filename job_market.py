import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

website = "https://realpython.github.io/fake-jobs/"

res = requests.get(website)
soup = BeautifulSoup(res.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

data = []

for j in jobs:
    title = j.find("h2", class_="title").text.strip()
    company = j.find("h3", class_="company").text.strip()

    data.append({
        "Job": title,
        "Company": company
    })

df = pd.DataFrame(data)

print("Total Jobs:", len(df))

company_count = df["Company"].value_counts().head(5)

print("\nTop Companies:")
print(company_count)


plt.figure()
plt.bar(company_count.index, company_count.values)

plt.title("Jobs by Company")
plt.xticks(rotation=45)

plt.show()