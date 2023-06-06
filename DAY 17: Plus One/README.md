# Approach
 
Converting into a string and adding values by making it integer.

# Complexity

- Time complexity: **O(N+M+K)**, **N** is the length of digits, **M** is the number of digits in the sum, **K** is the lenth of arr_sum

- Space complexity: **O(M)**

# Explanation

- Initialize an empty string arr_str.

- Iterate over each element i in the digits list and convert each element i to a string using str(i) and concatenate it with arr_str.

- Convert the concatenated string arr_str to an integer by using int(arr_str) and add 1.

- Convert the sum to a string using str() function and assign it to num.

- Create a new list by iterating over each character i in num and convert the character i to an integer using int(i).

- Append the integer to the new list and return the new list.
