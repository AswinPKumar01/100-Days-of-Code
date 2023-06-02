# Approach
 
Using enumerate function to split the array and checking wih each element

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

-  The method uses a for loop with enumerate which checks if the current element (char) is greater than or equal to the target value. 

-  If it is, it means that we have found the correct position to insert the target value or that the target value already exists in the list. In either case, the method returns the current index (i).

- The next block checks if the nums list is empty. If it is, it means that there are no elements in the list, so the method returns 0 as the position to insert the target value.

- If the nums list is not empty and the loop did not find a suitable position for the target value, the code returns the length of the nums list. This implies that the target value should be inserted at the end of the list.
