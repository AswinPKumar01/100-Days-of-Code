# Approach
 
Direct Approach

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(N)**

# Explanation

- Count the number of spaces in the input text using the count() method, and store it in the variable space.

- Split the input text into individual words using the split() method, and store the resulting list in the variable words.

- Determine the number of words in the text by getting the length of the words list and store it in the variable length.

- Calculate the number of spaces to be inserted between each word (denoted by r). If there are more than one word, divide the total number of spaces by the number of word gaps (length - 1); otherwise, set r to the total number of spaces.

- Initialize an empty string a to store the final result.

- Iterate over each word in the words list:

- Append the current word to the string a.

- If the remaining spaces (space) is greater than or equal to r, append r spaces after the current word and subtract r from space.

- If there are still spaces remaining (space > 0), append the remaining spaces to the string a.

- Return the final reordered string a.
