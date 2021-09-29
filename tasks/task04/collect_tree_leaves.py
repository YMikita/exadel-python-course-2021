def collect_leaves(leaves):
    if not isinstance(leaves, dict):
        return leaves

    result = []
    for node in leaves:
        result.extend(collect_leaves(leaves[node]))
    return result


tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [31, 5]
       },
       "node12": [31]
   },
   "node2": [7, 8, 9]
}

tests_error_message = "Collect_leaves function does not work correctly"

assert collect_leaves(tree) == [1, 2, 3, 31, 5, 31, 7, 8, 9], tests_error_message
assert collect_leaves([1, 2, 3]) == [1, 2, 3], tests_error_message
print("Tests passed")

