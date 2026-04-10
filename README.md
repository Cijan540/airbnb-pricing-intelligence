# Austin Airbnb Pricing Intelligence
### What the Data Says About Hosting Smart in Austin, Texas

---

## The Problem

Most new Airbnb hosts in Austin price by gut feeling.

They look at a few nearby listings, pick a number that feels reasonable, 
and hope for the best. Some undercharge and leave hundreds of dollars 
on the table every month. Others overprice and watch their calendar 
stay empty while competitors with identical properties stay booked.

The difference between those two outcomes is not luck. It is data.

This project exists to answer one specific business question with evidence:

> **What should a new Airbnb host in Austin charge per night to maximize 
> revenue, and which neighborhoods and property features drive the 
> highest returns?**

---

## What This Analysis Covers

This is not a cleaned Kaggle dataset with pre-answered questions.
This is real scraped data from Inside Airbnb — messy, inconsistent, 
and full of the exact data quality issues a working analyst encounters 
on the job.

The analysis moves through five distinct phases, each building on 
the last:

**Phase 1 — Data Cleaning**  
The raw listings data arrives with prices stored as strings like 
$120.00, nulls scattered across key fields, neighborhood names that 
do not match across files, and outlier listings priced at $10,000 
a night. Every cleaning decision is documented with the reasoning 
behind it — not just what was done but why.

**Phase 2 — SQL Business Analysis**  
Ten business questions answered entirely in SQL. Which neighborhoods 
command the highest median price? Which property type earns the most 
per bedroom? How does review score correlate with nightly rate? 
What amenities appear most in listings priced above $200 a night? 
Each query comes with a plain-English finding written for a 
non-technical reader.

**Phase 3 — Exploratory Visualization**  
Price distributions by neighborhood, room type performance, review 
score impact on revenue, and seasonal demand patterns from the 
calendar data. Every chart is framed around a business question, 
not just a label.

**Phase 4 — Geographic Pricing Map**  
An interactive map of Austin with every listing plotted and colored 
by price tier. This is the visualization that makes the neighborhood 
story impossible to ignore. Exported as a standalone HTML file that 
runs in any browser.

**Phase 5 — Pricing Model**  
A linear regression model trained to predict nightly price from 
bedrooms, bathrooms, neighborhood, room type, and review score. 
The output is not just an accuracy score — it is a set of 
interpretable coefficients that answer questions like: how much 
does each additional bedroom add to the nightly rate in Austin? 
What is the dollar value of a one-point improvement in review score?

---

## Tools and Technologies

| Layer | Tool | Role in This Project |
|-------|------|----------------------|
| Language | Python 3.10+ | End-to-end analysis |
| Data wrangling | Pandas, NumPy | Cleaning, transformation, feature engineering |
| Database | SQLite | Business query layer |
| Visualization | Matplotlib, Seaborn | EDA charts and model outputs |
| Geospatial | Folium | Interactive neighborhood pricing map |
| Machine learning | Scikit-learn | Linear regression pricing model |
| Dashboard | Tableau Public | Executive-facing four-view dashboard |
| Environment | Jupyter Notebook | Documented analysis with narrative |
| Version control | GitHub | Full project history and portfolio hosting |

---

## Dataset

**Source:** Inside Airbnb — insideairbnb.com  
**City:** Austin, Texas  
**Files:** listings.csv, calendar.csv, reviews.csv  

Inside Airbnb scrapes publicly available Airbnb listing data 
periodically and makes it available for research and analysis. 
The data is real, unfiltered, and reflects actual listings on 
the platform at the time of the scrape. This is not a curated 
teaching dataset — which is exactly why it is worth analyzing.

---

## Repository Structure

MY_AIRBNB_PROJECT/
│
├── data/
│   ├── raw/
│   │   ├── listings.csv
│   │   ├── calendar.csv
│   │   └── reviews.csv
│   └── processed/
│       └── listings_clean.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_sql_analysis.ipynb
│   ├── 03_eda_visualization.ipynb
│   ├── 04_pricing_model.ipynb
│   └── 05_geo_map.ipynb
│
├── sql/
│   └── queries.sql
│
├── outputs/
│   ├── austin_listings_map.html
│   └── figures/
│
├── docs/
│   └── project_charter.docx
│
├── requirements.txt
└── README.md

---

## Project Status

| Phase | Deliverable | Status |
|-------|-------------|--------|
| Data acquisition | Raw CSVs downloaded from Inside Airbnb | Done |
| Data cleaning | Cleaned dataset with engineered features | In Progress |
| SQL analysis | 10 business queries with narrative findings | Pending |
| Geographic map | Interactive HTML map by price tier | Pending |
| Pricing model | Regression model with dollar coefficients | Pending |
| Dashboard | Tableau Public — four business views | Pending |
| Strategy guide | Full host recommendation README | Pending |

---

## Key Findings

*The analysis is in progress. This section will be updated with 
specific findings including neighborhood price benchmarks, 
amenity premiums, seasonal pricing patterns, and model 
coefficients with exact dollar values once each phase is complete.*

---

## For a New Austin Host

*Upon project completion this section will contain a direct, 
data-backed answer to the core business question — what to charge, 
where to list, what amenities to highlight, and what review score 
to target to stay competitive in the Austin market.*

---

**Built by Cizen Bhatta**  
Analyst Portfolio Project  
Dataset: (https://insideairbnb.com/get-the-data/) — Austin, Texas  
Tools: Python · SQL · Tableau · GitHub