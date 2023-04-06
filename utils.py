def get_normalized_time(data):
   first_time = data["time"].iloc[0]
   data["time"] = data["time"] - first_time
   return data
    