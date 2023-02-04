Michael's specialty is pancakes. Every day, he makes many pancakes in his restaurant's kitchen. He piles them up as he makes them and always puts the newest pancake on top. He likes variety in his piles so he makes the pancakes of different sizes.

As the pancake on top gets cold the quickest, he occasionally puts his spatula between pancakes in the pile and flips them. That way; the pancake on top is now in the middle and the pancake in the middle is on top.

After several flips, can you tell which pancake is on the top?

The signature of your function should be:

```python
def solve(pancake_pile: List[int], flips: List[int]) -> int
```

You may implement other functions called by your `solve` function if you wish.

## Input Spec

The input will be two lists of integers. First, a list with the pancake sizes starting from the bottom, the last being the top pancake. 

Second, a list with the amount of pancakes he flips with each flip; these numbers will always be less than the amount of pancakes in the pile.

## Output Spec

The output should be the size of the pancake on top.

## Sample Input & Output

| Sample number | Input                       | Output |
| ------------- | --------------------------- | ------ |
| 1             | `[5, 4, 3, 2, 1]`, `[]`     | `1`    |
| 1             | `[5, 4, 3, 2, 1]`, `[3, 2]` | `2`    |
| 1             | `[5, 4, 3, 2, 1]`, `[5]`    | `5`    |