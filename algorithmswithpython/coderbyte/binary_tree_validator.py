def is_valid_binary_tree(client_tree: list[str]) -> bool:
    parent_children = parent_child_map(parse_input(client_tree))
    all_parents = set(parent_children.keys())
    all_children = {child for children in parent_children.values() for child in children}
    print(f'parent={all_parents}')
    print(f'children={all_children}')
    root_nodes = all_parents - all_children
    print(f'root_nodes={root_nodes}')
    non_binary_node = list(filter(lambda family: len(family[1]) > 2, parent_children.items()))
    if len(root_nodes) > 1 or len(non_binary_node) > 0 or has_cycle(parent_children):
        # if there is more than one root or a node has more than 2 children
        print('Not a valid binary tree - more than one node and non-binary node')
        return False
    print('valid binary tree')
    return True


def has_cycle(tree: dict[int, set[int]]) -> bool:
    visited_nodes = []
    for parent in tree.keys():
        for child in tree[parent]:
            if child in visited_nodes:
                print('Not a valid binary tree - has cycle')
                return True
            visited_nodes.append(child)
    return False


def parse_input(pairs: list[str]) -> list[tuple]:
    def parser_lambda(pair: str):
        return pair.strip('( )').split(',')
    maps = [(tuple(map(int, parser_lambda(str_pair)))) for str_pair in pairs]
    return maps


def parent_child_map(node_pairs: list[tuple]) -> dict[int, set[int]]:
    parent_child = {}
    for pair in node_pairs:
        if pair[1] not in parent_child:
            parent_child[pair[1]] = {pair[0]}
        else:
            parent_child[pair[1]].add(pair[0])
    print(f'tree={parent_child}')
    return parent_child


if __name__ == '__main__':
    ex_nodes = ['(1,2)', '(2,4)',  '(5,7)', '(7,2)', '(9,5)']
    #["(1,2)", "(2,4)", "(7,2)", "(7,2)", "(8, 4)", "(3,8)"]
    is_valid_binary_tree(ex_nodes)
