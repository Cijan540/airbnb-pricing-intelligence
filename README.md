# Austin Airbnb Pricing Intelligence
### What should a new Airbnb host in Austin charge per night to maximize revenue?

**Project ID:** AUS-AIR-01 | **Status:** Complete | **Built by:** Cizen Bhatta

---

## The Business Problem

A new Airbnb host in Austin, Texas has no structured way to determine:
- What nightly rate to charge
- Which neighborhood offers the best return
- What amenities drive price premiums
- How to transition from new listing to established performer

This project delivers a complete pricing intelligence analysis of the Austin
Airbnb market using real scraped data from Inside Airbnb. Every step is
documented, version-controlled, and presented as a professional
data analyst engagement.

---

## Deliverables

| Notebook | Focus | Output |
|---|---|---|
| 1 | Data cleaning and feature engineering | `listings_clean.csv` · 10,402 rows · 54 features |
| 2 | SQL business analysis | 10 queries · `queries.sql` |
| 3 | EDA and IBCS visualization | 10 IBCS-compliant charts |
| 4 | Linear regression pricing model | R² 0.605 · 72 features · 3 worked predictions |
| 5 | Geographic map | [Interactive HTML map](outputs/austin_listings_map.html) |

---

## Data Source

**Inside Airbnb** — [insideairbnb.com](https://insideairbnb.com/get-the-data/) — Austin, TX
Real scraped market data. Not a Kaggle dataset.

| File | Rows | Columns |
|---|---|---|
| listings.csv | 10,533 | 79 |
| calendar.csv | 3,844,547 | 7 |
| reviews.csv | 588,362 | 6 |

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
| Version control | GitHub |

---

## Key Findings

### The Austin Market

- **10,402 entire home listings** after cleaning and outlier removal
- **Median price: $144/night** — mean overstates market by 54%
- **Entire homes dominate** — 86.6% of listings generate 97.1% of revenue
- **52.5% superhost rate** — mature competitive market
- **14.9% of listings have no reviews yet** — the cold start segment

### What Drives Price (Model Coefficients)

| Driver | Impact | Note |
|---|---|---|
| Bathrooms | +25% per bathroom | Strongest single predictor |
| Bedrooms | +8% per bedroom | Second strongest |
| Accommodates | +4% per guest | Capacity signal |
| Hot tub | +$39/night | #1 amenity (controlled) |
| Pool | +$34/night | Strong premium |
| BBQ grill | +$23/night | Austin outdoor signal |
| Superhost status | -$14/night | Volume strategy, not premium |

### Where to List — Tier 1 Neighborhoods

| Neighborhood | Avg Price | Annual Revenue | Occupancy |
|---|---|---|---|
| 78736 | $237 | $29,600 | 111.7 nights |
| 78732 | $392 | $25,089 | 93.7 nights |
| 78702 | $242 | $22,376 | 112.2 nights |
| 78729 | $188 | $19,393 | 108.0 nights |

### The Optimal Host Strategy

| Decision | Recommendation |
|---|---|
| Neighborhood | 78702 or 78704 |
| Property size | 4-5 bedrooms |
| Must-have amenities | Pool + BBQ |
| Aspirational amenity | Hot tub |
| Entry price | 15% below neighborhood market average |
| Year one target | Superhost status |
| Expected year one | $6K–$12K revenue |
| Post-superhost | $22K+ annual revenue |

---

## Methodology Highlights

- **ML imputation** — KNN and Random Forest for missing data recovery
- **IBCS visualization** — International Business Communication Standards applied to all charts
- **Feature engineering** — 18 new columns from raw data
- **VIF multicollinearity analysis** — identified and removed 34 redundant features
- **Log transformation** — addressed right-skew in price distribution
- **Incremental modeling** — built 5 models sequentially to measure each feature block
- **Standardized coefficients** — fair comparison across features of different scales
- **Honest limitations disclosure** — clear documentation of where the model underperforms

---

## Repository Structure

| Path | Contents |
|---|---|
| `data/raw/` | Original unmodified CSV files from Inside Airbnb |
| `data/processed/` | Clean datasets (`listings_clean.csv`, `airbnb_austin.db`) |
| `notebooks/` | 5 Jupyter notebooks — one per analysis phase |
| `sql/queries.sql` | All 10 SQL queries as a standalone file |
| `outputs/figures/` | 12 IBCS-compliant visualizations as PNG |
| `outputs/austin_listings_map.html` | Interactive map of all 10,402 listings |
| `docs/data_dictionary.md` | Complete documentation of every cleaning decision |

---

## How to Explore This Project

**Start here:**
1. Open `outputs/austin_listings_map.html` in any browser — see the market visually
2. Scroll through `notebooks/03_eda_visualization.ipynb` — read the 10 IBCS charts
3. Read `docs/data_dictionary.md` — see every cleaning and feature decision
4. Review `sql/queries.sql` — read the 10 business queries

**For recruiters and hiring managers:**
The five notebooks tell a complete analytical story from raw data
to production-ready pricing recommendations. Each notebook opens
with a business context and closes with a summary of findings.
Every decision is documented. Every number is traceable.

---

*Built with real public data. Every decision documented. Nothing hidden.*

*Dataset: [insideairbnb.com](https://insideairbnb.com/get-the-data/) — Austin, Texas*
*Tools: Python · SQL · Folium · GitHub*