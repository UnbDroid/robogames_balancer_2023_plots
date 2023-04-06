import pandas as pd
import matplotlib.pyplot as plt
import sys
import plotting_functions
import usecase_15_cols
import usecase_13_cols
import usecase_12_cols
import controller_columns
import state_columns
import utils

get_all_signals = False

file_path = sys.argv[1]

data = pd.read_csv(file_path, header=None)

column_names = usecase_15_cols.column_names
controller_column_names = controller_columns.columns

title, data = plotting_functions.init_fetch_first_line_of_file(
    data, 
    controller_column_names,
    len(column_names)
)

data.columns = column_names
if("time" in column_names):
    data = utils.get_normalized_time(data)


# data = data.iloc[60000:100000]

printable_columns = controller_column_names

if(get_all_signals):
    printable_columns, data = controller_columns.get_all_signals(data, printable_columns)

plotting_functions.plot_multiple(
    printable_columns, 
    title, 
    data, 
    printable_columns=printable_columns,
    columns_that_have_refs=state_columns.has_ref_columns,
    plot_over_time=True,
)
plotting_functions.plot_separate_graph_with_ref(
    data=data,
    column_name='Position', 
    ref_column_name='RefPosition', 
    title=title,
    plot_over_time=True
) 

plotting_functions.plot_separate_graph_with_ref(
    data=data,
    column_name='Position', 
    ref_column_name='RefPosition', 
    title=title,
    plot_over_time=False
) 

plotting_functions.plot_separate_graph_with_ref(
    data=data,
    column_name='Velocity', 
    ref_column_name='RefVelocity', 
    title=title,
    plot_over_time=True
) 

printable_columns = state_columns.columns

plotting_functions.plot_multiple(
    printable_columns, 
    title, 
    data, 
    printable_columns=printable_columns,
    columns_that_have_refs=state_columns.has_ref_columns,
    plot_over_time=True
)

# Display the plot
plt.show()