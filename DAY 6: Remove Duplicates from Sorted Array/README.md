# Approach

Iterating through both strings simultaneously, returning True if 's' is a subsequence and False otherwise.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- First checks if the length of s (the subsequence) is greater than the length of t (the target string). If yes then returns False because it means that s cannot be a subsequence of t because s is longer than t.

- If no the, the code initializes two variables i and j to 0. These variables will be used as indices to traverse the strings s and t, respectively.

- Then, a loop is used to iterate over the characters of both strings in which the code checks if the characters at index i in s is equal to the character at index j in t. If they are equal, it means that the current character in s is present in t.

- After the while loop, the code checks if i is equal to the length of s. If it is, it means that all the characters in s have been found in t in the same order, and s is a subsequence of t. In that case, the method returns True. Otherwise, it returns False, indicating that s is not a subsequence of t.
