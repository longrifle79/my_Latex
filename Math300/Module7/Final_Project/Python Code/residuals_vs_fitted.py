import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Simulate the data (as per your LaTeX code)
np.random.seed(42)
n = 200
pt = [0]
vt = [1]
for t in range(n-1):
    pt.append(pt[-1] + vt[-1] + np.random.normal(0, 0.1))
    vt.append(vt[-1] + np.random.normal(0, 0.05))
s = np.random.binomial(1, 0.5, n)

# Compute pt_next directly from pt
pt_next = pt[1:]  # p_{t+1} is the next position in the pt list

# Prepare data for regression
pt_current = pt[:-1]  # p_t (excluding the last one)
vt_current = vt[:-1]  # v_t (excluding the last one)
s_current = s[:-1]    # S (excluding the last one)

# Fit the first-order main effects model: p_{t+1} = beta_0 + beta_1 p_t + beta_2 v_t + beta_3 S
X = sm.add_constant(np.column_stack((pt_current, vt_current, s_current)))
model = sm.OLS(pt_next, X).fit()

# Get fitted values and residuals
fitted_values = model.fittedvalues
residuals = model.resid

# Create scatter plot: Residuals vs Fitted
plt.figure(figsize=(6, 4))
plt.scatter(fitted_values, residuals, alpha=0.6, color='purple')
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.xlabel('Fitted Values ($\\hat{p}_{t+1}$, meters)')
plt.ylabel('Residuals ($p_{t+1} - \\hat{p}_{t+1}$, meters)')
plt.title('Residuals vs Fitted Values')
plt.grid(True)
plt.savefig('residuals_vs_fitted.png')
plt.close()

print("Residuals vs Fitted plot generated: 'residuals_vs_fitted.png'")