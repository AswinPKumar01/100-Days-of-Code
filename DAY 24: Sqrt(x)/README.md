# Approach
 
Using binary search logic.


# Complexity

- Time complexity: **O(logN)**

- Space complexity: **O(1)**

# Explanation

- Check if x is equal to 0 or 1. If so, return x as the square root.

- Set the maximum value (max) to x and the minimum value (min) to 0.

- Set q as the floor division of the sum of min and max divided by 2.

- Enter a loop that continues as long as min is less than max to calculate c as the square of q.

- If c is equal to x, return q as the square root else if c is less than x, update min to q + 1.

- Else, if c is greater than x, update max to q.

- Recalculate q as the floor division of the sum of min and max divided by 2.

- Return q - 1 as the square root approximation.
