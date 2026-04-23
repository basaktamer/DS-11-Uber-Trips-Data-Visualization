# 🚖 Uber NYC Pulse: Urban Demand Analysis

## **Project Overview**
This project analyzes **1,028,136 rows** of raw Uber pickup data from New York City (September 2014). By applying temporal feature engineering and interactive visualization techniques, the study identifies critical patterns in urban mobility and dispatch base performance.

## **🧠 Strategic Framework**
* **Core Algorithm: Temporal Feature Engineering.** Raw timestamps were transformed into descriptive periods—**The Lull, Morning Rush, Evening Surge, and Nightlife**—to provide human-readable context to the 24-hour cycle.
* **Key Metric: Hourly Trip Density (HTD).** A measure of market pressure used to identify supply-demand gaps across different dispatch bases.
* **Business Insight:** The **Evening Surge (16:00-19:00)** was identified as the primary revenue driver, suggesting that Uber serves as a vital "after-work" infrastructure in NYC.

## **📊 Key Features**
* **Dynamic Racing Bar Chart:** A cumulative visualization showing the hourly competition and growth of the various Uber dispatch bases throughout the month.
* **Interactive Streamlit Dashboard:** A responsive web interface allowing users to filter data by base and visualize trip distribution dynamically.
* **Automated Time Labeling:** Custom Python logic used to categorize data into urban activity phases, making technical data accessible for business decision-making.

## **🛠️ Tech Stack & Configuration**
* **Language:** Python 3.9+ (Miniconda Environment)
* **Frameworks:** `Streamlit`, `Pandas`, `Plotly`, `Bar_chart_race`
* **System Requirements:** **FFmpeg** engine (configured via `packages.txt`) for video rendering.
* **Deployment:** Hugging Face Spaces.

---
*Developed by **Basak** as a Capstone project during a 400-hour technical bootcamp, marking a career transition from Business Administration to Data Science.*