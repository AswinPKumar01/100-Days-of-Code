# Approach

 Using the approach of fibonacci sequence
 
# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- The code checks if the input n is equal to 0 or 1 using the condition n == 0 or n == 1. If n is either 0 or 1, the function returns 1, indicating that there is only one way to climb the stairs (either by taking 0 steps or 1 step).

- If the input n is neither 0 nor 1, the code proceeds to the next steps.

- Two variables a and b are initialized to 1. These variables represent the number of ways to climb the stairs for the previous two steps.

- The code enters a for loop that iterates from 2 to n (inclusive) using the range function. This loop calculates the number of ways to climb the stairs for the current step and updates the variables a and b accordingly.

- Inside the loop, a new variable c is assigned the value of a + b, which represents the number of ways to climb the stairs for the current step.

- Then, the variables a and b are updated: a is assigned the value of b, and b is assigned the value of c. This update prepares the variables for the next iteration of the loop.

- After the loop finishes, the function returns the value of b, which represents the number of ways to climb the stairs for the last step (i.e., n steps).
