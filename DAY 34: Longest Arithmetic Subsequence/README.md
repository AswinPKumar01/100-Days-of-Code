# Approach

Using Dynamic Programming

# Complexity

- Time complexity: **O(N^2)**
- Space complexity: **O(N^2)**

# Explanation

- Initialize the length of the list n as the length of the input list nums.

- If the length of the list is less than or equal to 2, return the length itself since any subsequence of length 2 or less will always have the same length.

- Initialize the variable longest to 2, which represents the length of the longest arithmetic subsequence found so far.

- Create a list dp of dictionaries, where each dictionary will store the length of arithmetic subsequences ending at a particular index i with a specific difference.

- Iterate over the indices i from 0 to n-1.

- For each index i, iterate over the indices j from 0 to i-1.

-  Calculate the difference between nums[i] and nums[j].

- Update dp[i][diff] to be equal to dp[j].get(diff, 1) + 1, which means the length of the arithmetic subsequence ending at index i with a difference of diff is equal to the length of the subsequence ending at index j with the same difference, incremented by 1.

- Update longest to be the maximum value between longest and dp[i][diff].

- After the loops, return the value of longest, which represents the length of the longest arithmetic subsequence.
