# -----------------------------
# Manuscript Sorting Problem
# (8-Puzzle Variant Formulation)
# -----------------------------

class ManuscriptSortingProblem:
    
    def __init__(self, initial_state):
        """
        State Representation:
        The 3x3 grid is represented as a string of length 9.
        'B' represents the Blank (empty slot).
        
        Example:
        "1234567B8"
        """
        self.initial_state = initial_state
        
        # Goal State:
        # Manuscripts must be in order: 1 2 3 / 4 5 6 / 7 B 8
        self.goal_state = "1234567B8"
        
        # Valid moves based on blank index
        self.moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7]
        }

    # -----------------------------
    # Actions Function
    # -----------------------------
    def actions(self, state):
        """
        Returns possible actions (Up, Down, Left, Right)
        by checking valid blank movements.
        """
        blank_index = state.index('B')
        possible_actions = []

        row, col = divmod(blank_index, 3)

        if row > 0:
            possible_actions.append("Up")
        if row < 2:
            possible_actions.append("Down")
        if col > 0:
            possible_actions.append("Left")
        if col < 2:
            possible_actions.append("Right")

        return possible_actions

    # -----------------------------
    # Result Function
    # -----------------------------
    def result(self, state, action):
        """
        Returns new state after applying an action.
        """
        blank_index = state.index('B')
        new_state = list(state)

        row, col = divmod(blank_index, 3)

        if action == "Up":
            swap_index = (row - 1) * 3 + col
        elif action == "Down":
            swap_index = (row + 1) * 3 + col
        elif action == "Left":
            swap_index = row * 3 + (col - 1)
        elif action == "Right":
            swap_index = row * 3 + (col + 1)

        new_state[blank_index], new_state[swap_index] = \
            new_state[swap_index], new_state[blank_index]

        return "".join(new_state)

    # -----------------------------
    # Goal Test
    # -----------------------------
    def goal_test(self, state):
        """
        Checks whether the current state is the goal state.
        """
        return state == self.goal_state

    # -----------------------------
    # Path Cost Function
    # -----------------------------
    def path_cost(self, cost_so_far, state1, action, state2):
        """
        Each move costs 1 unit of System Energy.
        """
        return cost_so_far + 1


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    problem = ManuscriptSortingProblem("123B45678")
    
    print("Initial State:", problem.initial_state)
    print("Goal State:", problem.goal_state)
    print("Possible Actions:", problem.actions(problem.initial_state))
    
    new_state = problem.result(problem.initial_state, "Down")
    print("State after moving Down:", new_state)
    
    print("Is Goal?", problem.goal_test(new_state))
