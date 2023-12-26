"""
1155. Number of Dice Rolls With Target Sum
Medium

You have d dice, and each die has k faces numbered 1, 2, ..., k.
Return the number of possible ways (out of k^d total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

"""
def numRollsToTarget(n: int, k: int, target: int) -> int:

    if n == 1 and target <= k:
        return 1
    elif n == 1 and target > k:
        return 0
    elif n == target:
        return 1

    # Create a diagonal matrix target rows and n columns
    matrix = [[1 if i == j else 0 for j in range(n + 1)] for i in range(target + 1)]
    matrix[0][0] = 0

    for index in range(2,min(target+1, k + 1)):
        matrix[index][1] = 1

    for t in range(3, target + 1):
        for i in range(2, min(t, n + 1)):
            counter = 0
            range_min = min(t - i + 1, k)
            for j in range(1, range_min + 1):
                counter += (matrix[t - j][i - 1])
            matrix[t][i] = counter

    return matrix[target][n] % (10 ** 9 + 7)
