class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
     
class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
     
    def push(self,data):        
        if self.head == None:
            self.head=Node(data)
             
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):         
        if self.isempty():
            return None
             
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):         
        if self.isempty():
            return None
             
        else:
            return self.head.data

    def display(self):        
        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
         
        else:   
            while(iternode != None):
                print(iternode.data,"->",end = " ")
                iternode = iternode.next
            return


if __name__ == "__main__":
    s = Stack()
    print("\n**"" *** Stack Using Linked List *** ""**")
    while(True):
        option = int(input("\nSTACK OPERATIONS...!\n1 = Push\n2 = Pop\n3 = to check if it is Empty\n4 = to print Stack\n5 = top element\n6 = exit\n\nSelect your choice: "))

        if(option == 1):
            item = input("Enter Element to push in stack\n")
            s.push(item)

        if(option == 2):
            print(s.pop())

        if(option == 3):
            print(s.isempty())

        if(option == 4):
            s.display()
            print("\n")

        if(option == 5):
            print(s.peek())

        if(option == 6):
            print("Exited...")
            break

 
