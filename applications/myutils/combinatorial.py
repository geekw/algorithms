
# Returns the list of permutations of a list
class Permutation:
    def __init__(self, the_list):
        self._list = the_list

    def __len__(self):
        return len(self._list)

    def solutions(self):
        return self._permute(self._list)

    # This implementation is extremely inefficient!!!
    def _permute(self, elements):
        print elements
        if len(elements) == 1:
            return [elements]
        else:
            solutions = list()
            for head in elements:
                remains = list(elements)
                remains.remove(head)
                rsolutions = self._permute(remains)
                for rsolution in rsolutions:
                    rsolution.insert(0, head)
                solutions.extend(rsolutions)
            return solutions
