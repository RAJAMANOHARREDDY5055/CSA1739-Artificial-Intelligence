"""Alpha-beta pruning with a small game tree."""
def minimax(node, depth, alpha, beta, maximizing):
    if depth == 0 or isinstance(node, int):
        return node if isinstance(node, int) else 0
    if maximizing:
        value = float("-inf")
        for child in node:
            value = max(value, minimax(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta: break
        return value
    value = float("inf")
    for child in node:
        value = min(value, minimax(child, depth-1, alpha, beta, True))
        beta = min(beta, value)
        if beta <= alpha: break
    return value

if __name__ == "__main__":
    tree = [[3, 5], [6, 9]]  # root MAX, then MIN, then leaf values
    print("Optimal value:", minimax(tree, 2, float("-inf"), float("inf"), True))
