# Approach
 
Common approach of finding the product by traversing each element and multiplying it with a product variable and then using abs function to get the sign.

# Complexity

- Time complexity: **O(N)**

- Space complexity: **O(1)**

# Explanation

- Initializing a **prod** variable as 1 which is used to get the product of all the elements in the array.

- Finding the product of all the elements by traversing each element and multiplying it with the **prod** variable. 

- Using conditionals to check if the product is zero, if yes then returns 0.

- Else then uses **abs** method to return **1** for positive and **-1** for negative by dividing the **prod** variable with the asolute of **prod.**
