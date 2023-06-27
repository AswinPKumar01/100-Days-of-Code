# Approach
 
Using a heap to efficiently keep track of the smallest pairs and a visited set to avoid duplicates.

# Complexity

- Time complexity: **O(k log k), k is the input parameter**

- Space complexity: **O(k), the maximum number of elements stored in the heap and visited set is k **

# Explanation

- Create an empty list res to store the result.

- If nums1, nums2, or k is empty (or zero), return the empty result list.

- Create an empty heap (priority queue) and a set to track visited pairs.

- Push the first pair (nums1[0] + nums2[0], 0, 0) to the heap. The first element is the sum of the pair elements, and 0, 0 represents the indices of the current pair in nums1 and nums2.

- Add (0, 0) to the visited set.

- While k is not zero and the heap is not empty: Pop the smallest pair (sum, i, j) from the heap and append the pair [nums1[i], nums2[j]] to the result list.

- If i + 1 is within the range of nums1 and (i + 1, j) is not in visited: Push (nums1[i + 1] + nums2[j], i + 1, j) to the heap and Add (i + 1, j) to the visited set.

- If j + 1 is within the range of nums2 and (i, j + 1) is not in visited: Push (nums1[i] + nums2[j + 1], i, j + 1) to the heap and Add (i, j + 1) to the visited set.

- Decrease k by 1.

- Return the result list.



