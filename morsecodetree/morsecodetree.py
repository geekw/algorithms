import string


class MorseCodeTree:
    def __init__(self):
        self._build_code_tree()
        self._rev_path = "" # For encoding

    def _build_code_tree(self):
        self._root = _TreeNode()

        character_map = {key:_TreeNode(key) for key in string.uppercase }

        self._root.left = character_map['E']
        self._root.right = character_map['T']
        character_map['E'].left = character_map['I']
        character_map['E'].right = character_map['A']
        character_map['T'].left = character_map['N']
        character_map['T'].right = character_map['M']
        character_map['I'].left = character_map['S']
        character_map['I'].right = character_map['U']
        character_map['A'].left = character_map['R']
        character_map['A'].right = character_map['W']
        character_map['N'].left = character_map['D']
        character_map['N'].right = character_map['K']
        character_map['M'].left = character_map['G']
        character_map['M'].right = character_map['O']
        character_map['S'].left = character_map['H']
        character_map['S'].right = character_map['V']
        character_map['U'].left = character_map['F']
        character_map['R'].left = character_map['L']
        character_map['W'].left = character_map['P']
        character_map['W'].right = character_map['J']
        character_map['D'].left = character_map['B']
        character_map['D'].right = character_map['X']
        character_map['K'].left = character_map['C']
        character_map['K'].right = character_map['Y']
        character_map['G'].left = character_map['Z']
        character_map['G'].right = character_map['Q']

    def decode(self, sequence):
        assert 0 < len(sequence) <= 4, "Illegal length"

        current_node = self._root
        for character in sequence:
            assert character is "." or character is "-", "Illegal character!"
            if character is "." and current_node.left is not None:
                current_node = current_node.left
            elif current_node.right is not None:
                current_node = current_node.right
            else:
                return None

        return current_node.character

    def encode(self, character):
        assert character in string.lowercase or character in string.uppercase, "Illegal character!"
        character = string.upper(character)
        if self._search(character, self._root):
            return self._rev_path[::-1]
        else:
            return None

    def _search(self, character, current_pos):
        if current_pos is not None:
            if current_pos.character == character:
                return True
            if self._search(character, current_pos.left):
                self._rev_path += "."
                return True
            if self._search(character, current_pos.right):
                self._rev_path += "-"
                return True
        else:
            return False


class _TreeNode:
    def __init__(self, character = None):
        self.character = character
        self.left = None
        self.right = None