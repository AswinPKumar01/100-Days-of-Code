# Approach

Using simple loop and iteration to check for values and replace it.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize a variable **'a'** to keep track of the new index while iterating through the list.

- Iterate through each element **'i'** in **'nums'.**

- If **'i'** is not equal to the given value **'val'** then update **'nums[a]'** to the current value of **'i'.**

- Increment **'a'** by 1 to move to the next position in **'nums'.**

- Finally, return the value of **'a'**, which represents the new length of the modified list.
