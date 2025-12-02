target_row = 2981
target_col = 3075

# target_row = 3
# target_col = 3

initial_value = 20151125
multiplier = 252533
modulus = 33554393

row = 0
col = 0
grid = [[0]*(target_row+target_col-1)]*(target_row+target_col-1)
grid[row][col] = initial_value

while True:
    previous_value = grid[row][col]
    if row == 0:
        row = col + 1
        col = 0
    else:
        row -= 1
        col += 1
    grid[row][col] = (previous_value * 252533) % modulus
    # print(f"{row+1}x{col+1} {grid[row][col]}")
    if row == target_row - 1 and col == target_col - 1:
        break
print("Advent of Code 2015 Day 25")
print(f"Part One: {grid[target_row - 1][target_col - 1]}")
