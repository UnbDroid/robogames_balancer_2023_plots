import pandas as pd
import matplotlib.pyplot as plt
import sys
import plotting_functions
import usecase_15_cols
import usecase_13_cols
import usecase_12_cols

file_path = sys.argv[1]

data = pd.read_csv(file_path, header=None)

column_names = usecase_15_cols.column_names
controller_column_names = [
    "uTheta", 
    "uOmega", 
    "uPosition", 
    "uVelocity",
    "uIPosition",
    "uAcceleration", 
]

title, data = plotting_functions.init_fetch_first_line_of_file(
    data, 
    controller_column_names,
    len(column_names)
)

data.columns = column_names
# data = data.iloc[60000:100000]

data['AllSignals'] = data['uTheta'] + data['uOmega'] + data['uPosition'] + data['uVelocity'] + data['uAcceleration']

new_colums = ["AllSignals"] + column_names

printable_columns = [
    "uTheta", 
    "uOmega", 
    "uPosition", 
    "Position",
    "uVelocity", 
    "uAcceleration",
    "VoltaDir",
    "VoltaEsq",
]

plotting_functions.plot_multiple(
    printable_columns, 
    title, 
    data, 
    printable_columns=printable_columns
)
plotting_functions.plot_separate_graph_with_ref(
    data=data,
    column_name='Position', 
    ref_column_name='RefPosition', 
    title=title 
) 
plotting_functions.plot_separate_graph_with_ref(
    data=data,
    column_name='Velocity', 
    ref_column_name='RefVelocity', 
    title=title
) 

printable_columns = [
    "Theta", 
    "Omega", 
    "Position", 
    "Velocity", 
    "Acceleration",
    "time", 
    "VoltaDir",
    "VoltaEsq",
]

plotting_functions.plot_multiple(
    printable_columns, 
    title, 
    data, 
    printable_columns=printable_columns
)

# Display the plot
plt.show()