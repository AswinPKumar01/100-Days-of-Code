# Approach

Adding the values of the linked list to a new list and checking whether it is a palindrome using string slice comparison.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(N)**

# Explanation

- **pal_check** is initialized as an empty list to store the values of the linked list nodes.

- The while loop iterates through the linked list starting from the head, appends the values of each node to the **pal_check** list and updates head to the next node.

- The if statement checks whether the **pal_check** list is equal to its reverse **"pal_check[::-1]"**. If they are equal, it means the linked list is a palindrome.

- If the condition in the if statement is true, the function returns **True**, indicating that the linked list is a palindrome. Otherwise, it returns **False**.
