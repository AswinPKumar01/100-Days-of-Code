# Approach

Using two variables to reduce the index searching from both the sides and finally returning the index if its equal
# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize leftSum to 0 and rightSum to the sum of all elements in nums.

- Iterate over each element in nums using the enumerate function to access both the index and the value of each element.

- Subtract the current element from rightSum.

- Check if leftSum is equal to rightSum. If they are equal, return the current index as the pivot index.

- Add the current element to leftSum.

- If no pivot index is found in the loop, return -1.
