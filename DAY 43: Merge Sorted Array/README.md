# Approach

Starting from the end of the arrays and comparing elements at each position, then placing the larger element at the end of nums1 until all elements from nums2 are merged using three pointers.

# Complexity

- Time complexity: **O(M+N)**, where M and N are the number of elements in mums 1 and nums2 respectively.
- Space complexity: **O(1)**

# Explanation

- Initialize variables i, j, and k to the last indices of nums1, nums2, and the merged array nums1 respectively.

- While j is greater than or equal to 0 (indicating there are elements remaining in nums2 to be merged):

- If i is greater than or equal to 0 and the element at nums1[i] is greater than the element at nums2[j]:

- Assign the element at nums1[i] to nums1[k].

- Decrement k, i, and move to the previous elements in nums1 and nums2 respectively.
  
- Otherwise, Assign the element at nums2[j] to nums1[k].
  
- Decrement k, j, and move to the previous element in nums2.

- The loop continues until all elements from nums2 have been merged into nums1.

- The resulting nums1 will be the merged and sorted array.
