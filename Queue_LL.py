class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isempty(self):
        if self.front == None:
            return True
        else:
            return False
    
    def peek(self):
        if self.isempty():
            print("\nQueue is Empty")
        else:
            print("The peek of the queue is: ",self.front.data)
    
    def Enqueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
 
    def Dequeue(self):
        if self.isempty():
            print("\nQueue is empty")
        else:
            temp = self.front
            self.front = temp.next
        if(self.front == None):
            self.rear = None
        return temp.data
    
    def Display(self):
        temp = self.front
        print("Queue  : ",end="")
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next
        print("")

    #def front(self):
    #    if self.isempty() == None:
    #        print("Queue is #empty")
    #    else:
    #        print('Front element: #')
    #        return self.front.data

    #def rear(self):
    #    if self.isempty() is True:
    #        print("Queue is empty")
    #    return self.rear.data

    def size(self):
        temp = self.front
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        print("Size of queue: ", count)
        return count
 
if __name__== '__main__':
    qu = Queue()
    while(True):
        Option = int(input("\n!.....Queue operations......! \n\n1 = inserting element in queue \n2 = deleting top element from queue \n3 = check Queue Is EMPTY or NOT\n4 = show PEEK element\n5 = Display Queue\n6 = size of queue\n7 =  exit\n\nEnter your choice: "))
        
        if(Option == 1):
            item = input("Enter Element to insert in Queue\n")
            qu.Enqueue(item)
            continue

        elif(Option == 2):
            print(qu.Dequeue()," is deleted from Queue!")
            continue

        elif(Option == 3):
            if qu.isempty():
                print("Queue is Empty!")
            else:
                print("Queue is NOT empty!")
            continue

        elif(Option == 4):
            qu.peek()
            continue

        elif(Option == 5):
            qu.Display()
            continue

        elif(Option == 6):
            qu.size()
            continue

        elif(Option == 7):
            break

        else:
            print("Wrong Option!\n")