import json


def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        data = json.load(f)

    product_sum = sum([item["score"] * item["weight"] for item in data])
    return round(product_sum, 3)


print(task())
