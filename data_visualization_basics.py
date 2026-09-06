"""
Data Visualization Basics
==========================
Practice project: build the same charts in both Matplotlib and Seaborn
using the Tips dataset (built into Seaborn).

Modules
-------
1. Histogram              - distribution of total_bill
2. Bar Chart               - average total_bill by day
3. Box Plot                 - spread of total_bill by day
4. Scatter Plot              - total_bill vs tip
5. Correlation Heatmap        - correlation between numeric columns
                                 (also saved to disk as a PNG)

Run this file directly, or copy each module function into its own
Jupyter Notebook cell to work through them interactively.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ---------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------
def load_data():
    """Task: Load the Tips dataset that ships with Seaborn."""
    tips = sns.load_dataset("tips")
    print(f"Loaded Tips dataset: {tips.shape[0]} rows, {tips.shape[1]} columns")
    print(tips.head(), "\n")
    return tips


# ---------------------------------------------------------------
# Module 1: Histogram
# ---------------------------------------------------------------
def module_1_histogram(tips):
    """
    Task: Visualize how total_bill values are distributed across all
    recorded visits.
    Specific Parameters: column (total_bill), bins (20), fill color,
    edge color, axis labels, chart title.
    Techniques Used: plt.hist() in Matplotlib, sns.histplot() in Seaborn.
    """
    # Matplotlib
    plt.figure()
    plt.hist(tips["total_bill"], bins=20, color="steelblue", edgecolor="white")
    plt.title("Total Bill Distribution (Matplotlib)")
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Seaborn
    plt.figure()
    sns.histplot(data=tips, x="total_bill", bins=20, color="teal")
    plt.title("Total Bill Distribution (Seaborn)")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------
# Module 2: Bar Chart
# ---------------------------------------------------------------
def module_2_bar_chart(tips):
    """
    Task: Compare the average total_bill across each day of the week.
    Specific Parameters: grouping column (day), aggregated value
    (mean total_bill), bar color/palette, axis labels, chart title.
    Techniques Used: pandas groupby(), plt.bar() in Matplotlib,
    sns.barplot() in Seaborn.
    """
    avg_bill = tips.groupby("day", observed=True)["total_bill"].mean()

    # Matplotlib
    plt.figure()
    plt.bar(avg_bill.index, avg_bill.values, color="coral")
    plt.title("Average Bill by Day (Matplotlib)")
    plt.xlabel("Day")
    plt.ylabel("Average Total Bill ($)")
    plt.tight_layout()
    plt.show()

    # Seaborn
    plt.figure()
    sns.barplot(data=tips, x="day", y="total_bill", hue="day",
                palette="pastel", legend=False)
    plt.title("Average Bill by Day (Seaborn)")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------
# Module 3: Box Plot
# ---------------------------------------------------------------
def module_3_box_plot(tips):
    """
    Task: Compare the spread and outliers of total_bill values across
    each day.
    Specific Parameters: grouping column (day), value column
    (total_bill), color palette, axis labels, chart title.
    Techniques Used: DataFrame.boxplot() in Matplotlib, sns.boxplot()
    in Seaborn.
    """
    # Matplotlib
    plt.figure()
    tips.boxplot(column="total_bill", by="day")
    plt.title("Total Bill by Day (Matplotlib)")
    plt.suptitle("")
    plt.xlabel("Day")
    plt.ylabel("Total Bill ($)")
    plt.tight_layout()
    plt.show()

    # Seaborn
    plt.figure()
    sns.boxplot(data=tips, x="day", y="total_bill", hue="day",
                palette="Set2", legend=False)
    plt.title("Total Bill by Day (Seaborn)")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------
# Module 4: Scatter Plot
# ---------------------------------------------------------------
def module_4_scatter_plot(tips):
    """
    Task: Examine the relationship between total_bill and tip amount.
    Specific Parameters: x (total_bill), y (tip), color grouping (sex),
    point transparency, axis labels.
    Techniques Used: plt.scatter() in Matplotlib, sns.scatterplot() in
    Seaborn, optional hue encoding.
    """
    # Matplotlib
    plt.figure()
    plt.scatter(tips["total_bill"], tips["tip"], c="purple", alpha=0.6)
    plt.title("Tip vs Total Bill (Matplotlib)")
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Tip ($)")
    plt.tight_layout()
    plt.show()

    # Seaborn
    plt.figure()
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
    plt.title("Tip vs Total Bill (Seaborn)")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------
# Module 5: Correlation Heatmap
# ---------------------------------------------------------------
def module_5_heatmap(tips, output_path="correlation_heatmap.png"):
    """
    Task: Visualize how the numeric columns in the dataset correlate
    with each other.
    Specific Parameters: correlation matrix (numeric columns only),
    color map (coolwarm), cell annotations, axis tick labels.
    Techniques Used: DataFrame.corr(), plt.imshow() + colorbar in
    Matplotlib, sns.heatmap() in Seaborn, plt.savefig().
    """
    corr = tips.corr(numeric_only=True)

    # Matplotlib
    plt.figure()
    plt.imshow(corr, cmap="coolwarm")
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns, rotation=45)
    plt.yticks(range(len(corr)), corr.columns)
    plt.title("Correlation Heatmap (Matplotlib)")
    plt.tight_layout()
    plt.show()

    # Seaborn (also saved to disk as the project's required PNG output)
    plt.figure()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap (Seaborn)")
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Saved: {output_path}")
    plt.show()


# ---------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------
def main():
    sns.set_theme(style="whitegrid")  # shared styling baseline for every chart
    tips = load_data()

    module_1_histogram(tips)
    module_2_bar_chart(tips)
    module_3_box_plot(tips)
    module_4_scatter_plot(tips)
    module_5_heatmap(tips)


if __name__ == "__main__":
    main()
