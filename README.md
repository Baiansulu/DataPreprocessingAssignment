# World Happiness Data Preprocessing Project

This repository contains a complete data preprocessing and analysis project using the **World Happiness Report (2020–2024)** dataset. The goal is to explore and model the factors influencing happiness scores across countries.

---

## Files Included
- `world_happiness_analysis.ipynb` – Full notebook
- `world_happiness_analysis.py` – Python script
- `2020.csv` to `2024.csv` – Happiness datasets
- `happiness_histogram.png` – Histogram visualization
- `report.pdf` – Summary of preprocessing and results

## Data Preprocessing Steps
- **Data Cleaning**: Removed duplicates and missing values
- **Data Integration**: Combined 5 years into one dataset
- **Data Reduction**: Selected important columns
- **Data Transformation**: Normalized numeric features
- **Data Discretization**: Categorized Happiness Score into 3 levels

## Bonus Analysis
- Built a Linear Regression model to predict Happiness Score
- Evaluated with R² Score and MSE
- Visualized score distribution

---

## Clustering Analysis
For this analysis, **K-Means clustering** was chosen as the primary model to group countries based on their happiness scores and related features such as GDP, social support, and life expectancy. Clustering was the most suitable approach as it allowed for the identification of natural groupings within the data without the need for predefined labels. By using K-Means, we could segment the countries into distinct clusters, providing insights into patterns and similarities between countries with similar happiness scores. This method helped uncover meaningful relationships and allowed for a more visual understanding of how various features contribute to global happiness.

---

## Project Summary

We analyzed how factors like **GDP**, **health**, **freedom**, and **corruption** impact the happiness of people in various countries. Key insights include:
- Strongest predictors: GDP per Capita, Social Support
- PCA helped reduce dimensionality and simplify analysis
- Regression performance: R² and MSE included in report
- Visualization included: Histograms, correlation heatmaps, and K-Means clustering results

---

## Author

Baiansuluu Bolotbekova 

---

## Purpose

This project was created for a data preprocessing assignment in psychology/statistics-related coursework. It demonstrates understanding of key preprocessing techniques and data analysis principles.
