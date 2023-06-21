# Approach
 
Using Binary Search

# Complexity

- Time complexity: **O(log N + 2N)**

- Space complexity: **O(1)**

# Explanation

- Find the minimum value (ii) and maximum value (j) from the nums list.

- Enter a while loop until ii is less than j and calculate the middle value (mid) as the floor division of the sum of ii and j divided by 2.

- Initialize total1 and total2 as 0 and iterate through each index i in the range of len(nums).

- Increment total1 by the absolute difference between mid and nums[i], multiplied by cost[i].

- Increment total2 by the absolute difference between mid+1 and nums[i], multiplied by cost[i].

- Compare total1 and total2: and if total1 is less than total2, update j to mid, otherwise, update ii to mid+1.

- After exiting the while loop, initialize ans as 0 and iterate through each index i in the range of len(nums).

- Increment ans by the absolute difference between ii and nums[i], multiplied by cost[i].

- Return the final ans.
