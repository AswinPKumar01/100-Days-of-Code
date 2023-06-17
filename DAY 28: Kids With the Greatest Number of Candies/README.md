# Approach
 
 Determining whether each child can have the maximum number of candies by adding some extra candies and returning a list of boolean values indicating if each child can have the most candies.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(N)**

# Explanation

- Find the maximum number of candies in the given list using the max() function and assign it to the variable max_.

- Create an empty list result to store the boolean values indicating if each child can have the most candies.

- Iterate through each element in the candies list using a for loop and the range() function.

- For each element, check if the current number of candies (candies[i]) plus the extra candies (extraCandies) is greater than or equal to the maximum number of candies (max_).

- If the condition is true, append True to the result list, indicating that the current child can have the most candies.

- If the condition is false, append False to the result list, indicating that the current child cannot have the most candies.

- After iterating through all the elements in the candies list, return the result list.
