# Approach
 
Using bitwise operations to track the occurrence of numbers.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initialize two variables, ones and twos, to 0.

- Iterate through each element, num, in the input array nums.

- Update the value of ones using the bitwise XOR operation (^) with num, followed by bitwise AND (&) with the complement of twos (~twos).

- This operation updates ones by XORing the current number with the previous ones value, and then clearing the bits where twos has set bits.

- Update the value of twos using the bitwise XOR operation with num, followed by bitwise AND with the complement of ones (~ones).

- This operation updates twos by XORing the current number with the previous twos value, and then clearing the bits where ones has set bits.

- Repeat steps 3 and 4 for each element in nums.

- After the iteration, the value of ones will hold the single number that appears only once.

- Return the value of ones as the result.
