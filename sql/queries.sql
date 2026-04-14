# ─── Save all queries to sql/queries.sql ─────────────────────────────────────
queries_content = f"""
-- Austin Airbnb Pricing Intelligence
-- SQL Business Analysis — All 10 Queries
-- Project: AUS-AIR-01 | Notebook: 02_sql_analysis.ipynb

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 1 — Room Type Market Intelligence
-- Business question: What is the complete market picture by room type?
-- ─────────────────────────────────────────────────────────────────────────────
{query_1}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 2 — Neighborhood Price Intelligence
-- Business question: Which neighborhoods rank highest across all dimensions?
-- ─────────────────────────────────────────────────────────────────────────────
{query_2}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 3 — Neighborhood Opportunity Matrix
-- Business question: Which neighborhoods are underpriced relative to demand?
-- ─────────────────────────────────────────────────────────────────────────────
{query_3}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 4 — Property Type Deep Dive
-- Business question: Which property types command the strongest premiums?
-- ─────────────────────────────────────────────────────────────────────────────
{query_4}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 5 — Superhost Premium Analysis
-- Business question: Do superhosts charge more and earn more?
-- ─────────────────────────────────────────────────────────────────────────────
{query_5a}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 6 — Amenity Price Premium Matrix
-- Business question: Which amenities command the highest price premium?
-- ─────────────────────────────────────────────────────────────────────────────
{query_6}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 7 — Top Performer Profiling
-- Business question: What separates the top 10% from the bottom 10%?
-- ─────────────────────────────────────────────────────────────────────────────
{query_7}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 8 — Host Experience Curve
-- Business question: Does experience translate into measurable revenue growth?
-- ─────────────────────────────────────────────────────────────────────────────
{query_8}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 9 — New Host Competitive Positioning
-- Business question: What price range should a new host target?
-- ─────────────────────────────────────────────────────────────────────────────
{query_9}

-- ─────────────────────────────────────────────────────────────────────────────
-- QUERY 10 — Revenue Optimization Matrix
-- Business question: Which combination produces the highest annual revenue?
-- ─────────────────────────────────────────────────────────────────────────────
{query_10}
"""

with open('../sql/queries.sql', 'w') as f:
    f.write(queries_content)

print("QUERIES SAVED")
print("=" * 45)
print("  File : sql/queries.sql")
print("  All 10 queries saved as standalone SQL file")