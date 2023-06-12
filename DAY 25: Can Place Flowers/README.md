# Approach
 
Using two variables and conditional statements to check the adjacency

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize variables 'count' and 'prev' to 0.

- Iterate over each element 'cur' in the flowerbed list.

- If 'cur' is equal to 1 (indicating a planted flower), check if the previous element 'prev' is also 1.

- If 'prev' is 1, it means there are consecutive flowers, so decrement 'count' by 1 and update 'prev' to 1.

- If 'cur' is equal to 0 (indicating an empty spot), check the value of 'prev':

- If 'prev' is 1, update 'prev' to 0 (indicating the current spot can be used to place a flower).

- If 'prev' is 0, increment 'count' by 1 (indicating a potential spot for a new flower), and update 'prev' to 1.

- After iterating through the entire flowerbed, check if 'count' is greater than or equal to 'n' (the required number of flowers).

- If 'count' is greater than or equal to 'n', return True (it is possible to place 'n' flowers).

- Otherwise, return False (it is not possible to place 'n' flowers).
