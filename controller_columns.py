columns = [
    "uTheta", 
    "uOmega", 
    "uPosition", 
    "uVelocity",
    # "uIPosition",
    "uAcceleration", 
]

def get_all_signals(data, column_names):
    data['AllSignals'] = data['uTheta'] + data['uOmega'] + data['uPosition'] + data['uVelocity'] + data['uAcceleration']
    new_colums = ["AllSignals"] + column_names
    return (new_colums, data)
