import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------
# LOAD FILE
# ---------------------------------
# file_name = "encoder_imu_rectangle.csv"
file_name = "encoder_only_rectangle.csv"

df = pd.read_csv(file_name)

for col in ["time", "imu_x", "x", "y"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["time", "imu_x", "x", "y"])

# ---------------------------------
# ORIGINAL DATA
# ---------------------------------
x = df["x"].values
y = df["y"].values

# ---------------------------------
# REMOVE START TILT
# Align first heading to 0 deg
# ---------------------------------
theta0 = np.radians(df["imu_x"].iloc[0])

x_rot = x * np.cos(theta0) + y * np.sin(theta0)
y_rot = -x * np.sin(theta0) + y * np.cos(theta0)

# ---------------------------------
# OPTIONAL FLIPS
# ---------------------------------

# Flip vertically (most common)
y_rot = -y_rot

# If instead you want horizontal flip, use:
# x_rot = -x_rot

# If you want 180 deg rotate:
# x_rot = -x_rot
# y_rot = -y_rot

# ---------------------------------
# PLOT PATH
# ---------------------------------
plt.figure(figsize=(7,7))
plt.plot(x_rot, y_rot, marker='o', linewidth=2)
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.title("Robot Path")
plt.grid(True)
plt.axis("equal")
plt.show()

# ---------------------------------
# HEADING VS TIME
# ---------------------------------
plt.figure(figsize=(10,5))
plt.plot(df["time"], df["imu_x"], linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("IMU Heading (deg)")
plt.title("IMU Heading vs Time")
plt.grid(True)
plt.show()