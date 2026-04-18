# Austin Airbnb Pricing Intelligence
### What should a new Airbnb host in Austin charge per night to maximize revenue?

**Project ID:** AUS-AIR-01 | **Status:** In Progress | **Phase:** Notebook 5 of 5

---

## The Business Problem

A new Airbnb host in Austin, Texas has no structured way to determine:
- What nightly rate to charge
- Which neighborhood offers the best return
- What amenities drive price premiums
- What review score threshold keeps a listing competitive

This project delivers a complete pricing intelligence analysis of the Austin
Airbnb market using real scraped data from Inside Airbnb — not a cleaned
Kaggle dataset. Every step is documented, version-controlled, and presented
as a professional data analyst engagement.

---

## Project Structure

| Notebook | Focus | Status |
|---|---|---|
| 1 | Data cleaning and feature engineering | ✅ Complete |
| 2 | SQL business analysis (10 queries) | ✅ Complete |
| 3 | EDA and IBCS visualization (10 charts) | ✅ Complete |
| 4 | Linear regression pricing model | ✅ Complete |
| 5 | Geographic map | 🔄 In Progress |

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
| ML | Scikit-learn (KNN, Random Forest, Linear Regression) |
| Statistical analysis | Statsmodels (VIF, p-values) |
| Database | SQLite |
| Visualization | Matplotlib, Seaborn (IBCS standards) |
| Mapping | Folium |
| Dashboard | Tableau Public |
| Version control | GitHub |

---

## Key Findings

### The Austin Market

- **10,402 entire home listings** after cleaning and outlier removal
- **Median price: $144/night** — mean overstates market by 54%
- **Entire homes dominate** — 86.6% of listings, 97.1% of revenue
- **52.5% superhost rate** — mature competitive market
- **14.9% of listings are new** with no reviews yet

### What Drives Price (From the Model)

| Driver | Impact | Interpretation |
|---|---|---|
| Bathrooms | +25% per bathroom | Strongest single predictor |
| Accommodates | +4% per guest | Property capacity matters |
| Bedrooms | +8% per bedroom | Still meaningful |
| Hot tub | +$39/night | #1 amenity (controlled) |
| Pool | +$34/night | Strong premium |
| BBQ grill | +$23/night | Austin outdoor signal |
| Superhost | -$14/night | Volume strategy, not premium |

### Where to List — Tier 1 Neighborhoods

| Neighborhood | Avg Price | Annual Revenue | Occupancy |
|---|---|---|---|
| 78736 | $237 | $29,600 | 111.7 nights |
| 78732 | $392 | $25,089 | 93.7 nights |
| 78702 | $242 | $22,376 | 112.2 nights |
| 78729 | $188 | $19,393 | 108.0 nights |

### The Optimal Host Strategy

**For a new Austin host targeting maximum revenue:**

| Decision | Recommendation |
|---|---|
| Neighborhood | 78702 or 78704 |
| Property size | 4-5 bedrooms |
| Must-have amenities | Pool + BBQ |
| Aspirational | Hot tub |
| Entry price | 15% below neighborhood market average |
| Year one target | Superhost status |
| Expected year one | $6K–$12K revenue |
| Post-superhost | $22K+ annual revenue |

---

## The Pricing Model

Linear regression on 72 features after multicollinearity analysis.

| Metric | Value |
|---|---|
| R² (test) | 0.605 |
| MAE (test) | $85 |
| Training rows | 7,210 |
| Test rows | 1,803 |
| Features | 72 (after VIF reduction from 106) |

**Honest limitations:** The model underpredicts luxury properties by 40%+ —
linear regression is not the right tool for the premium tier.
For budget and mid-market properties the model is accurate within 20-30%.

---

## Repository Structure

| Path | Contents |
|---|---|
| `data/raw/` | Original unmodified CSV files from Inside Airbnb |
| `data/processed/` | Clean datasets (listings_clean.csv, airbnb_austin.db) |
| `notebooks/` | Jupyter notebooks — one per analysis phase |
| `sql/queries.sql` | All 10 SQL queries as a standalone file |
| `outputs/figures/` | 12 IBCS charts exported as PNG |
| `docs/` | Project charter and data dictionary |

---

## Documentation

- [Data Dictionary](docs/data_dictionary.md) — every cleaning decision logged
- [SQL Queries](sql/queries.sql) — all 10 queries with business context
- [Figures](outputs/figures/) — 12 IBCS-compliant visualizations

---

## Methodology Highlights

- **ML imputation** — KNN and Random Forest for missing data recovery
- **IBCS visualization** — International Business Communication Standards applied to every chart
- **Feature engineering** — 18 new columns including amenity binaries and derived ratios
- **VIF multicollinearity analysis** — identified and eliminated severe collinearity in 16 features
- **Log transformation** — addressed right-skew in price distribution
- **Incremental modeling** — built 5 models sequentially to measure each feature block's contribution
- **Standardized coefficients** — fair comparison across features of different scales

---

*Built by Cizen Bhatta*
*Analyst Portfolio Project*
*Dataset: [insideairbnb.com](https://insideairbnb.com/get-the-data/) — Austin, Texas*
*Tools: Python · SQL · Tableau · GitHub*