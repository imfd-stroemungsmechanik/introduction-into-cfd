import matplotlib.pyplot as plt
import numpy as np
import os

# change to directory of python script
os.chdir(os.path.dirname(__file__))


# Determine which file to use
solver_info_file = "postProcessing/solverInfo/0/solverInfo_0.dat"
if not os.path.exists(solver_info_file):
    solver_info_file = "postProcessing/solverInfo/0/solverInfo.dat"
    
    
# Read residuals
time, R_p, R_Ux, R_Uy, R_Uz, R_h, R_k, R_omega = np.genfromtxt(
    "postProcessing/residuals/0/residuals.dat",
    unpack=True,
    skip_header=2
    )

# Plot residuals
plt.plot(time, R_p, label="$p$")
plt.plot(time, R_Ux, label="$U_x$")
plt.plot(time, R_Uy, label="$U_y$")
plt.plot(time, R_Uz, label="$U_z$")
plt.plot(time, R_h, label="$h$")
plt.plot(time, R_k, label="$k$")
plt.plot(time, R_omega, label="$\\omega$")

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




# Read probe data
time, T1, T2, T3 = np.genfromtxt(
    "postProcessing/probes/0/T",
    unpack=True,
    skip_header=4
    )

# Plot probe data
plt.plot(time, T1, label="Probe 1")
plt.plot(time, T2, label="Probe 2")
plt.plot(time, T3, label="Probe 3")

# Grid lines
plt.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")

# Set title and axis
plt.title("Probe Temperature")
plt.xlabel("Time [s]")
plt.ylabel("Temperature [K]")
plt.legend()

# Save figure and clean
plt.savefig("fig_probe_temperature.png")
plt.clf()




    
# Read average outlet temperature
time, avg_T = np.genfromtxt(
    "postProcessing/avgT/0/surfaceFieldValue.dat",
    unpack=True,
    skip_header=5
    )

# Plot residuals
plt.plot(time, avg_T, label="Average temperatur")

# Grid lines
plt.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")

# Set title and axis
plt.title("Average Outlet Temperature")
plt.xlabel("Time [s]")
plt.ylabel("Temperature [K]")
plt.legend()

# Save figure and clean
plt.savefig("fig_average_outlet_temperature.png")
plt.clf()







    
# Read maximum domain temperature
time, max_T = np.genfromtxt(
    "postProcessing/maxT/0/volFieldValue.dat",
    unpack=True,
    skip_header=5
    )

# Plot residuals
plt.plot(time, max_T, label="Maximum temperatur")

# Grid lines
plt.grid(linewidth=0.5, color="lightgrey", linestyle="dashed")

# Set title and axis
plt.title("Maximum Temperature")
plt.xlabel("Time [s]")
plt.ylabel("Temperature [K]")
plt.legend()

# Save figure and clean
plt.savefig("fig_maximum_temperature.png")
plt.clf()


