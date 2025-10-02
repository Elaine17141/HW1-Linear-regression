import streamlit as st
import numpy as np
import pandas as pd   # 如果後面有用到 DataFrame
import matplotlib.pyplot as plt  # 如果要畫圖
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score







# --- Data Generation (CRISP-DM: Data Preparation) ---
def generate_data(n_samples, true_a, true_b, variance):
    np.random.seed(42) # for reproducibility
    x = np.linspace(0, 10, n_samples)
    noise = np.random.normal(0, np.sqrt(variance), n_samples)
    y = true_a * x + true_b + noise
    return x, y

# --- Streamlit UI (CRISP-DM: Deployment) ---
st.title("HW1-1: Interactive Linear Regression Visualizer")

# Sidebar for user inputs
st.sidebar.header("Configuration")

n_samples = st.sidebar.slider("Number of data points (n)", 100, 1000, 200)
true_a = st.sidebar.slider("True coefficient (a)", -10.0, 10.0, 2.0)
true_b = 5.0 # Fixed intercept as per user request
variance = st.sidebar.slider("Noise Variance (var)", 0.0, 1000.0, 100.0)

# st.write(f"### Generated Data: y = {true_a:.2f}x + {true_b:.2f} + N(0, {variance:.2f}) noise")

# Generate data
x, y = generate_data(n_samples, true_a, true_b, variance)

# Reshape x for scikit-learn
X = x.reshape(-1, 1)

# --- Modeling (CRISP-DM: Modeling) ---
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Get model parameters
predicted_a = model.coef_[0]
predicted_b = model.intercept_

# --- Outlier Identification (CRISP-DM: Modeling) ---
residuals = np.abs(y - y_pred)
outlier_indices = np.argsort(residuals)[-5:] # Top 5 largest residuals
outlier_x = x[outlier_indices]
outlier_y = y[outlier_indices]
outlier_residuals = residuals[outlier_indices]

# Create a DataFrame for outliers
outliers_df = pd.DataFrame({
    'x': outlier_x,
    'y': outlier_y,
    'residuals': outlier_residuals
}, index=np.arange(1, len(outlier_x) + 1))

# --- Evaluation (CRISP-DM: Evaluation) ---
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)

st.subheader("Model Evaluation")
st.write(f"**R-squared (R2 Score):** {r2:.4f}")
st.write(f"**Mean Squared Error (MSE):** {mse:.4f}")
st.write(f"**Predicted Coefficient (a):** {predicted_a:.4f}")
st.write(f"**Predicted Intercept (b):** {predicted_b:.4f}")

# --- Visualization (CRISP-DM: Evaluation & Deployment) ---
fig, ax = plt.subplots(figsize=(10, 6))

# Plot generated data points
ax.scatter(x, y, label="Generated Data", alpha=0.6)

# Plot regression line
ax.plot(x, y_pred, color='red', label="Regression Line")

# Plot outliers
ax.scatter(outlier_x, outlier_y, color='purple', s=100, marker='o', edgecolor='black', label="Top 5 Outliers")
for i, idx in enumerate(outlier_indices):
    ax.annotate(f'Outlier {i+1}', (x[idx], y[idx]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='purple')


ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Linear Regression with Synthetic Data")
ax.legend()
st.pyplot(fig)

st.subheader("Top 5 Outliers")
st.dataframe(outliers_df[['x', 'y', 'residuals']])

