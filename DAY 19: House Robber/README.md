# Approach
 
Looping and getting highest non adjacent sum

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize variables curr and end to 0. These variables keep track of the maximum amount that can be robbed considering the current house and the previous house, respectively.

- Iterate through each house value i in the given list nums:

- Update end to the value of curr which is the maximum amount that can be robbed from the previous house.

- Update curr to the maximum between end + i, the amount that can be robbed if the current house is robbed and curr, the amount that can be robbed if the current house is not robbed.

- Return the value of curr, which represents the maximum amount that can be robbed from the given list of houses.
