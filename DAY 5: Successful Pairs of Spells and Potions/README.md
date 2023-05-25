# Approach

Using bisect_left function on a sorted version of the "potions" list to efficiently find the count of successful pairs for each spell.

# Complexity

- Time complexity: **O(NlogM)**

- Space complexity: **O(M)**

Where **N** is the length of the "spells" list and **M** is the length of the "portions" list

# Explanation

- Sorting the **"potions"** list in ascending order and assigning it to the variable **"sorted_potions"**.

- Initializing an empty list named **"result"** to store the counts of successful pairs for each spell.

- Iterating through each element **"a"** and calculates the value **(success + a - 1) // a**, which represents the minimum value a potion needs to be multiplied by to achieve or exceed the **"success"** value.

- Performing a binary search using the bisect_left function on the sorted **"potions"** list to find the index where the calculated value should be inserted, which gives the count of potions greater than or equal to the calculated value.

- Subtracting the index from the total length of the **"sorted_potions"** list to obtain the count of successful pairs for the current spell **"a"** and appending the count to the **"results"** list.

- After complete iteration, it returns the **"result"** list containing the counts of successful pairs for each spell.

