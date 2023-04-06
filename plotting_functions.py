import matplotlib.pyplot as plt

def init_fetch_first_line_of_file(
    data, 
    column_names,
    number_of_col_orig_file
):
    correction_size_file_columns = column_names + [""] * (number_of_col_orig_file - len(column_names))
    # Read the first row of the DataFrame
    first_row = data.iloc[[0]]
    first_row.columns = correction_size_file_columns
    controller_gains_string = f"Controller Gains: \n"
    for column_name in column_names:
        print(first_row[column_name][0])
        value = first_row[column_name][0]
        controller_gains_string += f"| {column_name}: {value}"

    # Print all K from the controller
    print(controller_gains_string)

    # Drop the first row from the DataFrame
    data = data.drop(0)

    # Reset the index after dropping the first row
    data.reset_index(drop=True, inplace=True)
    return (controller_gains_string, data)

def print_control_signals(
    columns_to_print,
    controller_gains_string,
    data, 
    printable_columns
):
    fig, axes = plt.subplots(nrows=len(columns_to_print), ncols=1, figsize=(10, 24))

    fig.suptitle(controller_gains_string, fontsize=16)

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
    # Add some space between the subplots
    fig.tight_layout(pad=3.0)
    

def print_separate_graph_with_ref(
    data,
    column_name, 
    ref_column_name, 
    title
):
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    fig2.suptitle(title, fontsize=16)

    ax2.plot(data[column_name], label=column_name)
    ax2.plot(data[ref_column_name], label=ref_column_name)
    ax2.set_ylabel(f'{column_name} / {ref_column_name}')
    ax2.legend()
    ax2.grid(True)