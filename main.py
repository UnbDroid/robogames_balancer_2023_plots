import pandas as pd
import matplotlib.pyplot as plt
import sys

file_path = sys.argv[1]

data = pd.read_csv(file_path, header=None)

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

# Read the first row of the DataFrame
first_row = data.iloc[0]

# Create a dictionary to store the first row values with the column names as keys
K = {}
for column_name in column_names[:5]:
    K[column_name] = first_row[column_name]
# Print all K from the controller
print("Controller Gains are:", K)
controller_gains_string = f"Controller Gains: {K}"

# Drop the first row from the DataFrame
data = data.drop(0)

# data = data.iloc[60000:100000]

# Reset the index after dropping the first row
data.reset_index(drop=True, inplace=True)

data['AllSignals'] = data['uTheta'] + data['uOmega'] + data['uPosition'] + data['uVelocity'] + data['uAcceleration']

new_colums = ["AllSignals"] + column_names

# Create a figure with 7 subplots
fig, axes = plt.subplots(nrows=6, ncols=1, figsize=(10, 24))

fig.suptitle(controller_gains_string, fontsize=16)

printable_columns = [
    "uTheta", 
    "uOmega", 
    "uPosition", 
    "Position",
    "uVelocity", 
    "uAcceleration"
]

# Iterate through each column and create a line plot
for index, column_name in enumerate(printable_columns):
    if column_name not in [
        "Theta",
        "Omega",
        "Acceleration",
        "RefPosition", 
        "Velocity", 
        "RefVelocity"
    ]:
        axes[index].plot(data[column_name], label=column_name)
        axes[index].set_ylabel(column_name)
        axes[index].legend()
        axes[index].grid(True)

def print_separate_graph_with_ref(column_name, ref_column_name):
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    fig2.suptitle(controller_gains_string, fontsize=16)

    ax2.plot(data[column_name], label=column_name)
    ax2.plot(data[ref_column_name], label=ref_column_name)
    ax2.set_ylabel(f'{column_name} / {ref_column_name}')
    ax2.legend()
    ax2.grid(True)
   

print_separate_graph_with_ref('Position', 'RefPosition') 
print_separate_graph_with_ref('Velocity', 'RefVelocity') 

# Add some space between the subplots
fig.tight_layout(pad=3.0)

# Display the plot
plt.show()