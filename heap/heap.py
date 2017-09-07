class MaxHeap:
    def __init__(self, capacity):
        self._items = [None] * capacity
        self._count = 0

    def __len__(self):
        return self._count

    def capacity(self):
        return len(self._items)

    def add(self, value):
        assert self._count < self.capacity(), "Cannot add to a full heap"
        self._items[self._count] = value
        self._sift_up(self._count)
        self._count += 1

    def extract(self):
        assert self._count > 0, "Cannot extract from an empty heap"
        result = self._items[0]
        self._count -= 1
        # Move the last leaf to root
        self._items[0] = self._items[self._count]
        self._items[self._count] = None

        self._sift_down(0)
        return result

    def _sift_up(self, current_pos):
        while current_pos > 0:
            parent_pos = (current_pos - 1) / 2
            if self._items[current_pos] > self._items[parent_pos]:
                # Swap it with its parent
                self._swap_items(current_pos, parent_pos)
                current_pos = parent_pos
            else:
                break

    def _sift_down(self, current_pos):
        while True:  # ToDo: make it more explicit
            left_pos = current_pos * 2 + 1
            right_pos = current_pos * 2 + 2
            if left_pos >= self._count:
                break
            elif right_pos >= self._count:
                bigger_pos = left_pos
            else:
                if self._items[left_pos] > self._items[right_pos]:
                    bigger_pos = left_pos
                else:
                    bigger_pos = right_pos

            # Swap current_pos with bigger_pos if not complying with max heap criteria
            if self._items[bigger_pos] > self._items[current_pos]:
                self._swap_items(bigger_pos, current_pos)
                current_pos = bigger_pos
            else:
                break

    def _swap_items(self, lindex, rindex):
        temp_item = self._items[lindex]
        self._items[lindex] = self._items[rindex]
        self._items[rindex] = temp_item
