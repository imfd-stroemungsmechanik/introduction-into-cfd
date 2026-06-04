import matplotlib.pyplot as plt
import numpy as np

# Read residuals
iteration, R_p, R_Ux, R_Uy = np.genfromtxt(
    "postProcessing/residuals/0/residuals.dat",
    unpack=True,
    skip_header=3)

# Plot residuals
plt.plot(iteration, R_p, label="$p$")
plt.plot(iteration, R_Ux, label="$U_x$")
plt.plot(iteration, R_Uy, label="$U_y$")

# Grid lines
plt.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")

# Set title and axis
plt.title("Residuals")
plt.xlabel("Iterations [-]")
plt.ylabel("Residuals [-]")
plt.legend()

# Logarithmic scale
plt.yscale("log")

# Save figure and clean
plt.savefig("fig_residuals.png")
plt.clf()



# Read force coefficients
iteration, Cm, Cd, Cl, Clf, Clr = np.genfromtxt(
    "postProcessing/forceCoeffs/0/forceCoeffs.dat",
    unpack=True,
    skip_header=4)

# Plot coefficients
plt.plot(iteration, Cd, label="Drag coefficient")
plt.plot(iteration, Cl, label="Lift coefficient")

# Set grid
plt.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")

# Set title and axis
plt.title("Drag and Lift Coefficients")
plt.xlabel("Iterations [-]")
plt.ylabel("Force Coefficients [-]")
plt.legend()

# Save figure
plt.savefig("fig_force_coefficients.png")
plt.clf()



# Read experimental data
alpha, Cl_exp, Cd_exp = np.genfromtxt(
    "experimental_data/lift_drag_coefficient.csv",
    unpack=True,
    delimiter=",")

# Create two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Lift coefficient plot
ax1.scatter(alpha, Cl_exp, label="Experiment", color="black", marker="s")
ax1.scatter(0, Cl[-1], label="Simulation", color="red")
ax1.set_title("Lift Coefficient")
ax1.set_xlabel("Angle of Attack [deg]")
ax1.set_ylabel("Lift Coefficient $C_L$ [-]")
ax1.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")
ax1.legend()

# Drag coefficient plot
ax2.scatter(alpha, Cd_exp, label="Experiment", color="black", marker="s")
ax2.scatter(0, Cd[-1], label="Simulation", color="red")
ax2.set_title("Drag Coefficient")
ax2.set_xlabel("Angle of Attack [deg]")
ax2.set_ylabel("Drag Coefficient $C_D$ [-]")
ax2.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")
ax2.legend()

# Save figure
plt.savefig("fig_force_coefficients_validation.png")

