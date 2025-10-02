# CRISP-DM Steps for Linear Regression

## 1. Business Understanding

*   **Objective:** Develop an interactive web application using Streamlit that demonstrates linear regression. The application should allow users to generate synthetic data with adjustable parameters (`n`, `a`, `var`), visualize the data and the fitted regression line, and identify the top 5 outliers.
*   **Success Criteria:** The application successfully generates data, performs linear regression, visualizes results, identifies outliers, and provides an intuitive Streamlit interface for parameter adjustment.

## 2. Data Understanding

*   **Data Source:** Synthetic data generated within the application.
*   **Data Generation Process:**
    *   `n` (number of data points): User-selectable integer between 100 and 1000.
    *   `x` values: Will be generated as a sequence (e.g., `np.linspace(0, 10, n)`).
    *   `b` (intercept): Fixed to 5.0 (not user-selectable).
    *   `a` (coefficient): User-selectable float between -10 and 10.
    *   `noise`: Random values drawn from a normal distribution `N(0, var)`, where `var` (variance) is user-selectable between 0 and 1000. The standard deviation will be `sqrt(var)`.
    *   `y` values: Calculated as `y = a * x + b + noise`.
*   **Data Characteristics:**
    *   Two-dimensional data (x, y).
    *   `x` will be a continuous independent variable.
    *   `y` will be a continuous dependent variable.
    *   The relationship is linear with added Gaussian noise.

## 3. Data Preparation

*   **Data Generation Function:** Create a Python function that takes `n`, `a`, `b`, and `var` as input and returns `x` and `y` arrays.
*   **Feature Engineering:** In this simple linear regression case, `x` is already the feature. No complex feature engineering is required.
*   **Data Splitting:** For a simple demonstration, the model will be fitted on all generated data, so no explicit train/test split is needed.
*   **Reshaping:** The `x` data will need to be reshaped from `(n,)` to `(n, 1)` to be compatible with `scikit-learn`'s `LinearRegression` model.

## 4. Modeling

*   **Model Selection:** `LinearRegression` from `scikit-learn`.
*   **Training:** The model will be trained on the generated `x` and `y` data.
*   **Prediction:** The trained model will be used to predict `y` values (`y_pred`) for the given `x` values. These predictions will form the regression line.
*   **Outlier Identification:**
    *   Calculate residuals: `residuals = y - y_pred`.
    *   Identify the top 5 outliers by finding the data points with the largest absolute residuals.

## 5. Evaluation

*   **Regression Metrics:**
    *   **R-squared (R2 Score):** To measure how well the regression predictions approximate the real data points. A higher R2 score indicates a better fit.
    *   **Mean Squared Error (MSE):** To quantify the average squared difference between the estimated values and the actual value. Lower MSE indicates a better fit.
    *   **Visual Evaluation:** Plotting data points and fitted regression line; visual inspection of outliers.
*   **Model Parameters:** Display the calculated coefficient (`a_pred`) and intercept (`b_pred`) from the fitted model and compare them to the true `a` and `b` used for data generation.
*   **Outlier Identification:** Verify that the identified outliers are indeed the points furthest from the regression line.

## 6. Deployment

*   **Streamlit Application:** Create `app.py` to encapsulate all logic (data generation, preparation, modeling, evaluation) and implement Streamlit widgets for user input and display results.
*   **Dependencies:** List all required Python libraries in `requirements.txt`.
*   **Instructions:** Provide clear instructions on how to run the Streamlit application.
*   Display the top 5 outliers in a `st.dataframe`.
