from pylistqueue import Queue

class ExpressionTree:
    # Builds an expression tree for the expression string.
    def __init__(self, expr_str):
        self._expr_tree = None
        self._build_tree(expr_str)

    def _build_tree(self, expr_str):
        # Build a queue containing the tokens in the expression string.
        expr_queue = Queue()
        for token in expr_str:
            expr_queue.enqueue(token)

        # Create an empty root node.
        self._expr_tree = _ExprTreeNode(None)
        # Call the recursive function to build the expression tree.
        self._rec_build_tree(self._expr_tree, expr_queue)

    def _rec_build_tree(self, current_node, expr_queue):
        # Extract the next token from the queue
        token = expr_queue.dequeue()

        if token == '(':
            current_node.left = _ExprTreeNode(None)
            self._rec_build_tree(current_node.left, expr_queue)

            # The next token will be an operator: + - * / %
            current_node.element = expr_queue.dequeue()
            current_node.right = _ExprTreeNode(None)
            self._rec_build_tree(current_node.right, expr_queue)

            # The next token will be ')', remove it
            expr_queue.dequeue()
        else:
            current_node.element = token

    # Evaluates the expression tree and returns the resulting value.
    def evaluate(self, var_dict):
        return self._eval_tree(self._expr_tree, var_dict)

    # Returns a string representation of the expression tree.
    def __str__(self):
        return self._build_string(self._expr_tree)

    # Recursively builds a string representation of the expression tree.
    def _build_string(self, tree_node):
        # If the node is a leaf, it is an operand.
        if tree_node.left is None and tree_node.right is None:
            return tree_node.element
        else: # Otherwise, it is an operator
            expr_str = '('
            expr_str += self._build_string(tree_node.left)
            expr_str += tree_node.element
            expr_str += self._build_string(tree_node.right)
            expr_str += ')'
            return expr_str

    def _eval_tree(self, subtree, var_dict):
        # See if the node is a leaf, in which case return its value
        if subtree.left is None and subtree.right is None:
            if  '0' <= subtree.element <= '9':
                return int(subtree.element)
            else:
                assert subtree.element in var_dict, "Invalid variable!"
                return var_dict[subtree.element]

        # Otherwise, it is an operator that needs to be computed.
        else:
            # Evaluate the expression in the left and right subtrees
            lvalue = self._eval_tree(subtree.left, var_dict)
            rvalue = self._eval_tree(subtree.right, var_dict)
            return self._compute_op(lvalue, subtree.element, rvalue)

    def _compute_op(self, left, op, right):
        assert op in '+-*/%', "Invalid operator!"
        if op is '+':
            return left + right
        elif op is '-':
            return left - right
        elif op is '*':
            return left * right
        elif op is '/':
            return left / right
        else:
            return left % right


class _ExprTreeNode:
    def __init__(self, data):
        self.element = data
        self.left = None
        self.right = None
