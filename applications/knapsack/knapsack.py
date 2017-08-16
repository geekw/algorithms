class Knapsack:
    def __init__(self, items, target_weight):
        self._items = items
        self._target_weight = target_weight
        self._rawsolutions = list()

    """
    :type items:int an array of positive integers
    :type target_sum:int an positive integers
    """
    def fill_knapsack(self):
        self._fill(self._items, self._target_weight, set())
        for rawsolution in self._rawsolutions:
            leftrawsolutions = list(self._rawsolutions)
            leftrawsolutions.remove(rawsolution)
            for leftrawsolution in leftrawsolutions:
                if self._equalset(rawsolution, leftrawsolution):
                    self._rawsolutions.remove(rawsolution)

        self._solutions = self._rawsolutions

    def _equalset(self, set1, set2):
        if len(set1) != len(set2):
            return False
        for item1 in set1:
            if item1 not in set2:
                return False

        return True

    def _fill(self, items, target_weight, picked):
        # Validation check
        assert sum(items) >= target_weight, "Impossible, asshole!!!"

        # Found a match
        if target_weight in items:
            mypicked = picked.copy()
            mypicked.add(target_weight)
            self._rawsolutions.append(mypicked)

        # Pick an item, the problems shrinks to solving a smaller knapsack problem
        elif target_weight > min(items):
            for item in items:
                mypicked = picked.copy()
                mypicked.add(item)
                remained = list(items) # Deep copy
                remained.remove(item)
                self._fill(remained, target_weight-item, mypicked)
        # Impossible to go on
        else:
            return

    def solutions(self):
        return self._solutions