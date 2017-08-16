from knapsack import Knapsack

items = [2, 5, 6, 9, 12, 14, 20]
target_weight = 30
# items = [2, 5]
# target_weight = 7
myknapsack = Knapsack(items, target_weight)
myknapsack.fill_knapsack()
solutions =  myknapsack.solutions()
print len(solutions)