A boolean matrix has the parity property when each row and each column has an even sum, i.e. contains an even number of bits which are set. Here's a 4×4 matrix which has the parity property:

```
1 0 1 0
0 0 0 0
1 1 1 1
0 1 0 1
```

The sums of the rows are `2`, `0`, `4` and `2`. The sums of the columns are `2`, `2`, `2` and `2`.

Your job is to write a program that reads in a matrix and checks if it has the parity property. If not, your program should check if the parity property can be established by changing only one bit. If this is not possible either, the matrix should be classified as corrupt.

The signature of your function should be:

```python
def solve(incoming: str) -> str
```

You may implement other functions called by your `solve` function if you wish.

## Input Spec

Each input will be a multi-line string where the first line contains the size of the matrix. On the next `n` lines, there will be `n` integers per line. No other integers than `0` and `1` will occur in the matrix.

## Output Spec

For each input, your function should return a string saying either "OK", "Change bit (y,x)" if it can be corrected by flipping one bit (y is the 1-based row number, x is the 1-based column number), or "Corrupt" if it is beyond repair.

## Sample Input & Output

Input:

```
4
1 0 1 0
0 0 0 0
1 1 1 1
0 1 0 1
```

Output:

```
"OK"
```

Input:

```
4
1 0 1 0
0 0 1 0
1 1 1 1
0 1 0 1
```

Output:

```
"Change bit (2,3)"
```

Input:

```
4
1 0 1 0
0 1 1 0
1 1 1 1
0 1 0 1
```

Output:

```
"Corrupt"
```