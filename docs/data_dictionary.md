# Data Dictionary
## Austin Airbnb Pricing Intelligence — AUS-AIR-01

**Last updated:** April 2026
**Notebook:** 01_data_cleaning.ipynb
**Clean dataset:** data/processed/listings_clean.csv
**Rows:** 10,402 | **Columns:** 54

---

## Data Source

| Detail | Value |
|---|---|
| Source | Inside Airbnb — insideairbnb.com |
| City | Austin, Texas |
| Scrape date | April 2026 |
| Raw files | listings.csv, calendar.csv, reviews.csv |
| License | Creative Commons CC0 1.0 |

---

## Cleaning Decisions Log

Every decision made during cleaning is documented here.
This log exists so any stakeholder can audit our choices.

### 1. Column Reduction

**Decision:** Reduced from 79 columns to 37 before feature engineering.

**Columns dropped and why:**

| Column | Reason |
|---|---|
| `neighbourhood_group_cleansed` | 100% null — zero value |
| `calendar_updated` | 100% null — zero value |
| `license` | 100% null — zero value |
| `listing_url` | URL — not analytical |
| `picture_url` | URL — not analytical |
| `host_url` | URL — not analytical |
| `host_thumbnail_url` | URL — not analytical |
| `host_picture_url` | URL — not analytical |
| `calendar_last_scraped` | Scrape metadata — not analytical |
| `scrape_id` | Scrape metadata — not analytical |
| `last_scraped` | Scrape metadata — not analytical |
| `source` | Scrape metadata — not analytical |
| `neighborhood_overview` | 49.1% null — free text, not analytical |
| `neighbourhood` | 49.1% null — use neighbourhood_cleansed instead |
| `host_about` | 33.9% null — free text bio, not analytical |
| `host_location` | 17.8% null — where host lives, not relevant |
| `bathrooms_text` | Redundant — bathrooms numeric column sufficient |
| `minimum_minimum_nights` | Redundant with minimum_nights |
| `maximum_minimum_nights` | Redundant with minimum_nights |
| `minimum_maximum_nights` | Redundant with minimum_nights |
| `maximum_maximum_nights` | Redundant with minimum_nights |
| `minimum_nights_avg_ntm` | Redundant with minimum_nights |
| `maximum_nights_avg_ntm` | Redundant with minimum_nights |
| `maximum_nights` | Redundant with minimum_nights |
| `host_listings_count` | Redundant — use calculated version |
| `host_total_listings_count` | Redundant — use calculated version |
| `availability_60` | Redundant — keeping 30 and 365 only |
| `availability_90` | Redundant — keeping 30 and 365 only |
| `availability_eoy` | Redundant — keeping 30 and 365 only |
| `number_of_reviews_l30d` | Redundant — keeping ltm and total |
| `number_of_reviews_ly` | Redundant — keeping ltm and total |
| `calculated_host_listings_count_entire_homes` | Redundant — keeping total only |
| `calculated_host_listings_count_private_rooms` | Redundant — keeping total only |
| `calculated_host_listings_count_shared_rooms` | Redundant — keeping total only |
| `review_scores_accuracy` | Keeping rating, cleanliness, location only |
| `review_scores_checkin` | Keeping rating, cleanliness, location only |
| `review_scores_communication` | Keeping rating, cleanliness, location only |
| `review_scores_value` | Keeping rating, cleanliness, location only |
| `host_neighbourhood` | Not relevant to pricing |
| `host_verifications` | Not relevant to pricing |
| `host_has_profile_pic` | Not relevant to pricing |
| `has_availability` | Redundant with availability columns |
| `description` | Free text — not analytical |

---

### 2. Price Column Cleaning

**Problem:** Price stored as string `$120.00` — cannot do math on it.

**Decision:** Strip `$` and `,` characters, convert to float64.

**Outlier handling:**
- Min price before: $8.00
- Max price before: $50,000.00
- Mean before: $414.54
- **Cap applied: 99th percentile = $2,431.92**
- Listings removed: 122 (1.2% of data)
- Mean after: $205.10
- Median after: $134.00

**Rationale:** A $50,000/night listing is not real market competition
for a new host. Capping at 99th percentile removes extreme noise
while retaining 98.8% of the market.

---

### 3. Host Column Cleaning

| Column | Problem | Solution |
|---|---|---|
| `host_is_superhost` | Stored as `t`/`f` strings + 399 nulls | Converted to bool, nulls predicted via ML |
| `host_identity_verified` | Stored as `t`/`f` strings + nulls | Converted to bool, nulls filled with False |
| `host_response_rate` | Stored as `90%` string | Stripped `%`, converted to float64 |
| `host_acceptance_rate` | Stored as `85%` string | Stripped `%`, converted to float64 |
| `host_since` | Date string | Converted to datetime, engineered `host_experience_years` |

---

### 4. KNN Imputation

**Method:** KNNImputer from scikit-learn, k=5 neighbors

**Columns imputed:**

| Column | Nulls Before | Nulls After |
|---|---|---|
| `host_response_rate` | 845 (8.1%) | 0 |
| `host_acceptance_rate` | 546 (5.2%) | 0 |
| `bedrooms` | 13 (0.1%) | 0 |
| `bathrooms` | 6 (0.1%) | 0 |
| `beds` | 8 (0.1%) | 0 |

**Features used for imputation:**
`host_response_rate`, `host_acceptance_rate`, `host_experience_years`,
`calculated_host_listings_count`, `bedrooms`, `bathrooms`, `beds`,
`accommodates`, `availability_365`, `number_of_reviews`

**Note:** `host_is_superhost` was intentionally excluded from KNN
to preserve its nulls for ML classification.

**Data leakage:** None. Target variable `price` not used in imputation.

---

### 5. Superhost Classification

**Problem:** 399 listings had unknown superhost status.

**Decision:** Train Random Forest classifier instead of assuming False.

**Model:** RandomForestClassifier — n_estimators=100, max_depth=6,
class_weight=balanced, random_state=42

**Features used (leakage-free):**

| Feature | Importance |
|---|---|
| `number_of_reviews` | 52.4% |
| `calculated_host_listings_count` | 27.5% |
| `host_experience_years` | 12.0% |
| `availability_365` | 8.1% |

**Performance:**

| Metric | Score |
|---|---|
| Accuracy | 72.2% |
| Precision | 70.8% |
| Recall | 78.2% |
| F1 Score | 74.3% |

**Predictions:** 327 predicted superhost, 72 predicted not superhost

**Leakage note:** `host_response_rate`, `host_acceptance_rate`,
and `review_scores_rating` were intentionally excluded because
they are Airbnb's own superhost criteria — using them would
introduce circular reasoning.

---

### 6. Remaining Null Handling

| Column | Nulls | Strategy | Rationale |
|---|---|---|---|
| `host_name`, `host_since`, `host_experience_years` | 9 | Dropped rows | Same 9 listings — negligible loss |
| `host_response_time` | 845 | Filled with mode: `within an hour` | Most common value — defensible |
| `review_scores_rating` | 1,554 | Filled with median: 4.93 | New listings — no reviews yet |
| `review_scores_cleanliness` | 1,554 | Filled with median: 4.91 | New listings — no reviews yet |
| `review_scores_location` | 1,554 | Filled with median: 4.90 | New listings — no reviews yet |
| `reviews_per_month` | 1,554 | Filled with 0 | Correct value — no bookings yet |
| `first_review` | 1,554 | Filled with 'No reviews yet' | Honest label for new listings |
| `last_review` | 1,554 | Filled with 'No reviews yet' | Honest label for new listings |

**Note:** The 1,554 review nulls all belong to the same listings —
new listings that have never been reviewed. This is not random
missing data. It is a meaningful market signal.

---

### 7. Feature Engineering

**18 new columns created:**

#### Amenity Features (15 binary columns)
Extracted via case-insensitive keyword matching from `amenities` column.
The amenities column contained 4,433 unique strings across 458,540 mentions.
Keyword matching was chosen over exact matching to capture all variations.

| New Column | Keyword | Listings | % |
|---|---|---|---|
| `has_wifi` | wifi | 10,324 | 99.3% |
| `has_kitchen` | kitchen | 9,885 | 95.0% |
| `has_ac` | air conditioning | 9,889 | 95.1% |
| `has_washer` | washer | 9,184 | 88.3% |
| `has_free_parking` | free parking | 7,775 | 74.7% |
| `has_private_entrance` | private entrance | 5,537 | 53.2% |
| `has_bbq` | bbq | 4,428 | 42.6% |
| `has_outdoor_dining` | outdoor dining | 4,110 | 39.5% |
| `has_pets_allowed` | pets allowed | 4,089 | 39.3% |
| `has_pool` | pool | 3,754 | 36.1% |
| `has_fire_pit` | fire pit | 2,555 | 24.6% |
| `has_gym` | gym | 1,570 | 15.1% |
| `has_paid_parking` | paid parking | 1,050 | 10.1% |
| `has_hot_tub` | hot tub | 937 | 9.0% |
| `has_ev_charger` | ev charger | 765 | 7.4% |

#### Numeric Features (2 columns)

| New Column | Formula | Avg Value |
|---|---|---|
| `price_per_bedroom` | price ÷ bedrooms (studios treated as 1) | $99.58 |
| `amenity_count` | len(amenities_list) | — |

#### Boolean Feature (1 column)

| New Column | Logic | Count |
|---|---|---|
| `is_new_listing` | first_review == 'No reviews yet' | 1,552 (14.9%) |

**Dropped after engineering:** `amenities` (raw string — replaced by extracted features)

---

## Final Dataset Summary

| Metric | Value |
|---|---|
| File | data/processed/listings_clean.csv |
| Rows | 10,402 |
| Columns | 54 |
| File size | 3.73 MB |
| Total nulls | 0 |
| Duplicate rows | 0 |
| Price range | $8.00 — $2,400.00 |
| Price mean | $205.10 |
| Price median | $134.00 |

---

## Column Reference — All 54 Columns

| # | Column | Type | Description |
|---|---|---|---|
| 0 | `id` | int64 | Unique listing identifier |
| 1 | `name` | object | Listing title |
| 2 | `host_id` | int64 | Unique host identifier |
| 3 | `host_name` | object | Host first name |
| 4 | `host_since` | object | Date host joined Airbnb |
| 5 | `host_response_time` | object | Typical response time category |
| 6 | `host_response_rate` | float64 | % of inquiries host responds to |
| 7 | `host_acceptance_rate` | float64 | % of requests host accepts |
| 8 | `host_is_superhost` | bool | Superhost status (ML predicted for 399) |
| 9 | `host_identity_verified` | bool | Whether host identity is verified |
| 10 | `neighbourhood_cleansed` | int64 | Standardized neighborhood (ZIP code) |
| 11 | `latitude` | float64 | Listing latitude — for geo map |
| 12 | `longitude` | float64 | Listing longitude — for geo map |
| 13 | `property_type` | object | Type of property |
| 14 | `room_type` | object | Entire home / Private room / Shared room |
| 15 | `accommodates` | int64 | Max guest capacity |
| 16 | `bathrooms` | float64 | Number of bathrooms |
| 17 | `bedrooms` | float64 | Number of bedrooms |
| 18 | `beds` | float64 | Number of beds |
| 19 | `price` | float64 | Nightly price in USD — TARGET VARIABLE |
| 20 | `minimum_nights` | int64 | Minimum stay requirement |
| 21 | `availability_30` | int64 | Days available in next 30 days |
| 22 | `availability_365` | int64 | Days available in next 365 days |
| 23 | `number_of_reviews` | int64 | Total reviews — booking proxy |
| 24 | `number_of_reviews_ltm` | int64 | Reviews in last 12 months |
| 25 | `estimated_occupancy_l365d` | int64 | Estimated occupied nights last year |
| 26 | `estimated_revenue_l365d` | float64 | Estimated annual revenue |
| 27 | `first_review` | object | Date of first review |
| 28 | `last_review` | object | Date of most recent review |
| 29 | `review_scores_rating` | float64 | Overall guest rating |
| 30 | `review_scores_cleanliness` | float64 | Cleanliness rating |
| 31 | `review_scores_location` | float64 | Location rating |
| 32 | `instant_bookable` | object | Whether listing can be instantly booked |
| 33 | `calculated_host_listings_count` | int64 | Total listings this host manages |
| 34 | `reviews_per_month` | float64 | Booking velocity signal |
| 35 | `host_experience_years` | float64 | Years since host joined — engineered |
| 36 | `has_wifi` | bool | Listing has WiFi — engineered |
| 37 | `has_kitchen` | bool | Listing has kitchen — engineered |
| 38 | `has_free_parking` | bool | Listing has free parking — engineered |
| 39 | `has_paid_parking` | bool | Listing has paid parking — engineered |
| 40 | `has_ac` | bool | Listing has air conditioning — engineered |
| 41 | `has_washer` | bool | Listing has washer — engineered |
| 42 | `has_outdoor_dining` | bool | Listing has outdoor dining — engineered |
| 43 | `has_pets_allowed` | bool | Pets allowed — engineered |
| 44 | `has_bbq` | bool | Listing has BBQ grill — engineered |
| 45 | `has_fire_pit` | bool | Listing has fire pit — engineered |
| 46 | `has_private_entrance` | bool | Listing has private entrance — engineered |
| 47 | `has_pool` | bool | Listing has pool — engineered |
| 48 | `has_gym` | bool | Listing has gym — engineered |
| 49 | `has_ev_charger` | bool | Listing has EV charger — engineered |
| 50 | `has_hot_tub` | bool | Listing has hot tub — engineered |
| 51 | `amenity_count` | int64 | Total number of amenities — engineered |
| 52 | `price_per_bedroom` | float64 | Price divided by bedrooms — engineered |
| 53 | `is_new_listing` | bool | No reviews yet — engineered |