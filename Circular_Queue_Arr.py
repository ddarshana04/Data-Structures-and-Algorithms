class CircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full....!\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty....!\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def display(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
    
    def size(self):
        if self.tail >= self.head:
           qSize = self.tail - self.head
        else:
            qSize = self.maxSize - (self.head - self.tail)
        print ("Size of circular queue: ", size)
        return qSize

if __name__== '__main__':
    
    size = input("Enter the size of the Circular Queue: ")
    qu = CircularQueue(int(size))

    while(True):
        Option = int(input("\n!.....Circular Queue operations......! \n\n1 = Insert element in queue \n2 = Deleting element from queue \n3 = Display Queue\n4 = size\n5 =  exit\n\nEnter your choice: "))
        
        if(Option == 1):
            item = input("Enter Element to insert in Queue\n")
            qu.enqueue(item)
            continue

        elif(Option == 2):
            print(qu.dequeue()," is deleted from Queue!")
            continue

        elif(Option == 3):
            qu.display()
            continue

        elif(Option == 4):
            qu.size()
            continue

        elif(Option == 5):
          print ("Exited..!")
          break

        else:
            print("Wrong Option!\n")

