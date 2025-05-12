import numpy as np
import matplotlib.pyplot as plt

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
pt_next = pt[1:]  # p_{t+1} is simply the next position in the pt list

# Prepare data for scatter plots
pt_current = pt[:-1]  # p_t (excluding the last one)
vt_current = vt[:-1]  # v_t (excluding the last one)
s_current = s[:-1]    # S (excluding the last one)

# Verify lengths match
print(f"Length of pt_current: {len(pt_current)}")
print(f"Length of vt_current: {len(vt_current)}")
print(f"Length of s_current: {len(s_current)}")
print(f"Length of pt_next: {len(pt_next)}")

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
plt.savefig('scatter_v_t_vs_p_t_plus_1.png')
plt.close()

print("Scatter plots generated: 'scatter_p_t_vs_p_t_plus_1.png' and 'scatter_v_t_vs_p_t_plus_1.png'")