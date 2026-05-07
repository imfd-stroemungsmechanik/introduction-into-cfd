import matplotlib.pyplot as plt
import numpy as np

# Read residuals
time, R_p, R_Ux, R_Uy = np.genfromtxt(
    "postProcessing/residuals/0/residuals.dat",
    unpack=True,
    skip_header=3)

# Plot residuals
plt.plot(time, R_p, label="$p$")
plt.plot(time, R_Ux, label="$U_x$")
plt.plot(time, R_Uy, label="$U_y$")

# Grid lines
plt.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")

# Set title and axis
plt.title("Residuals")
plt.xlabel("Time [s]")
plt.ylabel("Residuals [-]")
plt.legend()

# Logarithmic scale
plt.yscale("log")

# Save figure and clean
plt.savefig("fig_residuals.png")
plt.clf()



# Read inlet pressure
time, velocity = np.genfromtxt(
    "postProcessing/Umax/0/volFieldValue.dat",
    unpack=True,
    skip_header=4)

# Plot velocity
plt.plot(time, velocity, label="Maximum velocity")

# Set grid
plt.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")

# Set title and axis
plt.title("Maximum Velocity in the Solution Domain")
plt.xlabel("Time [s]")
plt.ylabel("Maximum velocity [m/s]")
plt.legend()

# y-axis range
#plt.ylim(0, 200)

# Save figure
plt.savefig("fig_max_velocity.png")
