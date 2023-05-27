# Approach

- FInding the maximum area between two vertical lines by using the two-pointer approach.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Setting three variables:  **max_amt** to 0 (initial maximum area), **i** to 0 (left pointer), and **j** to the index of the last element in the height list (right pointer).

- While **i** less than **j**, Check if the height at index **i** is less than or equal to the height at index **j**

- If the condition is true, calculate the area a by multiplying the height at index **i** with the difference between **j** and **i** (width of the rectangle) 

- If the condition is false, calculate the area a by multiplying the height at index j with the difference between j and i.

- Check if **a** is greater than **max_amt**. If true, update **max_amt** with the value of **a**.

- After the while loop ends, return the maximum area (**max_amt**).
