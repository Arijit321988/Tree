# Tree
Identifying Left view and Right view of a tree
1. create an empty queue and an output list variable
2. create a variable current node and initialize it with root Node.
3. Insert the current node to queue
4. Now start popping out the queue (as FIFO thus popleft )
5. For identifying left view of a tree we need to keep only the left side elements of a tree that can be achieved like below
6. For each LEVEL of BST tree keep on inserting the left node of a tree then the right node of tree into queue
7. keep on popping the first element of the queue and put in output_list to show only the left element 
Example 
                                        10
                                      /     \
                                     5       15
                                   /  \      /  \ 
                                   3.   7   13  17
                                            / \
                                           11  14
 
 
 LEFT VIEW: 10,5,3,11
 
 so empty queue q=deque()
 rootNode.value = 10
 queue.append(rootNode)
 while len(q) > 0 :
    for idx in range(1,len(q)+1):
      currentNode=q.popleft()
      if idx==1 #left most element of the current level
         output_list.append(currentNode.value)
      #Keep on searching left and right node and populate it in queue
      if currentNode.left:
         q.append(currentNode.left)
      if currentNode.right:
         q.append(currentNode.right)
