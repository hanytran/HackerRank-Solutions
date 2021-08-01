def cavityMap(grid):
    grid_return = [grid[0]]
    grid = [[int(v) for v in value] for value in grid]
    print(grid)
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            m = grid[i][j]
            k = max(grid[i][j+1], grid[i][j-1], grid[i+1][j], grid[i-1][j])
            print(k)
            if m > k:
                grid[i][j] = 'X'
        grid_return.append(''.join([str(m) for m in grid[i]]))
    grid_return.append(''.join([str(m) for m in grid[-1]]))  
    return grid_return

grid = ['1112', '1912', '1892', '1234']
r = cavityMap(grid)
print(r)