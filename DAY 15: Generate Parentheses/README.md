# Approach
 
Sorting the array in ascending order to make the highest number to the end of the array and then returning the sum of all the highest numbers.

# Complexity

- Time complexity: **O(NMlog(M))**, **n** is the number of rows and **m** is the number of columns in the matrix.

- Space complexity: **O(1)**

# Explanation

Initialize a queue called "queue" with a tuple containing an opening parenthesis '(', the number of opening parentheses (1), and the number of closing parentheses (0). This tuple represents the current state of parentheses generation.
Initialize two variables: 'f' as the front index of the queue and 'l' as the queue length.
Enter a while loop that continues until the front index 'f' becomes equal to the queue length 'l', indicating that all possibilities have been explored.
Inside the loop, retrieve the current tuple from the front of the queue using the front index 'f'.
Check if the sum of the number of opening and closing parentheses in the current tuple is equal to 2 times 'n'. If so, it means a valid combination has been generated. Append the string representation of the current combination (cur[0]) to the "ans" list. Increment 'f' by 1 to move to the next item in the queue, and continue to the next iteration of the loop.
If the number of opening parentheses (cur[1]) is less than 'n', it means it's possible to add an additional opening parenthesis '('. Append a new tuple to the queue by concatenating 'cur[0]' with '(', increment 'cur[1]' by 1, and increment 'l' by 1 to reflect the addition of a new item to the queue.
If the number of closing parentheses (cur[2]) is less than the number of opening parentheses (cur[1]), it means it's possible to add a closing parenthesis ')'. Append a new tuple to the queue by concatenating 'cur[0]' with ')', increment 'cur[2]' by 1, and increment 'l' by 1 to reflect the addition of a new item to the queue.
After the inner if statements, increment 'f' by 1 to move to the next item in the queue.
Once the loop finishes, return the "ans" list containing all the valid combinations of parentheses.
