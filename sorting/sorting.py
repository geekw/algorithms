class Sorting:
    def __init__(self, the_list):
        self.items = the_list

    def __len__(self):
        return len(self.items)

    # Bubble Sort
    def bubble_sort(self):
        length = len(self)
        for i in range(length-1):
            for j in range(i,length-1):
                if self.items[j] > self.items[j+1]:
                    temp_item = self.items[j]
                    self.items[j] = self.items[j+1]
                    self.items[j+1] = temp_item

        return self.items

    # Selection Sort
    def selection_sort(self):
        length = len(self)
        for i in range(length-1):
            smallest = self.items[i]
            for j in range(i+1, length):
                if self.items[j] < smallest:
                    temp_item = smallest
                    smallest = self.items[j]
                    self.items[j] = temp_item
            self.items[i] = smallest

        return self.items

    # Insertion Sort
    def insertion_sort(self):
        length = len(self)
        for i in range(1, length):
            value = self.items[i]
            pos = i
            while pos > 0 and value < self.items[pos-1]:
                self.items[pos] = self.items[pos-1]
                pos -= 1
            self.items[pos] = value

        return self.items

    # Merge Sort
    def merge_sort(self):
        return self._merge_sort(self.items)

    def _merge_sort(self, the_list):
        if len(the_list) == 1:
            return the_list
        else:
            mid = len(the_list) // 2
            left_half = self._merge_sort(the_list[:mid])
            right_half = self._merge_sort(the_list[mid:])
            new_list = self._merge_sorted_lists(left_half, right_half)
            return new_list

    def _merge_sorted_lists(self, left_half, right_half):
        new_list = list()

        whole_length = len(left_half) + len(right_half)
        while len(new_list) < whole_length:
            if len(left_half) == 0:
                new_list.extend(right_half)
            elif len(right_half) == 0:
                new_list.extend(left_half)
            else:
                if left_half[0] < right_half[0]:
                    new_list.append(left_half.pop(0))
                else:
                    new_list.append(right_half.pop(0))

        return new_list


def quick_sort(the_list):
    n = len(the_list)
    rec_quick_sort(the_list, 0, n-1)


def rec_quick_sort(the_list, first, last):
    if first >= last:
        return
    else:
        pos = partition_seq(the_list, first, last)
        rec_quick_sort(the_list, first, pos-1)
        rec_quick_sort(the_list, pos+1, last)


def partition_seq(the_list, first, last):
    pivot = the_list[first]
    left = first + 1
    right = last

    while True:
        # Find the first key larger than the pivot
        # What if None is larger than the pivot?
        while the_list[left] < pivot:
            if left == last:
                break
            left += 1
        # Here all items should be smaller than the pivot for index <= left

        # Find the last key smaller than the pivot
        # What if None is smaller than the pivot?
        # What if All is smaller than the pivot?
        while the_list[right] >= pivot:
            if right == first:
                break
            right -= 1
        # Here all items should be greater than or equal to the pivot for index >= right


        # Swap if necessary
        if left < right:
            temp_key = the_list[left]
            the_list[left] = the_list[right]
            the_list[right] = temp_key
        else:
            break

    # Put the pivot in the proper position.
    the_list[first] = the_list[right]
    the_list[right] = pivot

    # Return the index position of the pivot value.
    return right
