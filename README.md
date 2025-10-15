# Redlands, CA Economic Modeling and Simulation

## 📊 Project Overview

This project is a data-driven simulation model developed in **Python** to forecast long-term economic trends for the city of Redlands, California. Using historical data and a multi-variable impact algorithm, the model generates projections for key economic indicators—most notably **median individual income**—extending through the year 2100.

The primary goal was to explore the interconnected dynamics of local economic health and provide realistic forecasts by accounting for complex variables like inflation and labor market fluctuations.

---

## ✨ Key Features & Technical Highlights

* **Python Simulation:** Developed a robust **Python simulation model** to forecast Redlands, CA, economic trends, with projections extending to **2100**.
* **Algorithmic Modeling:** Designed and implemented a custom **simulation algorithm** to project median income based on the weighted influence of **five key economic factors** (e.g., unemployment, poverty rates, labor force size).
* **Data Integration:** **Integrated and parsed historical economic data** using **Pandas** to establish baseline metrics and calculate long-term rates of change for all model inputs.
* **Inflation Adjustment:** Modeled the effect of inflation, applying a **2.5% annual rate** (based on St. Louis Fed historical data) to the projected median income for realistic economic forecasting.
* **Data Visualization:** Visualized **over eight distinct economic metrics** and multi-variable combo graphs using **Matplotlib** for comprehensive data interpretation.
* **Version Control:** Code base managed through this **GitHub Repository**, facilitating collaboration and version tracking.

---

## ⚙️ Methodology & Model Inputs

The core of the simulation is a novel impact-based algorithm that uses recent and long-term rates of change to extrapolate future values. The five primary economic indicators influencing the projected median individual income are:

1.  **Unemployment**
2.  **Employment**
3.  **Poverty Rates**
4.  **Labor Force Size**
5.  **Population Change**

The model then applies a **constant inflation factor** of 2.5% to the projected income values, resulting in two distinct output plots: one for nominal projected income and one for inflation-adjusted (real) projected income.

---

## 🛠️ Technical Stack

* **Language:** Python
* **Data Handling:** Pandas
* **Visualization:** Matplotlib
* **Numerical Operations:** NumPy
* **Project Management:** GitHub / Git

---

## ▶️ Usage

To run the simulation and generate the plots locally, you will need Python installed.

1.  Clone the repository:
    ```bash
    git clone [YOUR_REPO_URL]
    ```
2.  Navigate to the project directory:
    ```bash
    cd Redlands-Economic-Modeling
    ```
3.  Install the required dependencies:
    ```bash
    pip install pandas matplotlib numpy
    ```
4.  Run the main simulation script:
    ```bash
    python redlands_simulation.py
    ```
    *The script will execute and display the generated economic plots.*

---

## 📈 Future Work

This project laid the foundation for long-term economic modeling. Future iterations could include:

* **Variable Integration:** Modeling additional complex factors such as migration patterns, crime rates, and climate impact.
* **Model Refinement:** Analyzing past economic drops and increases to better calibrate the model's sensitivity coefficients for greater accuracy.
* **External Factor Analysis:** Incorporating the specific economic impact of the University of Redlands to create a more localized, granular forecast.

