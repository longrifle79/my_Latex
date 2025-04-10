import numpy as np
import statsmodels.api as sm

np.random.seed(42)
n = 200
pt = [0]
vt = [1]
for t in range(n-1):
    pt.append(pt[-1] + vt[-1] + np.random.normal(0, 0.1))
    vt.append(vt[-1] + np.random.normal(0, 0.05))
s = np.random.binomial(1, 0.5, n)

# Fix pt_next to match the length of X
pt_next = pt[1:]  # Only take positions from t=1 to t=199 (length 199)

# X uses predictors from t=0 to t=198 (length 199)
X = sm.add_constant(np.column_stack((pt[:-1], vt[:-1], s[:-1])))

# Now pt_next and X both have 199 observations
model = sm.OLS(pt_next, X).fit()
print(model.summary())