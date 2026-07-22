"""VegetablePartitioner.py
Groups mapped vegetable categories.
"""

def partition(mapped_data):
    partitions = {}

    for category, value in mapped_data:
        if category not in partitions:
            partitions[category] = []
        partitions[category].append(value)

    return partitions
