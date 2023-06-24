# Approach
 
Using Dynammic Programming

# Complexity

- Time complexity: **O(N*M)**, where N is the size of the and M is the dp dictionary

- Space complexity: **O(M)**

# Explanation

- Initialize a dictionary dp with a single key-value pair, {0:0}. This represents the difference in height between the two sides of the billboard and the maximum height achieved at that difference.

- Iterate over each rod in the input list rods.

- For each rod, iterate over each key-value pair in dp using tuple(dp.items()).

- Calculate the height difference diff and the height height from the key-value pair.

- Update dp by adding the current rod's height to the existing difference: dp[diff+rod] = max(dp.get(diff+rod, 0), height). This ensures that the maximum height for a given difference is stored.

- Update dp by considering the scenario where the current rod is used on the opposite side of the billboard, resulting in a new difference: dp[abs(diff-rod)] = max(dp.get(abs(diff-rod), 0), height+min(diff, rod)). This calculates the maximum height for the new difference, considering the minimum of the previous difference and the current rod's height.

- Repeat steps 3-6 for all rod-key pairs in dp.

- Return the maximum height stored in dp for a difference of 0, which represents the maximum achievable height for the billboard.
