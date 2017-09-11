from bstmap import BSTMap

tree = BSTMap()
tree.add(60, "sixty")
tree.add(25, "twenty five")
tree.add(100, "one hundred")
tree.add(35, "thirty five")
tree.add(17, "seventeen")
tree.add(80, "eighty")

assert len(tree) == 6, "Wrong Length!"

for key in tree:
    print key, tree.value_of(key)

tree.remove(100)
tree.remove(60)
tree.remove(25)
tree.remove(17)
tree.remove(35)
tree.remove(80)
# assert  len(tree) == 0, "Wrong Length!"
