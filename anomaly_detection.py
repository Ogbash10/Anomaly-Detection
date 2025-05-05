import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate a dataset with failed login attempts
np.random.seed(0)
data = pd.DataFrame({
    'timestamp': pd.date_range(start='2025-01-01', periods=100, freq='H'),
    'login_attempts': np.random.normal(loc=5, scale=2, size=100),  # Normal login attempts
})

# Inject some anomalies
data.loc[30, 'login_attempts'] = 15  # Anomaly
data.loc[60, 'login_attempts'] = 25  # Anomaly

# Data preprocessing - scaling the login attempts
scaler = StandardScaler()
data['login_attempts_scaled'] = scaler.fit_transform(data[['login_attempts']])

# Apply Isolation Forest for anomaly detection
model = IsolationForest(contamination=0.1, random_state=42)
data['anomaly'] = model.fit_predict(data[['login_attempts_scaled']])

# Map anomaly labels
data['anomaly'] = data['anomaly'].map({1: 'Normal', -1: 'Anomaly'})

# Print the first few rows
print(data.head())

# Visualize the anomalies
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='timestamp', y='login_attempts', hue='anomaly', palette=['green', 'red'])
plt.title('Login Attempts with Anomalies')
plt.xlabel('Timestamp')
plt.ylabel('Login Attempts')
plt.xticks(rotation=45)
plt.legend(title='Anomaly', loc='upper left')
plt.show()
