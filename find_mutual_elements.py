# 1. Write a function”find_mutual_elements” to find the mutual content
# in a 2 dimensional array. The mutual contents should be non repeating.
# Example
# array = [
# [0, 4, 4, 2, 3,1],
# [1, 4, 8, 7, 3],
# [3, 3, 3, 7, 1],
# ]

# find_mutual_elements(array)
# >>>
# [1, 3]


def find_mutual_elements(array):
    mutuals = set()
    for i, row in enumerate(array):
        if i == 0:
            mutual = set(row).intersection(array[i + 1])
            mutuals = mutual
        if i > 1:
            mutual = set(row).intersection(mutuals)
            mutuals = mutual
    return list(mutuals)


if __name__ == "__main__":
    array = [
        [0, 4, 4, 2, 3, 1],
        [1, 4, 8, 7, 3],
        [3, 3, 3, 7, 1],
    ]
    mutuals = find_mutual_elements(array)
    print(f"Mutuals: {mutuals}")
