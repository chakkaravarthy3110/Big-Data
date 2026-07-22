# VegetableReducer.py
"""Reducer that sums counts for each vegetable category."""

def reducer(grouped_data):
    reduced_data = {}

    if hasattr(grouped_data, "items"):
        iterator = grouped_data.items()
    else:
        iterator = grouped_data

    for category, values in iterator:
        try:
            reduced_data[category] = sum(values)
        except TypeError:
            reduced_data[category] = sum(int(v) for v in values)

    return reduced_data
