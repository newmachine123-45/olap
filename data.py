from itertools import combinations
from collections import defaultdict

def find_frequent_2_itemsets(dataset, min_support):
    # Create a dictionary to count occurrences of 2-itemsets
    itemset_counts = defaultdict(int)

    # Count the occurrences of all possible 2-item combinations
    for transaction in dataset:
        # Generate all possible pairs in the transaction
        for itemset in combinations(sorted(transaction), 2):
            itemset_counts[itemset] += 1

    # Filter the 2-itemsets that meet the minimum support count
    frequent_2_itemsets = {itemset: count for itemset, count in itemset_counts.items() if count >= min_support}

    return frequent_2_itemsets

# Example dataset
dataset = [
    ['bread', 'milk'],
    ['bread', 'diaper', 'beer', 'egg'],
    ['milk', 'diaper', 'beer', 'cola'],
    ['bread', 'milk', 'diaper', 'beer'],
    ['bread', 'milk', 'diaper', 'cola']
]

# Minimum support count
min_support = 2

# Find frequent 2-itemsets
frequent_itemsets = find_frequent_2_itemsets(dataset, min_support)

# Print the results
print("Frequent 2-itemsets:")
for itemset, count in frequent_itemsets.items():
    print(f"{itemset}: {count}")
