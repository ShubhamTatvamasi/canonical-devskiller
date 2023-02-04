from typing import List

def solve(pancake_pile: List[int], flips: List[int]) -> int:
    for flip in flips:
        pancake_pile = pancake_pile[:flip][::-1] + pancake_pile[flip:]
    return pancake_pile[-1]
