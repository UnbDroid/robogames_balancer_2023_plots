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
    controller_gains_string = f"Controller Gains: "
    for column_name in column_names:
        print(first_row[column_name][0])
        value = first_row[column_name][0]
        controller_gains_string += f"| {column_name}: {value}"

    # Drop the first row from the DataFrame
    data = data.drop(0)

    # Reset the index after dropping the first row
    data.reset_index(drop=True, inplace=True)
    return (controller_gains_string, data)

def plot_multiple(
    columns_to_print,
    controller_gains_string,
    data, 
    printable_columns,
    columns_that_have_refs,
    plot_over_time
):
    fig, axes = plt.subplots(nrows=len(columns_to_print), ncols=1, figsize=(10, 24))

    fig.suptitle(controller_gains_string, fontsize=16)

    # Iterate through each column and create a line plot
    for index, column_name in enumerate(printable_columns):
        axes[index] = plot_single_data(
            ax2=axes[index],
            data=data, 
            with_time=plot_over_time, 
            column_name=column_name
        )
        if(column_name in columns_that_have_refs):
            ref_column_name= f"Ref{column_name}"
            axes[index] = plot_single_data(
                ax2=axes[index],
                data=data, 
                with_time=plot_over_time, 
                column_name=ref_column_name
            )
        axes[index].set_ylabel(column_name)
        axes[index].legend()
        axes[index].grid(True)
    # Add some space between the subplots
    fig.tight_layout(pad=3.0)

def plot_single_data(ax2, data, with_time, column_name):
    if(with_time and column_name != "time"):
        ax2.plot(data["time"], data[column_name], label=column_name)
    else:    
        ax2.plot(data[column_name], label=column_name)
    return ax2

def plot_separate_graph_with_ref(
    data,
    column_name, 
    ref_column_name, 
    title,
    plot_over_time
):
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    fig2.suptitle(title, fontsize=16)

    ax2 = plot_single_data(
        ax2=ax2,
        data=data, 
        with_time=plot_over_time, 
        column_name=column_name
    )

    ax2 = plot_single_data(
        ax2=ax2,
        data=data, 
        with_time=plot_over_time, 
        column_name=ref_column_name
    )
    ax2.set_ylabel(f'{column_name} / {ref_column_name}')
    ax2.legend()
    ax2.grid(True)