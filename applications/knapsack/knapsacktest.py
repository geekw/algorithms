from knapsack import Knapsack

items = [2, 2, 5, 6, 9, 12, 14, 20]
target_weight = 30
myknapsack = Knapsack(items, target_weight)
myknapsack.fill_knapsack()
solutions =  myknapsack.solutions()
for solution in solutions:
    print solution