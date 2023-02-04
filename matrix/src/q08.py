def solve(incoming: str) -> str:
    rows = incoming.strip().split("\n")[1:]
    n = len(rows)
    matrix = [[int(j) for j in i.split()] for i in rows]

    row_sums = [sum(matrix[i]) for i in range(n)]
    col_sums = [sum([matrix[i][j] for i in range(n)]) for j in range(n)]

    if all([x % 2 == 0 for x in row_sums + col_sums]):
        return "OK"

    for i in range(n):
        for j in range(n):
            matrix[i][j] = (matrix[i][j] + 1) % 2
            new_row_sums = [sum(matrix[k]) for k in range(n)]
            new_col_sums = [sum([matrix[k][l] for k in range(n)]) for l in range(n)]
            if all([x % 2 == 0 for x in new_row_sums + new_col_sums]):
                return f"Change bit ({i + 1},{j + 1})"
            matrix[i][j] = (matrix[i][j] + 1) % 2

    return "Corrupt"
