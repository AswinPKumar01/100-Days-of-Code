# Approach

Converting the array into set data type to remove the duplicates.

# Complexity

- Time complexity: **O(NlogN)**, **n** is the length of input words and **m** is the number of unique characters in the counters.

- Space complexity: **O(N)**

# Explanation

- A new list is created using the set function to remove any duplicates from the original **nums** list which converts the nums list into a set, which only contains unique elements, and then the **sorted** function is used to sort the elements in ascending order.

- The contents of the nums list is replaced with the new list using slice assignment **nums[:]**

- The method returns the length of the updated nums list using the len function, this represents the number of unique elements in the list after removing duplicates.
