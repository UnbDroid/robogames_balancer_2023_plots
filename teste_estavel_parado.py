import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("csv/vai_estavel.csv")
column_names = ["uTheta", "uOmega", "uPosition", "uVelocity", "uiPosition", "uAcceleration", "Position"]
data.columns = column_names

# Create a figure with 7 subplots
fig, axes = plt.subplots(nrows=7, ncols=1, figsize=(10, 20))

# Iterate through each column and create a line plot
for index, column_name in enumerate(column_names):
    axes[index].plot(data[column_name], label=column_name)
    axes[index].set_ylabel(column_name)
    axes[index].legend()
    axes[index].grid(True)

# Add some space between the subplots
fig.tight_layout(pad=3.0)

# Display the plot
plt.show()

def sameGraph():
    # Create a figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Iterate through each column and create a line plot
    for column_name in column_names:
        ax.plot(data[column_name], label=column_name)

    # Set labels and title
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    ax.set_title('All Columns')

    # Add a legend
    ax.legend()

    # Display the plot
    plt.show()