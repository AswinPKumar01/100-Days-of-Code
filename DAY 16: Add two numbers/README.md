# Approach

Iterating through the linked lists, performing digit-wise addition and updating the carry. It returns the resulting linked list.

# Complexity

- Time complexity: **O(max(N,M))**, where N and M are the lengths of the input linked lists l1 and l2, respectively.

- Space complexity: **O(max(N,M))**

# Explanation

- Create a new linked list with a dummy node using start = curr = ListNode(0). This will serve as the head of the resulting linked list.

- Initialize the carry variable as 0.

- Enter a while loop that continues until both l1 and l2 are None and the carry is 0.

- Within the loop, determine the values x and y by extracting the values from the current nodes of l1 and l2, respectively. If either l1 or l2 is None, assign 0 to the corresponding value.

- Perform the digit-wise addition using x + y + carry, and obtain both the new carry and the resulting value using divmod (dividing the sum by 10 to get the carry and taking the remainder as the value).

- Create a new node with the resulting value and assign it to curr.next to link it to the current node.

- Update curr to the newly created node.

- If l1 is not None, move l1 to the next node; otherwise, assign None to it. Repeat the same for l2.

- Once the while loop ends, return the next node of the dummy node, which is the actual head of the resulting linked list.
