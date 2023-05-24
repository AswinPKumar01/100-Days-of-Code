# Approach

Using Counter function to count the occurence of characters and then comparing to check whether they have the same set of characters.

# Complexity

- Time complexity: **O(N + MlogN)**, **n** is the length of input words and **m** is the number of unique characters in the counters.

- Space complexity: **O(N+M)**

# Explanation

- Initializing two Counter objects, **count1** and **count2**, by using the **Counter** function to count the occurrences of the characters in word1 and word2.

- Extracting the values from the Counters and **sorts** them in ascending order. The sorted values are assigned to variables **a** and **b** respectively.

- This line checks if the keys i.e., unique characters in **count1** and **count2** are equal and checks if the sorted values **a** and **b** are equal. 

- If both conditions are true, it returns **True**; otherwise, it returns** False**.
