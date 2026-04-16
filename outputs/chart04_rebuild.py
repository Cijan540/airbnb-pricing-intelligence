import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np
from adjustText import adjust_text

# ── Data ─────────────────────────────────────────────────────────────────────
df = pd.read_csv("s:/Projects for my portfolio/my_airbnb_project/data/processed/listings_clean.csv")
entire = df[df["room_type"] == "Entire home/apt"].copy()

grouped = (
    entire.groupby("neighbourhood_cleansed")
    .agg(avg_price=("price", "mean"),
         avg_occupancy=("estimated_occupancy_l365d", "mean"),
         listing_count=("id", "count"))
    .reset_index()
)
data = grouped[grouped["listing_count"] >= 20].copy()
data["zip"] = data["neighbourhood_cleansed"].astype(str)

mkt_price = data["avg_price"].mean()
mkt_occ   = data["avg_occupancy"].mean()

def quadrant(row):
    if   row["avg_price"] <  mkt_price and row["avg_occupancy"] >= mkt_occ: return "Q1"
    elif row["avg_price"] >= mkt_price and row["avg_occupancy"] >= mkt_occ: return "Q2"
    elif row["avg_price"] <  mkt_price and row["avg_occupancy"] <  mkt_occ: return "Q3"
    else:                                                                    return "Q4"

data["quadrant"] = data.apply(quadrant, axis=1)

q_meta = {
    "Q1": {"label": "Q1 — Underpriced Opportunity", "color": "#27AE60"},
    "Q2": {"label": "Q2 — Premium Market",          "color": "#2980B9"},
    "Q3": {"label": "Q3 — Low Price · Low Demand",  "color": "#95A5A6"},
    "Q4": {"label": "Q4 — Overpriced · Low Demand", "color": "#E74C3C"},
}

# ── Figure: plot area left, legend panel right ────────────────────────────────
fig = plt.figure(figsize=(17, 10), facecolor="#FAFAFA")
# Left: plot (80% width). Right 20% is for legends.
ax = fig.add_axes([0.07, 0.10, 0.68, 0.76])   # [left, bottom, width, height]
ax.set_facecolor("#FAFAFA")

x_min, x_max = 50, 620
y_min, y_max = 40, 140

# Quadrant shading
for q, (xl, xr, yb, yt) in {
    "Q1": (x_min, mkt_price, mkt_occ, y_max),
    "Q2": (mkt_price, x_max,  mkt_occ, y_max),
    "Q3": (x_min, mkt_price, y_min,   mkt_occ),
    "Q4": (mkt_price, x_max,  y_min,   mkt_occ),
}.items():
    ax.fill_between([xl, xr], [yb, yb], yt,
                    color=q_meta[q]["color"], alpha=0.07, zorder=0)

# Crosshairs
ax.axvline(mkt_price, color="#777", lw=1.1, ls="--", alpha=0.5, zorder=1)
ax.axhline(mkt_occ,   color="#777", lw=1.1, ls="--", alpha=0.5, zorder=1)

# Bubbles + zip labels
max_count  = data["listing_count"].max()
size_scale = (data["listing_count"] / max_count) * 900 + 60
texts = []
for q, meta in q_meta.items():
    sub = data[data["quadrant"] == q]
    ax.scatter(sub["avg_price"], sub["avg_occupancy"],
               s=size_scale[sub.index], color=meta["color"],
               alpha=0.82, edgecolors="white", linewidths=1.4, zorder=3)
    for _, row in sub.iterrows():
        txt = ax.text(row["avg_price"], row["avg_occupancy"], row["zip"],
                      fontsize=7.5, fontweight="bold", color="#1a1a1a",
                      ha="center", va="center", zorder=5)
        texts.append(txt)

adjust_text(
    texts, ax=ax,
    expand=(1.8, 2.2),
    arrowprops=dict(arrowstyle="-", color="#BBBBBB", lw=0.6, shrinkA=3, shrinkB=3),
    force_text=(0.9, 1.3),
    force_points=(0.4, 0.6),
    x_lim=(x_min, x_max),
    y_lim=(y_min, y_max),
)

# Market avg callout labels
ax.text(mkt_price + 6, y_min + 2, f"Market avg\n${mkt_price:,.0f}/night",
        fontsize=8, color="#666", va="bottom")
ax.text(x_min + 5, mkt_occ + 1.5, f"Market avg  {mkt_occ:.0f} nights",
        fontsize=8, color="#666", va="bottom")

# Axes styling
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xlabel("Average Nightly Price (USD)", fontsize=11, labelpad=8, color="#333")
ax.set_ylabel("Average Occupied Nights / Year", fontsize=11, labelpad=8, color="#333")
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${int(x):,}"))
ax.tick_params(axis="both", labelsize=9, colors="#555")
ax.spines[["top", "right"]].set_visible(False)
ax.spines[["left", "bottom"]].set_color("#CCC")
ax.grid(axis="both", ls=":", color="#DDD", lw=0.8, zorder=0)

# ── Legend panel (right side, figure coordinates) ────────────────────────────
# Quadrant legend — using fig.text + colored rectangles via fig.add_axes trick
# Simpler: draw a dedicated legend axes
leg_ax = fig.add_axes([0.78, 0.10, 0.20, 0.76])
leg_ax.set_axis_off()
leg_ax.set_facecolor("#FAFAFA")

# Quadrant section
leg_ax.text(0.05, 0.97, "Quadrant", fontsize=10, fontweight="bold",
            color="#333", va="top", transform=leg_ax.transAxes)

q_items = list(q_meta.items())
for i, (q, meta) in enumerate(q_items):
    y = 0.90 - i * 0.09
    rect = mpatches.FancyBboxPatch((0.05, y - 0.025), 0.12, 0.05,
                                    boxstyle="round,pad=0.005",
                                    facecolor=meta["color"], edgecolor="white",
                                    transform=leg_ax.transAxes, clip_on=False)
    leg_ax.add_patch(rect)
    star = "  ★" if q == "Q1" else ""
    leg_ax.text(0.22, y, meta["label"] + star, fontsize=8.5, color="#222",
                va="center", transform=leg_ax.transAxes)

# Bubble size section
leg_ax.text(0.05, 0.50, "Bubble size", fontsize=10, fontweight="bold",
            color="#333", va="top", transform=leg_ax.transAxes)
leg_ax.text(0.05, 0.44, "= listing count", fontsize=8, color="#666",
            va="top", transform=leg_ax.transAxes)

for i, n in enumerate([50, 250, 800]):
    y = 0.34 - i * 0.10
    r = np.sqrt((n / max_count) * 900 + 60) * 0.0038   # normalise to axes coords
    circle = plt.Circle((0.11, y), r, color="#AAAAAA", ec="white", lw=1,
                         transform=leg_ax.transAxes, clip_on=False)
    leg_ax.add_patch(circle)
    leg_ax.text(0.22, y, f"{n} listings", fontsize=8.5, color="#444",
                va="center", transform=leg_ax.transAxes)

# ── Title (constrained to plot width, above ax) ───────────────────────────────
q1_count = len(data[data["quadrant"] == "Q1"])
fig.text(0.07, 0.895,
         f"{q1_count} Austin Neighborhoods Are Underpriced\nRelative to Demand — Pricing Upside Exists",
         fontsize=13, fontweight="bold", color="#1a1a1a", va="bottom", linespacing=1.4)
fig.text(0.07, 0.875,
         "Entire home/apt  ·  Min 20 listings  ·  Bubble size = listing count  ·  Dashed lines = market averages",
         fontsize=8.5, color="#888", va="top")

fig.text(0.07, 0.015, "Source: Inside Airbnb · Austin TX · 2026",
         fontsize=8, color="#AAAAAA")

out = "s:/Projects for my portfolio/my_airbnb_project/outputs/figures/chart_04_opportunity_matrix.png"
fig.savefig(out, dpi=160, bbox_inches="tight", facecolor="#FAFAFA")
print("Saved:", out)
plt.close()
