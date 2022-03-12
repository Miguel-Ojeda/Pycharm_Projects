from typing import List
from math import exp

def dot_product(u: List[float], v: List[float]) -> float:
    return sum(uu * vv for uu, vv in zip(u, v))


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))


def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)

# assume all rows are of equal length
# and feature scale each column to be in the range 0 - 1
def normalize_by_feature_scaling(dataset: List[List[float]]) -> None:
    for col_num in range(len(dataset[0])):
        column: List[float] = [row[col_num] for row in dataset]
        maximum = max(column)
        minimum = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = (dataset[row_num][col_num] - minimum) / (maximum - minimum)


if __name__ == "__main__":
    u = [1, 2, 3, 4]
    v = [-4, 5, 3, 4]
    print (dot_product(u, v))
    print(sigmoid(-1))
    print(sigmoid(1.2))
    print(sigmoid(2))
