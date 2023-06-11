# Approach
 
 Comparing and swapping to make the same colours adjacent.

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize three pointers: red, white, and blue. red points to the start of the array, white starts from the beginning, and blue points to the end of the array.

- Enter a while loop that continues until white pointer surpasses the blue pointer.

- If the value at the white pointer is 0, swap the values at the red and white pointers, increment both red and white pointers, and move white one step forward. This step ensures all 0s are moved to the beginning of the array.

- If the value at the white pointer is 1, simply increment white pointer. This step ensures all 1s remain in the middle.

- If the value at the white pointer is 2, swap the values at the white and blue pointers, decrement the blue pointer, and move white one step forward. This step ensures all 2s are moved to the end of the array.

- Repeat steps 3-5 until the white pointer surpasses the blue pointer.
- The array will now be sorted in the order: 0s, 1s, 2s.
