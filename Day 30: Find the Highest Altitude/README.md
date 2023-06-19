# Approach
 
Finding the highest gain by adding up the current gain and then finding the maximum.
# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize variables high and curr to 0, representing the highest altitude reached and the current altitude, respectively.

- Iterate over the elements i in the gain list.

- Add the value of i to the curr variable, representing the current altitude.

- Update the high variable by taking the maximum value between the current high and curr. This ensures that high always stores the highest altitude reached so far.

- After iterating through all the elements in gain, return the value of high, which represents the highest altitude reached.
