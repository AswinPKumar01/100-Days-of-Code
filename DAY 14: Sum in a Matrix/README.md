# Approach
 
Sorting the array in ascending order to make the highest number to the end of the array and then returning the sum of all the highest numbers.

# Complexity

- Time complexity: **O(NMlog(M))**, **n** is the number of rows and **m** is the number of columns in the matrix.

- Space complexity: **O(1)**

# Explanation

- Initialize a variable sum to 0, which will store the sum of the highest values.

- Sort each row of the matrix nums in ascending order.

- Iterate through the columns and  initialize a variable highest to 0, which will store the highest value found in that column for each column.

- Iterate through the rows and update highest by comparing the current element in the column with highest and taking the maximum.

- Add the highest value to sum.

- Return the sum value.
