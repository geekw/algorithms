from expressiontree import ExpressionTree

expr_str = '((a*(b+c))+6)'
var_dict = {'a': 5, 'b' : 3, 'c' : 8}
expr_tree = ExpressionTree(expr_str)
result = expr_tree.evaluate(var_dict)
assert expr_tree.evaluate(var_dict) == 61, "Wrong!"