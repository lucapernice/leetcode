"""
1814. Count Nice Pairs in an Array
You are given an array nums that consists of non-negative integers.
Let us define rev(x) as the reverse of the non-negative integer x.
For example, rev(123) = 321, and rev(120) = 21.
A pair of indices (i, j) is nice if it satisfies all of the following conditions:

   - 0 <= i < j < nums.length
   - nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

Return the number of nice pairs of indices. Since that number can be too large, return it modulo 10^9 + 7.

"""

def rev(x: int) -> int:
    return int(str(x)[::-1])


def count_nice_pairs_in_an_array(nums: list[int]) -> int:
    """
    :param nums: an array of integers
    :return: the number of nice pairs in nums

    A pair (i,j) is nice if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    and so nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]).
    This means that if two numbers have the same difference, they form a nice pair.
    """
    differences = {}
    for num in nums:
        difference = num - rev(num)
        if difference in differences:
            differences[difference] += 1
        else:
            differences[difference] = 1

    nice_pairs = 0
    for difference in differences:
        nice_pairs += differences[difference] * (differences[difference] - 1) // 2

    return nice_pairs % (10 ** 9 + 7)


