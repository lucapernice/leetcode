""" Leetcode 91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1, 'B' -> 2, ... 'Z' -> 26
Given a string of digits, determine the number of ways to decode it.
"""


def extract_first(s: str) -> (int, str):
    """ Extract the first character from string s and return it as an int
    and the remaining string.
    """
    if len(s) == 0:
        return None, None
    else:
        return int(s[0]), s[1:]


def numDecodings(s: str) -> int:
    """ Return the number of ways to decode string s.
    """

    if len(s) == 0:
        return 0

    first, rest = extract_first(s)

    # base cases
    if first == 0:
        return 0

    if len(rest) == 0:
        return 1

    if len(rest) == 1:
        if int(rest) == 0:
            return 1
        if int(s) <= 26:
            return 2
        else:
            return 1

    # recursive case
    if int(s[:2]) <= 26:
        return numDecodings(rest) + numDecodings(s[2:])
    else:
        return numDecodings(rest)


def main():
    s = "11111111111111111111111110"
    print(f"numDecodings({s}) = {numDecodings(s)}")

if __name__ == "__main__":
    main()
