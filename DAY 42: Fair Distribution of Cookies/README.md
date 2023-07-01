# Approach
 
Using recursion to find the solution by parts.

- Time complexity: **O(N^2)**

- Space complexity: **O(N+K)**, where N is the number of cookies and K is the number of children.

# Explanation


- The method initializes an empty list split and a variable best with a value of positive infinity.

- It then calls a nested helper function dfs with an initial parameter value of 0.

- The dfs function is defined inside the distributeCookies method and takes a single parameter p.

- Inside the dfs function, it uses the nonlocal keyword to access and modify the best variable from the outer scope.

- The dfs function uses backtracking to explore different combinations of distributing cookies among the children.

- If p is equal to the length of the cookies list, it means all cookies have been distributed, so it calculates the maximum number of cookies received by any child (max(split)) and updates the best variable if it is smaller than the current best value.

- If the length of split is less than k, it means not all children have received cookies yet, so it appends the pth cookie to the split list, recursively calls dfs with p+1, and then removes the last cookie from the split list (backtracking).

- If the length of split is already k, it means all children have received cookies, so it checks if adding the pth cookie to any existing child's count results in a smaller maximum value than the current best. If so, it temporarily adds the cookie to the ith child's count, recursively calls dfs with p+1, and then subtracts the cookie from the ith child's count (backtracking).

- After the recursive exploration, the dfs function returns.

- Finally, the distributeCookies method returns the value stored in the best variable.
