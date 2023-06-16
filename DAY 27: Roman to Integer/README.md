# Approach
 
Mapping roman numerals to their corresponding integer values in a dictionary and providing conditions using if else.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Create a dictionary r that maps Roman numerals to their corresponding integer values.

- Initialize a variable num to 0, which will store the final integer value.

- Iterate over the characters in the input string s using a for loop and index i.

- Check if the current Roman numeral at index i has a smaller value than the next Roman numeral at index (i+1).

- If true, subtract the corresponding integer value from num.

- If false, add the corresponding integer value to num.

- After the loop, add the integer value of the last Roman numeral in s to num.

- Return the final value of num.
