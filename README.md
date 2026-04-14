# Austin Airbnb Pricing Intelligence
### What should a new Airbnb host in Austin charge per night to maximize revenue?

**Project ID:** AUS-AIR-01 | **Status:** In Progress | **Phase:** Notebook 2 of 5

---

## The Business Problem

A new Airbnb host in Austin, Texas has no structured way to determine:
- What nightly rate to charge
- Which neighborhood offers the best return
- What amenities drive price premiums
- What review score threshold keeps a listing competitive

This project delivers a full pricing intelligence analysis of the Austin
Airbnb market using real scraped data from Inside Airbnb — not a cleaned
Kaggle dataset. Every step is documented, version-controlled, and presented
as a professional data analyst engagement.

---

## Project Structure

---

## Data Source

**Inside Airbnb** — insideairbnb.com — Austin, TX
Real scraped market data. Not a Kaggle dataset.

| File | Rows | Columns | Description |
|---|---|---|---|
| listings.csv | 10,533 | 79 | Every active Airbnb listing in Austin |
| calendar.csv | 3,844,547 | 7 | 365 days of pricing data per listing |
| reviews.csv | 588,362 | 6 | Guest reviews across all listings |

---

## Technology Stack

| Category | Tool |
|---|---|
| Language | Python 3.10+ |
| Notebook | Jupyter via VS Code |
| Data wrangling | Pandas, NumPy |
| ML imputation | Scikit-learn (KNN, Random Forest) |
| Database | SQLite |
| Visualization | Matplotlib, Seaborn, Folium |
| Dashboard | Tableau Public |
| Version control | GitHub |

---

## Notebook 1 — Data Cleaning ✅

**What was done:**

Starting point: 10,533 raw listings × 79 columns
Final output: 10,402 clean listings × 54 columns — saved to `data/processed/listings_clean.csv`

**Key decisions made:**

| Decision | Detail |
|---|---|
| Column reduction | Dropped 42 columns — URLs, 100% nulls, redundant |
| Price cleaning | Stripped `$` and `,` — converted to float64 |
| Outlier removal | Capped at 99th percentile ($2,431) — removed 122 listings |
| KNN imputation | k=5 — filled nulls in response rate, acceptance rate, bedrooms, bathrooms, beds |
| Superhost prediction | Random Forest — predicted 399 unknown labels — 72.2% accuracy |
| Review score nulls | Filled with median — new listings with no reviews yet |
| Feature engineering | 18 new columns — amenities, price per bedroom, new listing flag |

**Key market findings so far:**

- Median Austin price: **$134/night**
- Average host experience: **8.5 years** — mature, competitive market
- Superhost rate: **52.5%** of listings
- WiFi penetration: **99.3%** — table stakes, not a differentiator
- Pool penetration: **36.1%** — higher than expected
- BBQ penetration: **42.6%** — Austin outdoor culture confirmed
- New listings: **14.9%** of the market have no reviews yet

---

## Notebook 2 — SQL Business Analysis 🔄

*In progress — 10 business queries answering the core pricing question*

---

## Repository Structure

| Path | Contents |
|---|---|
| `data/raw/` | Original unmodified CSV files from Inside Airbnb |
| `data/processed/` | Clean, feature-engineered datasets |
| `notebooks/` | Jupyter notebooks — one per analysis phase |
| `sql/queries.sql` | All 10 SQL queries as a standalone file |
| `outputs/figures/` | All charts exported as PNG |
| `docs/` | Project charter and data dictionary |

---

## Documents

- [Project Charter](docs/project_charter.docx)
- [Data Dictionary](docs/data_dictionary.md)

---

*This project is part of a data analyst portfolio.
Built with real public data. Every decision documented.*