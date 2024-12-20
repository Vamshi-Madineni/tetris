import sys

shapes = {
    "Q": [[0, 0], [0, 1], [1, 0], [1, 1]], 
    "Z": [[1, 0], [1, 1], [0, 1], [0, 2]], 
    "S": [[0, 0], [0, 1], [1, 1], [1, 2]], 
    "T": [[1, 0], [1, 1], [0, 1], [1, 2]], 
    "I": [[0, 0], [0, 1], [0, 2], [0, 3]], 
    "L": [[0, 0], [1, 0], [0, 1], [2, 0]], 
    "J": [[0, 0], [0, 1], [1, 1], [2, 1]]
}

def process_tetris_actions(action_sequence: list[str]):
    """
    Processes a sequence of actions, adding shapes to the playfield,
    removing completed rows, and calculating the resulting height.

    Args:
        action_sequence (list[str]): Sequence of actions representing shape placements.

    Returns:
        int: The resulting height of the playfield after all actions.
    """
    playfield = [[0] * 10]  # Create the initial line of the playfield
    column_tops = [0] * 10  # Initialize the column tops array

    for action in action_sequence:
        add_shape_to_playfield(action, playfield, column_tops)
        remove_completed_rows(playfield, column_tops)

    remove_completed_rows(playfield, column_tops)

    return len(playfield)

def add_shape_to_playfield(action, playfield, column_tops):
    """
    Adds a shape to the playfield based on the action and updates the column tops.

    Args:
        action (str): The shape and its starting column (e.g., "T4").
        playfield (list[list[int]]): The current playfield grid.
        column_tops (list[int]): List tracking the highest occupied cell in each column.
    """
    shape = shapes[action[0]]
    start_column = int(action[1])

    # Determine the minimum height for the shape to land
    min_height = 0
    for shape_element in shape:
        col_index = start_column + shape_element[1]
        min_height = max(min_height, column_tops[col_index] - shape_element[0])

    # Place the shape at the calculated height
    y = min_height
    for shape_element in shape:
        row = y + shape_element[0]
        col = start_column + shape_element[1]

        # Extend playfield if necessary
        while row >= len(playfield):
            playfield.append([0] * 10)

        playfield[row][col] = 1
        column_tops[col] = max(column_tops[col], row + 1)

def remove_completed_rows(playfield, column_tops):
    """
    Removes completed rows from the playfield and updates column tops.

    Args:
        playfield (list[list[int]]): The current playfield grid.
        column_tops (list[int]): List tracking the highest occupied cell in each column.
    """
    rows_to_remove = set()

    # Identify rows to remove
    for i in range(len(playfield)):
        if all(playfield[i]):
            rows_to_remove.add(i)

    if not rows_to_remove:
        return

    # Remove identified rows and update playfield
    new_playfield = []
    for i in range(len(playfield)):
        if i not in rows_to_remove:
            new_playfield.append(playfield[i])

    # Update playfield and column tops
    playfield.clear()
    playfield.extend(new_playfield)

    # Recalculate column tops
    column_tops[:] = [0] * 10
    for row_index, row in enumerate(playfield):
        for col_index, cell in enumerate(row):
            if cell:
                column_tops[col_index] = max(column_tops[col_index], row_index + 1)

if __name__ == "__main__":
    """
    Main function to read input from a file, process the Tetris engine, and write the output.
    """
    # Specifying the file path
    file_path = sys.argv[1]
    out_file = sys.argv[2]

    # Open the file in read mode and run the Tetris Engine
    resulting_heights = []
    with open(file_path, 'r') as file:
        # Read and process each line in the file
        for line in file:
            # Process the action sequence and return the resulting height of the stack
            resulting_heights.append(process_tetris_actions(action_sequence=line.split(",")))

    with open(out_file, 'w') as o:
        for height in resulting_heights:
            o.write(str(height) + "\n")
