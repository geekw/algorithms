class BSTMap:
    # Creates an empty map instance.
    def __init__(self):
        self._root = None
        self._size = 0

    # Returns the number of entries in the map
    def __len__(self):
        return self._size

    # Returns an iterator for traversing the keys in the map
    def __iter__(self):
        return _BSTMapIterator(self._root, self._size)

    # Determines if the map contains the given key.
    def __contains__(self, key):
        return self._bst_search(self._root, key) is not None

    # Returns the value associated with the key.
    def value_of(self, key):
        node = self._bst_search(self._root, key)
        assert node is not None, "Invalid map key."
        return node.value

    # Helper method that recursively searches the tree for a target key.
    def _bst_search(self, subtree, target):
        if subtree is None:
            return None
        elif target < subtree.key:  # target is left of subtree root
            return self._bst_search(subtree.left, target)
        elif target > subtree.key:  # target is right of subtree root
            return self._bst_search(subtree.right, target)
        return subtree

    # Add a new entry to a map or replacing an existing key.
    def add(self, key, value):
        node = self._bst_search(self._root, key)
        # Finding the node containing the key, if it exists.
        if node is not None:
            node.value = value
            return False
        # Otherwise, add a new entry
        else:
            self._root = self._bst_insert(self._root, key, value)
            self._size += 1
            return True

    # Helper method for inserting a new item recursively
    def _bst_insert(self, subtree, key, value):
        if subtree is None:
            subtree = _BSTMapNode(key, value)
        elif key < subtree.key:
            subtree.left = self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            subtree.right = self._bst_insert(subtree.right, key, value)
        return subtree

    # Removes the map entry associated with the given key.
    def remove(self, key):
        assert key in self, "Invalid map key!"
        self._root = self._bst_remove(self._root, key)
        self._size -= 1

    # Helper method that removes an existing item recursively.
    def _bst_remove(self, subtree, target):
        # Search for the item in the tree.
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._bst_remove(subtree.left, target)
            return subtree
        elif target > subtree.key:
            subtree.right = self._bst_remove(subtree.right, target)
            return subtree
        # We found the node containing the item
        else:
            if subtree.left is None and subtree.right is None: # 0-0
                return None
            elif subtree.left is not None and subtree.right is None: # 1-0
                return subtree.left
            elif subtree.left is None and subtree.right is not None: # 0 - 1
                return subtree.right
            else: # 1-1
                successor = self._bst_maximum(subtree.left)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.left = self._bst_remove(subtree.left, successor.key)
                return subtree

    # Helper method for finding the node containing the minimum key.
    def _bst_minimum(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bst_minimum(subtree.left)

    # Helper method for finding the node containing the maximum key.
    def _bst_maximum(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._bst_maximum(subtree.right)


# Storage class for the binary search tree nodes of the map
class _BSTMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


# Iterator for BST Map
class _BSTMapIterator :
    def __init__(self, root, size):
        # Creates the array and fills it with the keys.
        self._the_keys = [None]*size
        self._current_item = 0 # Keep track of the next location in the array
        self._bst_traversal(root)
        self._current_item = 0 # Reset the current item index

    def __iter__(self):
        return self

    # Returns the next key in the array of keys
    def next(self):
        if self._current_item < len(self._the_keys):
            key = self._the_keys[self._current_item]
            self._current_item += 1
            return key
        else:
            raise StopIteration

    # Performs an inorder traversal used to build the array of keys.
    def _bst_traversal(self, subtree):
        if subtree is not None:
            self._bst_traversal(subtree.left)
            self._the_keys[self._current_item] = subtree.key
            self._current_item += 1
            self._bst_traversal(subtree.right)

