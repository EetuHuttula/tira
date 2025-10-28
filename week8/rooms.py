def count_rooms(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '#' or visited[i][j]:
            return
        visited[i][j] = True
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for k in range(rows * cols):
        i = k // cols
        j = k % cols
        if grid[i][j] == '.' and not visited[i][j]:
            dfs(i, j)
            count += 1


    return count

if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2