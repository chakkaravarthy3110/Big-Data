import os
from builtins import len, print

from VegetableMapper import mapper
from VegetablePartitioner import partition
from VegetableSorter import sorter
from VegetableReducer import reducer

current_folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_folder, "vegtable..txt")
if not os.path.exists(input_file):
    fallback = os.path.join(current_folder, "vegetable.txt")
    if os.path.exists(fallback):
        input_file = fallback

def splitter(mapped_data):
    mid = len(mapped_data) // 2
    return mapped_data[:mid], mapped_data[mid:]

def main():
    mapped = mapper(input_file)
    print("MAP OUTPUT")
    print(mapped)

    split1, split2 = splitter(mapped)
    print("\nSPLITTER OUTPUT")
    print("Split 1:", split1)
    print("Split 2:", split2)

    part1 = partition(split1)
    part2 = partition(split2)

    merged = {}
    for part in (part1, part2):
        for key, value in part.items():
            merged.setdefault(key, []).extend(value)

    print("\nPARTITION OUTPUT")
    print(merged)

    sorted_data = sorter(merged)
    print("\nSORT OUTPUT")
    print(sorted_data)

    result = reducer(sorted_data)
    print("\nREDUCE OUTPUT")
    for category, count in result.items():
        print(category, ":", count)

if __name__ == "__main__":
    main()
