# Approach 

Using reduce function to find the XOR of all the values in the array.

# Complexity

- Time complexity: **O(N)**
- Space complexity: **O(1)**

# Explanation

- Iterate over the indices i in the range of the length of the input list nums.

- Inside the loop, return the result of applying the XOR operation (^) to all elements in the nums list using the functools.reduce function with a lambda function.

- The XOR operation returns 0 for matching pairs of numbers and the number itself if it appears only once.

- Since the code returns immediately after the first iteration of the loop, it assumes that there is only one number that appears once in the list.
