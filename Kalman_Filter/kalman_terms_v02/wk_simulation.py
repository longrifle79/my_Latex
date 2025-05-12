import numpy as np
import matplotlib.pyplot as plt

# Define simulation parameters
dt = 1  # Time step (seconds)
num_steps = 50  # Number of time steps

# Define the system model (State Transition Matrix A)
A = np.array([[1, dt],
              [0, 1]])

# Define the process noise covariance matrix Q_k
Q_k = np.array([[0.0125, 0.025], 
                [0.025, 0.05]])

# Define initial state (position and velocity)
x_true = np.array([[0],  # Initial position
                   [1]])  # Initial velocity (1 m/s)

# Initialize predicted state
x_pred = x_true.copy()

# Store results for plotting
true_positions = []
predicted_positions = []

# Run Kalman Filter simulation
for k in range(num_steps):
    # Generate process noise w_k (random sample from N(0, Q_k))
    w_k = np.random.multivariate_normal(mean=[0, 0], cov=Q_k).reshape(2, 1)
    print(w_k)
    # True state update (without noise)
    x_true = A @ x_true  # Assuming no control input for simplicity

    # Predicted state (with process noise)
    x_pred = A @ x_pred + w_k

    # Store results for plotting
    true_positions.append(x_true[0, 0])
    predicted_positions.append(x_pred[0, 0])

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(range(num_steps), true_positions, label="True Position (No Noise)", linestyle='--', color='blue')
plt.plot(range(num_steps), predicted_positions, label="Predicted Position (With Process Noise)", linestyle='-', color='red')
plt.xlabel("Time Step")
plt.ylabel("Position (m)")
plt.title("Effect of Process Noise \( w_k \) on Position Estimation")
plt.legend()
plt.grid()
plt.ion()  # Enable interactive mode
plt.show(block=True)
