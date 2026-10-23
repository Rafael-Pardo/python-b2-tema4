def mean(data: list, key: str) -> float:
    total = sum(float(row[key]) for row in data)
    return total / len(data)


def median(data: list, key: str) -> float:
    sorted_data = sorted(float(row[key]) for row in data)
    n = len(sorted_data)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_data[midpoint]
    else:
        return (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2
