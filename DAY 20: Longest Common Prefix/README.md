# Approach
 
Sorting and iterating through the elements

# Complexity

- Time complexity: **O(NMlog(N))**, where N is the number of strings in the input list and M is the average length of the strings

- Space complexity: **O(M)**

# Explanation

- Initialize an empty string "pref" to store the longest common prefix.

- Sort the input list of strings in lexicographic order and getting the first and last string from the sorted list using indexing.

- Iterate through the characters of the first and last string simultaneously and Check if the characters at the current index are not equal.

- If the characters are not equal, return the current prefix: return pref.

- If the characters are equal, append the current character to the prefix: pref += first[i].

- After the loop ends, return the final prefix: return pref.
