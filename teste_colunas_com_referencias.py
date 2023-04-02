
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("csv/coleta12.csv")
column_names = [
    "uTheta", 
    "uOmega", 
    "uPosition", 
    "uVelocity", 
    "uAcceleration", 
    "Theta",
    "Omega",
    "Position", 
    "Velocity", 
    "Acceleration",
    "RefPosition",
    "RefVelocity"
 ]
data.columns = column_names

# # Read the first row of the DataFrame
# first_row = data.iloc[0]

# # Create a dictionary to store the first row values with the column names as keys
# K = {}
# for column_name in column_names[:5]:
#     K[column_name] = first_row[column_name]
# # Print all K from the controller
# print("Controller Gains are:", K)

data['AllSignals'] =  data['uTheta'] + data['uOmega'] + data['uPosition'] + data['uVelocity'] + data['uAcceleration']

new_colums = ["AllSignals"] + column_names

# Create a figure with 7 subplots
fig, axes = plt.subplots(nrows=6, ncols=1, figsize=(10, 24))

# Iterate through each column and create a line plot
for index, column_name in enumerate(new_colums):
    if column_name not in [
        "Theta",
        "Omega",
        "Acceleration",
        "Position", 
        "RefPosition", 
        "Velocity", 
        "RefVelocity"
    ]:
        axes[index].plot(data[column_name], label=column_name)
        axes[index].set_ylabel(column_name)
        axes[index].legend()
        axes[index].grid(True)

# Create a figure for the Position and RefPosition plot
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Plot "Position" and "RefPosition"
ax2.plot(data['Position'], label='Position')
ax2.plot(data['RefPosition'], label='RefPosition')
ax2.set_ylabel('Position / RefPosition')
ax2.legend()
ax2.grid(True)

fig3, ax3 = plt.subplots(figsize=(10, 6))

# Plot "Velocity" and "RefVelocity"
ax3.plot(data['Velocity'], label='Velocity')
ax3.plot(data['RefVelocity'], label='RefVelocity')
ax3.set_ylabel('Velocity / RefVelocity')
ax3.legend()
ax3.grid(True)

# Add some space between the subplots
fig.tight_layout(pad=3.0)

# Display the plot
plt.show()