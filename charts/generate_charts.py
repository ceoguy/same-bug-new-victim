#!/usr/bin/env python3
"""
Generate the three charts referenced in the report.
Outputs: charts/01_april_incidents.png, 02_14_month_arc.png, 03_tvl_exodus.png
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from pathlib import Path

OUT = Path(__file__).parent
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.size": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.labelweight": "bold",
    "axes.titleweight": "bold",
    "figure.dpi": 150,
    "text.usetex": False,
    "axes.formatter.use_mathtext": False,
})
import matplotlib
matplotlib.rcParams['text.parse_math'] = False

# ---------- Chart 1: April 2026 incidents by loss size ----------
incidents = [
    ("KelpDAO", 292),
    ("Drift", 285),
    ("Rhea Finance", 18.4),
    ("Grinex", 15.0),
    ("Wasabi", 5.0),
    ("Volo Vault", 3.5),
    ("Sweat Foundation", 3.5),
    ("Hyperbridge", 2.5),
    ("Other (22 sub-$2M)", 5.0),
]
labels = [x[0] for x in incidents]
losses = [x[1] for x in incidents]
colors = ["#c0392b", "#c0392b"] + ["#7f8c8d"] * (len(incidents) - 2)

fig, ax = plt.subplots(figsize=(12, 5.625))
bars = ax.barh(labels, losses, color=colors)
ax.invert_yaxis()
ax.set_xscale("log")
ax.set_xlabel("USD lost (millions, log scale)")
ax.set_title("April 2026 Web3 incidents, by loss size")
for bar, val in zip(bars, losses):
    ax.text(val * 1.05, bar.get_y() + bar.get_height() / 2,
            f"${val:.1f}M", va="center", fontsize=10)
ax.set_xlim(1, 1000)
fig.text(0.5, 0.01, "Two attacks ($577M) = 93% of monthly losses. The other 28 = $48M.",
         ha="center", fontsize=10, style="italic", color="#555")
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(OUT / "01_april_incidents.png", bbox_inches="tight")
plt.close()
print("01_april_incidents.png")

# ---------- Chart 2: 14-month arc ----------
events = [
    ("Bybit\nFeb 2025", 1460, "UI / supply-chain\n(Safe wallet JS injection)"),
    ("Drift\nApr 2026", 285, "Signer social engineering\n(durable nonces)"),
    ("KelpDAO\nApr 2026", 292, "Off-chain verifier\n(RPC poisoning)"),
]
fig, ax = plt.subplots(figsize=(12, 5.625))
xs = list(range(len(events)))
losses2 = [e[1] for e in events]
bars = ax.bar(xs, losses2, color="#c0392b", width=0.55)
ax.set_xticks(xs)
ax.set_xticklabels([e[0] for e in events])
ax.set_ylabel("USD lost (millions)")
ax.set_title("Three nine-figure incidents. Zero contract bugs.")
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${int(x):,}M"))
for bar, e in zip(bars, events):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 30,
            e[2], ha="center", fontsize=9, color="#333")
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2,
            f"${e[1]:,}M", ha="center", color="white", fontsize=12, fontweight="bold")
ax.set_ylim(0, max(losses2) * 1.35)
fig.text(0.5, 0.01,
         "Combined: $2.04B. Combined contract-level code bugs: 0.",
         ha="center", fontsize=10, style="italic", color="#555")
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(OUT / "02_14_month_arc.png", bbox_inches="tight")
plt.close()
print("02_14_month_arc.png")

# ---------- Chart 3: DeFi TVL April 14-25 ----------
days = list(range(14, 26))
# Approximate TVL trajectory anchored on reported peak/trough
tvl = [97.0, 98.2, 98.8, 99.5, 99.1, 95.4, 86.3, 87.0, 87.4, 87.8, 88.2, 88.6]
fig, ax = plt.subplots(figsize=(12, 5.625))
ax.plot(days, tvl, color="#c0392b", linewidth=2.5, marker="o")
ax.fill_between(days, tvl, min(tvl) - 1, alpha=0.08, color="#c0392b")
ax.axvline(18, color="#333", linestyle="--", linewidth=1)
ax.text(18.1, max(tvl) - 1, "KelpDAO exploit\nApril 18", fontsize=10, color="#333")
ax.set_xlabel("Day of April 2026")
ax.set_ylabel("Total DeFi TVL (billions USD)")
ax.set_title("$292M of theft, $13.21B of capital flight")
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${int(x)}B"))
ax.set_ylim(85, 101)
fig.text(0.5, 0.01,
         "Peak $99.5B (Apr 17) to bottom $86.3B (Apr 20). Steepest 2-day drop since LUNA-UST collapse, May 2022.",
         ha="center", fontsize=10, style="italic", color="#555")
plt.tight_layout(rect=[0, 0.04, 1, 1])
plt.savefig(OUT / "03_tvl_exodus.png", bbox_inches="tight")
plt.close()
print("03_tvl_exodus.png")

print("\nAll charts generated in", OUT)
