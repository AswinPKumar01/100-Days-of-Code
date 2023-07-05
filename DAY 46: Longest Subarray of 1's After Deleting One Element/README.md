# Approach
 
Iterating through the list using two pointers.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize the variable 'zero' to 1, which represents the number of zeros that can still be removed from the subarray.

- Initialize 'l' and 'r' to 0, representing the left and right pointers of the subarray.

- Iterate through the 'nums' list using the 'r' pointer.

- Subtract 1 from 'zero' if the current element at 'r' is equal to 0, indicating that a zero has been encountered.

- Check if 'zero' is less than 0, which means we have encountered more zeros than the allowed limit.

- If 'zero' is less than 0, increment 'zero' by 1 if the element at 'l' is equal to 0, indicating that a zero can be removed from the left end of the subarray.

- Increment 'l' by 1 to move the left pointer towards the right.

- Continue steps 4-7 until the end of the 'nums' list is reached.

- Return the difference between 'r' and 'l', which represents the length of the longest subarray that satisfies the condition.
