from itertools import combinations

class Knapsack:
    def __init__(self, items, target_weight):
        self._items = items
        self._target_weight = target_weight
        self._solutions = list()

    def fill_knapsack(self):
        assert min(self._items) <= self._target_weight <= sum(self._items), "Impossible, asshole!"
        for number_of_items in range(1, len(self._items)+1):
            combis = combinations(self._items, number_of_items)
            for combi in combis:
                if sum(combi) == self._target_weight:
                    self._solutions.append(combi)


    def solutions(self):
        return self._solutions