# Approach
 
Using **Kadane's Algorithm** to scan the entire array, along with finding the sum of elements while traversing and finally extracting the maximum sum.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation:

- Initializing two variables: **current_sum** for keeping track of the sum of the elements and a max_sum variable to store the larget sum.

- Iterating through each element of the array and adding current element of the array to the **current_sum** variable.

- If the **current_sum** is greater than the max_sum, we update the **max_sum** to be the current sum.

- If the **current_sum** becomes negative, we reset it to 0. This is because any negative sum would only decrease the total sum of a potential subarray.

- After iterating through all elements, we return the **max_sum** as the maximum sum of a subarray.
