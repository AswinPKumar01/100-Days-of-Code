# Approach
 
Computes averages by sliding a window of size 2 * k + 1.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(N)**

# Explanation

- Initialize variables: Assign the length of nums to variable n, set the window size as 2k+1, and create a list named result with all elements initialized to -1.

- Check if the length of nums is less than the window size. If it is, return the result list as it is.

- Create a prefix sum array named pref_Sum with length n+1, initialized with zeros.

- Compute the prefix sum by iterating over nums and updating pref_Sum[i+1] as the sum of pref_Sum[i] and nums[i].

- Iterate over the range from k to n-k (exclusive) to define the sliding window.

- Update the result list at index i with the average of the subarray using the formula: (pref_Sum[i + k + 1] - pref_Sum[i - k]) // window.

- Return the resulting list.
