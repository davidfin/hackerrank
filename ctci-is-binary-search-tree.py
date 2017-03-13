def check(root, min_, max_):
    if root == None:
        return True
    if root.data <= min_ or root.data >= max_:
        return False
    return check(root.left, min_, root.data) and check(root.right, root.data, max_)

def check_binary_search_tree_(root):
    return check(root, float('-inf'), float('inf'))