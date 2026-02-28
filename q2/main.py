from collections import defaultdict

# Variables
slots = ["Slot1", "Slot2", "Slot3", "Slot4"]

# Domains
domains = {
    "Slot1": ["A", "B", "C"],
    "Slot2": ["A", "B", "C"],
    "Slot3": ["A", "B", "C"],
    "Slot4": ["A", "B"]  # C removed (maintenance)
}

# Adjacency for No Back-to-Back
neighbors = {
    "Slot1": ["Slot2"],
    "Slot2": ["Slot1", "Slot3"],
    "Slot3": ["Slot2", "Slot4"],
    "Slot4": ["Slot3"]
}


# -----------------------------
# Constraint Check
# -----------------------------

def is_consistent(var, value, assignment):
    # No Back-to-Back
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True


# -----------------------------
# Minimum Remaining Values (MRV)
# -----------------------------

def select_unassigned_variable(assignment):
    unassigned = [v for v in slots if v not in assignment]
    return min(unassigned, key=lambda var: len(domains[var]))


# -----------------------------
# Forward Checking
# -----------------------------

def forward_check(var, value, assignment, local_domains):
    for neighbor in neighbors[var]:
        if neighbor not in assignment:
            if value in local_domains[neighbor]:
                local_domains[neighbor].remove(value)
                if not local_domains[neighbor]:
                    return False
    return True


# -----------------------------
# Backtracking Search
# -----------------------------

def backtrack(assignment, local_domains):

    if len(assignment) == len(slots):
        # Check Minimum Coverage
        used_bots = set(assignment.values())
        if {"A", "B", "C"}.issubset(used_bots):
            return assignment
        return None

    var = select_unassigned_variable(assignment)

    for value in local_domains[var]:
        if is_consistent(var, value, assignment):

            new_assignment = assignment.copy()
            new_assignment[var] = value

            new_domains = {v: local_domains[v].copy() for v in local_domains}
            
            if forward_check(var, value, new_assignment, new_domains):
                result = backtrack(new_assignment, new_domains)
                if result:
                    return result

    return None


# -----------------------------
# Run CSP
# -----------------------------

solution = backtrack({}, domains)

print("Solution:")
print(solution)
