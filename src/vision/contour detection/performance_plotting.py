import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.loadtxt("hw3_recording_data.txt")

# Convert to milliseconds
data_ms = data * 1000

# Frame index (0 → 149 if 150 frames)
frames = np.arange(len(data_ms))


# -----------------------------
# Plot 1: Frame vs Processing Time
# -----------------------------
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(frames, data_ms, 'b-o', markersize=4, linewidth=1, label="Raw Data")

plt.title("Object Tracking: Processing Time")
plt.xlabel("Frame")
plt.ylabel("Processing Time [msec]")
plt.xlim(0, len(data_ms)-1)
plt.grid(True)
plt.legend()

# -----------------------------
# Plot 2: Histogram
# -----------------------------
plt.subplot(2, 1, 2)
plt.hist(data_ms, bins=50)

plt.title("Object Tracking: Processing Time")
plt.xlabel("Processing Time [msec]")
plt.ylabel("Number of Frames")
plt.grid(True)

plt.show()