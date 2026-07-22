"""VegetableMapper.py
Maps vegetable categories from vegetable.txt
"""

def mapper(input_file):
    mapped_data = []
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                vegetable = [field.strip() for field in line.split(",")]

                if len(vegetable) >= 3:
                    category = vegetable[2]
                    mapped_data.append((category, 1))

    except FileNotFoundError:
        raise

    return mapped_data
