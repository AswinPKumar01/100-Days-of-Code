# Approach
 
Adding digits and carry overs from both left and right side.
# Complexity

- Time complexity: **O(max(N,M))**, where N and M are the lengths of strings a and b respectively

- Space complexity: **O(max(N,M))**

# Explanation

- Initialize an empty string s to store the result, a variable carry to keep track of the carry value during addition and variables i and j to point to the last index of strings a and b, respectively.

- Enter a while loop in which: 

- If i is greater than or equal to 0, add the integer value of a[i] to the carry, decrement i by 1.

- If j is greater than or equal to 0, add the integer value of b[j] to the carry, decrement j by 1.

- Compute the current bit of the result by taking the modulo of carry with 2 and appending it to the front of string s.

- Update carry by integer dividing it by 2.

- Return the final binary string s.
