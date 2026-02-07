# HR Employee Retention Analysis (Power BI)

## Project Overview

This project analyzes employee retention and attrition patterns using an HR dataset sourced from Kaggle. The primary objective is to understand how employee retention has changed over a recent six‑month period and to identify which employee segments (particularly departments) are most susceptible to turnover. The final deliverable is an interactive Power BI dashboard designed for exploratory analysis and executive-level reporting.

This project was intentionally scoped as a **descriptive analytics** exercise, emphasizing metric definition, data quality handling, and clear communication of insights rather than predictive modeling.

---

## Research Questions

* How have employee termination and attrition levels changed over the most recent six months of available data?
* Which departments exhibit higher concentrations or spikes in employee terminations?
* What is the overall six‑month attrition rate, and how does it compare across employee segments?

---

## Dataset Description

* **Source:** Kaggle (Human Resource Data Set (The Company))
* **Granularity:** One row per employee
* **Key fields:**

  * Start_Date
  * Termination_Date
  * Department
  * Active_Status

### Data Quality Considerations

* Active employees are represented using a **placeholder termination date (12/12/2999)**.
* The dataset appears to be a historical snapshot rather than a continuously updated feed.
* Based on observed status patterns, the analysis is anchored to a fixed **as‑of date of June 29, 2021** to ensure temporal consistency.

These issues required explicit assumptions and handling logic, which are documented below.

---

## Analytical Assumptions

* A snapshot date of the most recent start date is used in place of `TODAY()` to reflect the dataset’s last known update.
* Attrition rate is calculated using **employees active at the start of the analysis window** as the denominator to avoid inflation from mid‑period hires.

---

## Key Metrics

* **Active Employees (Start of Period):** Employees employed as of the beginning of the six‑month window
* **Terminations (Last 6 Months):** Employees whose termination dates fall within the analysis window
* **6‑Month Attrition Rate:**

  {Attrition Rate} = {Terminations in Last 6 Months} / {Active Employees at Period Start}

---

## Dashboard Features

The Power BI dashboard includes:

* **KPI Tile**

  * Overall 6‑month attrition rate
* **Department-Level Analysis**

  * Bar chart comparing termination counts by department
  * Pie chart depicting active headcount by department
* **Time-Series Visualization**

  * Line chart showing monthly termination trends over the last six months, segmented by department
* **Interactive Controls**

  * Job Level and Job Title slicers
  * Reset button (implemented using bookmarks) to clear filters and drill states

All visuals are explicitly constrained to the six‑month analysis window to ensure consistency across metrics.

---

## Tools & Technologies

* **Power BI**

  * Data modeling
  * DAX for metric creation and time‑window logic
  * Interactive dashboard design
* **GitHub**

  * Version control
  * Project documentation

Python and SQL were evaluated but not required for this phase, as the analysis centered on aggregation, filtering, and metric definition rather than statistical modeling or ETL complexity.

---

## Key Insights

* Overall six‑month attrition is approximately **3.9%**, indicating moderate turnover during the analysis period.
* Attrition is not evenly distributed across departments; certain departments show clear termination spikes.
* Termination activity is clustered in specific months, suggesting potential operational drivers.

*(Exact insights may vary depending on user interaction with the dashboard.)*

---

## Future Enhancements

* Predictive attrition modeling using Python (e.g., logistic regression or survival analysis)
* Statistical testing to evaluate drivers of turnover
* Automated data refresh and parameterized snapshot dates
* Integration with compensation or performance data for deeper analysis

---

## Author

**Tanner West**
BS in Data Analytics (in progress)

---

## Notes

This project emphasizes analytical judgment, metric defensibility, and clear communication—skills directly applicable to junior data analyst and business intelligence roles.
