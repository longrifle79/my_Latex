import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.graphics.gofplots as smg
import scipy.stats as stats  # Add this import for stats.norm
import os

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

# Get fitted values and residuals for residuals vs fitted plot
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
print("Saving residuals vs fitted plot to:", os.path.abspath('residuals_vs_fitted.png'))
plt.savefig('residuals_vs_fitted.png')
plt.close()

# Create Q-Q plot
plt.figure(figsize=(6, 4))
smg.qqplot(residuals, line='45', fit=True, dist=stats.norm, marker='o', color='purple', alpha=0.6)
plt.title('Q-Q Plot of Residuals')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles (Residuals)')
plt.grid(True)
print("Saving Q-Q plot to:", os.path.abspath('qq_plot_residuals.png'))
plt.savefig('qq_plot_residuals.png')
plt.close()

# Create scatter plot: p_{t+1} vs p_t, colored by sensor type
plt.figure(figsize=(6, 4))
for sensor in [0, 1]:
    mask = (s_current == sensor)
    plt.scatter(np.array(pt_current)[mask], np.array(pt_next)[mask], 
                label='GPS' if sensor == 0 else 'Lidar',
                alpha=0.6)
plt.xlabel('$p_t$ (meters)')
plt.ylabel('$p_{t+1}$ (meters)')
plt.title('$p_{t+1}$ vs $p_t$ by Sensor Type')
plt.legend()
plt.grid(True)
print("Saving scatter plot (p_t+1 vs p_t) to:", os.path.abspath('scatter_p_t_vs_p_t_plus_1.png'))
plt.savefig('scatter_p_t_vs_p_t_plus_1.png')
plt.close()

# Create scatter plot: p_{t+1} vs v_t, colored by sensor type
plt.figure(figsize=(6, 4))
for sensor in [0, 1]:
    mask = (s_current == sensor)
    plt.scatter(np.array(vt_current)[mask], np.array(pt_next)[mask], 
                label='GPS' if sensor == 0 else 'Lidar',
                alpha=0.6)
plt.xlabel('$v_t$ (meters/second)')
plt.ylabel('$p_{t+1}$ (meters)')
plt.title('$p_{t+1}$ vs $v_t$ by Sensor Type')
plt.legend()
plt.grid(True)
print("Saving scatter plot (p_t+1 vs v_t) to:", os.path.abspath('scatter_v_t_vs_p_t_plus_1.png'))
plt.savefig('scatter_v_t_vs_p_t_plus_1.png')
plt.close()

print("All plots generated successfully.")