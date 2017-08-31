class Sorting:
    def __init__(self, the_list):
        self.items = the_list

    def __len__(self):
        return len(self.items)

    def bubble_sort(self):
        length = len(self)
        for i in range(length-1):
            for j in range(i,length-1):
                if self.items[j] > self.items[j+1]:
                    temp_item = self.items[j]
                    self.items[j] = self.items[j+1]
                    self.items[j+1] = temp_item

        return self.items

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