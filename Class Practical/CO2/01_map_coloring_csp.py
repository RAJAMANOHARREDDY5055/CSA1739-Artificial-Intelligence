"""Map coloring as a Constraint Satisfaction Problem (backtracking)."""
def solve_map_coloring(graph, colors):
    assignment = {}
    def valid(region, color):
        return all(assignment.get(neighbor) != color
                   for neighbor in graph[region])
    def backtrack():
        if len(assignment) == len(graph):
            return assignment.copy()
        # Minimum remaining values heuristic
        region = min((r for r in graph if r not in assignment),
                     key=lambda r: sum(valid(r, c) for c in colors))
        for color in colors:
            if valid(region, color):
                assignment[region] = color
                result = backtrack()
                if result:
                    return result
                del assignment[region]
        return None
    return backtrack()

if __name__ == "__main__":
    australia = {
        "WA": ["NT", "SA"], "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"], "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"], "T": []
    }
    print(solve_map_coloring(australia, ["Red", "Green", "Blue"]))
