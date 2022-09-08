from _collections import deque
#creating a BST tree
class Node:
  def __init__(self,data):
    self.value = data
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root=None

  def getDepthOfTree(self):
    if self.root == None:
      return -1
    currentNode = self.root;
    def getHeight(node):
      if node == None:
        return -1
      lheight=getHeight(node.left)
      rheight=getHeight(node.right)
      if lheight > rheight:
        return lheight+1
      else:
        return rheight+1
    return getHeight(currentNode)
  
#leftview of a tree
  def leftview(self):
    output_array=[]
    currentNode=self.root
    q = deque()
    #put root Node in queue
    q.append(currentNode)
    while (len(q) > 0):
      n=len(q)
      #go through each nodes of every level
      for i in range(1,n+1):
        currentNode=q.popleft()
        #first node of leftside side
        if i==1:
          output_array.append(currentNode.value)
        if currentNode.left:
          q.append(currentNode.left)
        if currentNode.right:
          q.append(currentNode.right)

    return output_array


  #rightview of a tree
  def rightvieworig(self):
    output_array=[]
    currentNode=self.root
    q = deque()
    #put root Node in queue
    q.append(currentNode)
    while (len(q) > 0):
      n=len(q)
      #go through each nodes of every level
      for i in range(1,n+1):
        currentNode=q.popleft()
        #first node of leftside side
        if i==1:
          output_array.append(currentNode.value)
        if currentNode.right:
          q.append(currentNode.right)
        if currentNode.left:
          q.append(currentNode.left)

    return output_array


#right view of a tree using while and using pointer method
  def rightview(self):
    output_array=[]
    currentNode=self.root
    q=deque()
    q.append(currentNode)
    while(len(q) > 0):
      n=len(q)
      while(n>0):
        n -=1
        currentNode=q.popleft()
        if n == 0 :
          output_array.append(currentNode.value)
        if currentNode.left:
          q.append(currentNode.left)
        if currentNode.right:
          q.append(currentNode.right)

    return output_array
    
def insert(self,data):
    #insert a newNode
    newNode=Node(data)
    if self.root == None:
      self.root=newNode
    else:
      currentNode=self.root ;
      while(True):
          if data == currentNode.value:
            return
          if data < currentNode.value:
            #insert data to left
            if currentNode.left == None:
              currentNode.left = newNode
              return 
            else:
              currentNode=currentNode.left
          if data > currentNode.value:
            #insert data to right
            if currentNode.right == None:
              currentNode.right = newNode
              return 
            else:
              currentNode=currentNode.right

if __name__ == "__main__":
  t=BinarySearchTree()
  t.insert(10)
  t.insert(5)
  t.insert(3)
  t.insert(13)
  t.insert(22)
  t.insert(11)
  t.insert(7)
  t.insert(9)
  t.insert(100)
  print("Left view of a BST: ", t.leftview())
  print("Right view of a BST: ", t.rightview())
  print("Right view of a BST: ", t.rightvieworig())
