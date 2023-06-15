# Approach
 
Removing the paranthesis and checking whether the length of original string is same or not

# Complexity

- Time complexity: **O(N^2)**

- Space complexity: **O(N)**

# Explanation

- The function isValid takes a string s as input and returns a boolean value.

- Initialize a while loop and inside the loop, stroe the current length of s in the variable l.

- The replace function is used to remove pairs of matching brackets ('()', '{}', '[]') from the string s.

- If no replacements were made (i.e., the length of s remains the same), it means there are no more matching pairs and the function returns False.

- The loop continues until all matching pairs are removed from the string.

- If the loop completes without returning False, it means all pairs of brackets were properly balanced, and the function returns True.
