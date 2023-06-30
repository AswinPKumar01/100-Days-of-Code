# Approach
 
using the sliding window technique. It maintains a sliding window between left and right indices, and updates the window boundaries and a character index array idx to track the last occurrence of each character. Finally, it returns the maximum length of a valid substring encountered.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize variables: n with the length of the input string s, max_len as 0 to track the maximum length, idx as a list of 128 elements initialized with -1, and left as 0 to represent the left pointer.

- Iterate over each character in the string using the right pointer.

- Check if the current character has appeared before by comparing the index of the character in the idx list with the left pointer.

- If the index is greater than or equal to left, it means the character has appeared in the current substring. Update the left pointer to the next index after the last occurrence of the character.

- Update the index of the current character in the idx list to the current right pointer.

- Calculate the length of the current substring by subtracting left from right and adding 1. Update max_len if the current length is greater than the previous maximum length.

- Repeat steps 2-5 for the remaining characters in the string.

- Return the maximum length of a substring without repeating characters.
