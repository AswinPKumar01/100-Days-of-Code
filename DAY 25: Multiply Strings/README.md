# Approach
 
Converting the input strings into corresponding numerical values, multiplying them, and returning the result as a string.

# Complexity

- Time complexity: **O(M+N)**, where "M" and "N" are the lengths of the arrays "num1" and "num2" respectively.

- Space complexity: **O(1)**

# Explanation

- Create a dictionary num that maps each digit character to its numerical value.

- Initialize variables r1 and r2 to 0.

- Iterate over each character i in num1 and multiply r1 by 10 and add the numerical value of i from the num dictionary.

- Iterate over each character j in num2 and multiply r2 by 10 and add the numerical value of j from the num dictionary.

- Multiply r1 and r2 and convert the result to a string.

- Return the string representation of the multiplication result.
