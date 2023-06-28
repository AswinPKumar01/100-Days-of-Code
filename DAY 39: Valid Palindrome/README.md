# Approach

Checking if it is a palindrome (reads the same forwards and backwards) after removing non-alphanumeric characters and converting to lowercase. It returns True if it is a palindrome and False otherwise.
# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(N)**


# Explanation

- Create a variable raw and assign it the value of the string s after removing non-alphanumeric characters using a generator expression and converting it to lowercase.

- Return the result of comparing raw reversed with the original raw string, using slicing notation [::-1] which reverses the string.

- If the reversed string is equal to the original string, it is a palindrome and True is returned; otherwise, False is returned.
