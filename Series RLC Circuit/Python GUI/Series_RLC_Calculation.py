'''

Series RLC Circiut Analysis
By Nariman Ziaie
Student ID: 40010140119030

'''
import numpy as np
import matplotlib.pyplot as plt

# Define circuit parameters and input voltage
vb = 2  # Volts
r = 10  # Ohms
l = 10e-3  # Henries
c = 4.7e-9  # Farads
dt = 1e-6  # Second

# Initial conditions
i1_initial = 0
vc_initial = 0

# Define damping resistance
R_overdamped = 33e3 # Overdamped
R_critical = 3.3e3 # Critically damped
R_underdamped = 330 # Underdamped

# Define simulation function
def simulate_rlc(vb, r, l, c, dt, i1_initial, vc_initial, n_iterations):
    time1 = np.zeros(n_iterations + 1)
    i1 = np.zeros(n_iterations + 1)
    vl = np.zeros(n_iterations + 1)
    vc = np.zeros(n_iterations + 1)

    # Set initial values
    time1[0] = 0
    i1[0] = i1_initial
    vc[0] = vc_initial

    # Calculate values for each iteration
    for n in range(1, n_iterations + 1):
        time1[n] = time1[n-1] + dt
        l_dt = l / dt
        c_dt = c * dt
        i1[n] = ((i1[n-1] * (l_dt - r / 2 - dt / (2 * c))) + vb - vc[n-1]) / (l_dt + r / 2 + dt / (2 * c))
        vl[n] = ((i1[n] - i1[n-1]) / dt) * l
        vc[n] = vc[n-1] + (((i1[n] + i1[n-1]) / 2) * dt) / c

    return time1, i1, vl, vc

# Simulate the circuit
n_iterations = 500
time1, i1, vl, vc = simulate_rlc(vb, r, l, c, dt, i1_initial, vc_initial, n_iterations)

time1, i1, vl, V_overdamped = simulate_rlc(vb, R_overdamped, l, c, dt, i1_initial, vc_initial, n_iterations)
time1, i1, vl, V_critical = simulate_rlc(vb, R_critical, l, c, dt, i1_initial, vc_initial, n_iterations)
time1, i1, vl, V_underdamped = simulate_rlc(vb, R_underdamped, l, c, dt, i1_initial, vc_initial, n_iterations)

# Plot results
plt.figure(figsize=(12, 8))
plt.title("Voltage Response of Series RLC Circuit\nBy Nariman Ziaie\nStudent ID: 40010140119030")

# Overdamped
plt.plot(time1, V_overdamped, label="Overdamped", color="blue")

# Critically damped
plt.plot(time1, V_critical, label="Critically damped", color="green")

# Underdamped
plt.plot(time1, V_underdamped, label="Underdamped", color="red")

# Label the axes
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")

# Add a legend
plt.legend(loc="upper right")

# Increase the font size of the labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
