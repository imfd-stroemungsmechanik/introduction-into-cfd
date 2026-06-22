import matplotlib.pyplot as plt
import numpy as np
import os

# change to directory of python script
os.chdir(os.path.dirname(__file__))


# Read residuals
iteration, R_p, R_Ux, R_Uy, R_epsilon, R_k = np.genfromtxt(
    "postProcessing/residuals/0/residuals.dat",
    unpack=True,
    skip_header=3)

# Plot residuals
plt.plot(iteration, R_p, label="$p$")
plt.plot(iteration, R_Ux, label="$U_x$")
plt.plot(iteration, R_Uy, label="$U_y$")
plt.plot(iteration, R_k, label="$k$")
plt.plot(iteration, R_epsilon, label="$\\epsilon$")

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

