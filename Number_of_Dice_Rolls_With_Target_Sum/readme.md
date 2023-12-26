# NumberOfDiceToRoll

This Python project contains a function `numRollsToTarget` that calculates the number of possible ways to roll `n` dice (each with `k` faces numbered from 1 to `k`) so that the sum of the face-up numbers equals a given `target`. The result is returned modulo 10^9 + 7 to prevent overflow.

## Function Explanation

Here's a step-by-step explanation of the function:

1. The function takes three parameters: `n` (the number of dice), `k` (the number of faces on each die), and `target` (the sum that we want the face-up numbers to add up to).

2. If there is only one die (`n == 1`), and the `target` is less than or equal to `k` (the number of faces on the die), there is only one way to achieve the target (by rolling the `target` number), so the function returns `1`. If the `target` is greater than `k`, it's impossible to achieve the target with one die, so the function returns `0`.

3. If the number of dice `n` is equal to the `target`, there is only one way to achieve the target (by rolling a `1` on each die), so the function returns `1`.

4. The function then creates a `matrix` with `target + 1` rows and `n + 1` columns. The diagonal is filled with `1`s, and the rest of the elements are `0`s. This matrix will be used to store the number of ways to achieve each possible sum with each possible number of dice.

5. The function then fills the second column of the matrix (which corresponds to using one die) with `1`s for sums from `2` to `min(target, k)` (since these are the possible sums that can be achieved with one die).

6. The function then iterates over each possible sum `t` from `3` to `target`, and for each number of dice `i` from `2` to `min(t, n + 1)`, it calculates the number of ways to achieve the sum `t` with `i` dice. This is done by summing the number of ways to achieve the sum `t - j` with `i - 1` dice, for each `j` from `1` to `min(t - i + 1, k)`. This value is then stored in `matrix[t][i]`.

7. Finally, the function returns the number of ways to achieve the `target` sum with `n` dice, which is stored in `matrix[target][n]`, modulo 10^9 + 7.

This function uses dynamic programming to efficiently calculate the number of ways to achieve each possible sum with each possible number of dice. The time complexity is O(`n` * `target` * `k`), and the space complexity is O(`n` * `target`).

## Testing

The project also includes a test suite for the `numRollsToTarget` function, using Python's built-in `unittest` module. The test suite contains several test cases, each of which tests the function with different inputs and compares the output with the expected output.

