# Approach
 
 Removing duplicates and then checking whether sum is equal to 0.
 
# Complexity

- Time complexity: **O(N^2)**

- Space complexity: **O(1)**

# Explanation

- Sort the input list in ascending order

- l is initialized as an empty list to store the resulting triplets.

- The code iterates through each element of the sorted list to check if the current element is a duplicate and skips it to avoid duplicate triplets.

- Two pointers j and k are initialized to find the remaining two elements of the triplet. j starts from i+1 (next element after i) and k starts from the end of the list (len(nums)-1).

- A while loop is used to iterate until j is less than k to find  the sum of the current triplet s.

- If s is greater than 0, it means the current triplet is too large, so we decrement k by 1 to move to a smaller element and if s is equal to 0, it means we have found a triplet that sums up to zero. So, we append the triplet [nums[i], nums[j], nums[k]] to the result list l.

- After appending the triplet to l, we increment j by 1 to move to the next element and then check if the new j is equal to the previous j to skip duplicate elements in the sorted list.

- Finally, the function returns the list l containing all the unique triplets that sum up to zero.
