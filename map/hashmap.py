# Implementation of the Map ADT using closed hashing and a probe with
# double hashing.

# Storage class for holding the key/value pairs.
class _HashMapEntry:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


# Iterator class for HashMap
class _MapIterator:
    def __init__(self, the_table):
        self._mapItems = the_table
        self._curItem = 0

    def __iter__(self):
        return self

    def next(self):
        if self._curItem < len(self._mapItems):
            prev_pos = self._curItem
            for item in self._mapItems[prev_pos:]:
                self._curItem += 1
                if item is not HashMap.UNUSED or item is not HashMap.EMPTY:
                    return item
        else:
            raise StopIteration


class HashMap:
    # Defines constants to represent the status of each table entry.
    UNUSED = None
    EMPTY = _HashMapEntry()

    # Creates an empty map instance.
    def __init__(self):
        self._table = [self.UNUSED] * 7
        self._count = 0
        self._max_count = len(self._table) - len(self._table) / 3

    # Returns the number of entries in the map.
    def __len__(self):
        return self._count

    # Determines if the map contains the given key.
    def __contains__(self, key):
        slot = self._find_slot(key, False)
        return slot is not None

    # Adds a new entry to the map if the key does not exist. Otherwise, the
    # new value replaces the current value associated with the key.
    def add(self, key, value):
        if key in self:
            slot = self._find_slot(key, False)
            self._table[slot].value = value
            return False
        else:
            slot = self._find_slot(key, True)
            self._table[slot] = _HashMapEntry(key, value)
            self._count += 1
            if self._count == self._max_count:
                self._rehash()
            return True

    # Returns the value associated with the key.
    def value_of(self, key):
        slot = self._find_slot(key, False)
        assert slot is not None, "Invalid map key."
        return self._table[slot].value

    # Removes the entry associated with the key.
    def remove(self, key):
        slot = self._find_slot(key, False)
        assert slot is not None, "Invalid map key."
        entry = self._table[slot]
        self._count -= 1
        self._table[slot] = self.EMPTY
        return entry

    # Returns an iterator for traversing the keys in the map
    def __iter__(self):
        return _MapIterator(self._table)

    # Finds the slot containing the key or where the key can be added.
    # forInsert indicates if the search is for an insertion, which locates
    # the slot into which the new key can be added.
    def _find_slot(self, key, for_insert):
        # Compute the home slot and the step size.
        slot = self._hash1(key)
        step = self._hash2(key)

        # Probe for the key
        M = len(self._table)
        while True:
            if for_insert:
                if self._table[slot] is self.EMPTY \
                        or self._table[slot] is self.UNUSED:
                    return slot;
                else:
                    slot = (slot + step) % M
            else:
                if self._table[slot] is self.UNUSED:
                    return None
                elif self._table[slot] is self.EMPTY:
                    slot = (slot + step) % M
                else:
                    if self._table[slot].key == key:
                        return slot
                    else:
                        slot = (slot + step) % M

    # Rebuilds the hash table.
    def _rehash(self):
        # Create a new larger table.
        orig_table = self._table
        new_size = len(self._table) * 2 + 1
        self._table = [None]*new_size

        # Modify the size attributes.
        self._count = 0
        self._max_count = new_size - new_size // 3

        # Add the keys from the original array to the new table.
        for entry in orig_table:
            if entry is not self.UNUSED and entry is not self.EMPTY:
                slot = self._find_slot(entry.key, True)
                self._table[slot] = entry
                self._count += 1

    # The main hash function for mapping keys to table entries.
    def _hash1(self, key):
        return abs(hash(key)) % len(self._table)

    # The second hash function used with double hashing probes.
    def _hash2(self, key):
        return 1 + abs(hash(key)) % (len(self._table) - 2)



