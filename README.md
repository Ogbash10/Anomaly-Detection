# Anomaly Detection for Login Patterns

## Description
This project demonstrates anomaly detection using the **Isolation Forest** algorithm to detect abnormal login patterns from a given login dataset.

The dataset consists of login attempts, and the goal is to identify unusual patterns based on the time of login and other factors.

## Files
1. **`anomaly_detection.py`**: Python script that analyzes the login dataset and detects anomalies based on login hour patterns.
2. **`login_dataset.csv`**: Sample dataset of login attempts with timestamps and success flags.
3. **`anomaly_plot.png`**: Plot visualizing anomalies in login patterns.

## How to Run
1. Install the required Python libraries:
   ```bash
   pip install pandas scikit-learn matplotlib
   
2. Run the Python script:
   
 anomaly_detection.py

3.View the generated plot and printed anomalies.
