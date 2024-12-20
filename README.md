# Tetris Playfield Engine

## Overview
This program simulates a simplified Tetris-like game. Given a sequence of Tetris shapes and their positions, it calculates the resulting height of the playfield after all the shapes have been placed and completed rows have been removed.

## Features
- Supports common Tetris shapes: `Q`, `Z`, `S`, `T`, `I`, `L`, `J`.
- Dynamically adjusts the playfield height as shapes are placed.
- Removes completed rows to mimic the classic Tetris gameplay.
- Efficiently tracks the topmost occupied cell in each column for optimized placement.

## How It Works
1. **Input:** The program reads a text file where each line contains a sequence of shape actions (e.g., `T4,Z2,Q0`), representing:
    - The shape type (`T`, `Z`, etc.).
    - The column where the shape begins (`4`, `2`, etc.).
2. **Processing:**
    - Shapes are added to the playfield starting from the top, aligning with the specified column.
    - Completed rows are removed from the playfield.
    - The playfield dynamically adjusts its height as new rows are added.
3. **Output:** The resulting height of the playfield after processing all shapes is written to an output file.

## File Structure
### Input File Format
Each line in the input file represents a sequence of Tetris actions. Example:
```
T4,Z2,Q0
I0,L3,T5
```
- Each action specifies a shape and its starting column.

### Output File Format
The output file contains one number per line, representing the final height of the playfield for the corresponding input line.

### Example
#### Input File (`input.txt`):
```
T4,Z2,Q0
I0,L3,T5
```
#### Output File (`output.txt`):
```
4
6
```

## Code Explanation
### Functions
1. **`process_tetris_actions(action_sequence)`**
    - Processes a sequence of Tetris actions.
    - Adds shapes to the playfield, removes completed rows, and calculates the final height.

2. **`add_shape_to_playfield(action, playfield, column_tops)`**
    - Adds a shape to the playfield.
    - Updates the `column_tops` array to track the highest occupied cell in each column.

3. **`remove_completed_rows(playfield, column_tops)`**
    - Identifies and removes rows that are completely filled.
    - Updates the `column_tops` array accordingly.

### Main Function
- Reads the input file.
- Processes each line of Tetris actions.
- Writes the resulting heights to the output file.

## Usage
### Command Line
Run the program from the command line with the following syntax:
```
python tetris_engine.py <input_file> <output_file>
```
#### Example:
```
python tetris_engine.py input.txt output.txt
```

### Requirements
- Python 3.x

## Shape Definitions
The following shapes are supported:
- **Q** (Square):
  ```
  **
  **
  ```
- **Z**:
  ```
   **
  **
  ```
- **S**:
  ```
  **
   **
  ```
- **T**:
  ```
   *
  ***
  ```
- **I**:
  ```
  ****
  ```
- **L**:
  ```
  *
  *
  **
  ```
- **J**:
  ```
   *
   *
  **
  ```


