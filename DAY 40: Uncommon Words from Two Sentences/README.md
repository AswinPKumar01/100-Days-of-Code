# Approach
 
Splitting the input sentences into arrays of words, creating a dictionary using Counter to count the occurrences of each word in both arrays, and then filtering the dictionary to include only the words with a count of 1, which are returned as the final result.

# Complexity

- Time complexity: **O(N+M)**, where M is the total number of characters and N is the number of unique words in combined array.

- Space complexity: **O(N+M)**

# Explanation

- Split the first string (s1) and second string (s2) into two arrays of words arr1 and arr2 using spaces as the delimiter.

- Combine the arrays arr1 and arr2.

- Create a dictionary (d_) using the combined array as keys and their frequency as values.

- Return a list comprehension that iterates over the items of d_, filtering only the keys (x) where the value (v) is equal to 1.
