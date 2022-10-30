class queue:
    def __init__(self):
        self.queue_ds = []
        self.Front = -1
        self.Rear = -1

    def enqueue(self, val):
        self.queue_ds.append(val)
        if self.Front == -1:
            self.Front += 1
            self.Rear += 1
        else:
            self.Rear += 1

    def dequeue(self):
        if self.empty() is True:
            print("\nQueue is empty")
            return
        else:
            temp = self.queue_ds.pop(self.Front)
            self.Rear -= 1
            if self.empty() is True:
                self.Front = -1
                self.Rear = -1
            return temp

    #def size(self):
    #    temp = self.Front
    #    count = 0
    #    while temp is not None:
    #        count = count + 1
    #        temp = temp.next
    #    print("Size of queue: ", count)
    #    return count

    #def front(self):
    #    if self.empty() is True:
    #        print("\nQueue empty")
    #    print("Front element: ", self.Front)    	
    #    return self.Front

    #def rear(self):
    #    if self.empty() is True:
    #        print("\nQueue empty")
    #    print("Rear element: ", self.Rear)
    #    return self.Rear

    def empty(self):
        if len(self.queue_ds) == 0:
            return True
        else:
            return False

    def display(self):
        if self.empty() is True:
            print("Queue empty")
            return
        print("\nThe Queue")
        if self.Front == self.Rear:
            print(self.queue_ds[self.Front], "<== Front <== Rear")
            return
        print(self.queue_ds[self.Front], "<== FRONT")
        i = self.Front + 1
        while i < self.Rear:
            print(self.queue_ds[i])
            i += 1
        print(self.queue_ds[self.Rear], "<== REAR")
        print("The Queue Ends\n")


if __name__== '__main__':
    qu = queue()
    while(True):
        Option = int(input("\n!.....Queue operations......! \n\n1 = inserting element in queue \n2 = deleting top element from queue \n3 = check Queue Is EMPTY or NOT\n4 = Display Queue\n5 =  exit\n\nEnter your choice: "))
        
        if(Option == 1):
            item = input("Enter Element to insert in Queue\n")
            qu.enqueue(item)
            continue

        elif(Option == 2):
            print(qu.dequeue()," is deleted from Queue!")
            continue

        elif(Option == 3):
            if qu.empty():
                print("Queue is Empty!")
            else:
                print("Queue is NOT empty!")
            continue

        elif(Option == 4):
            qu.display()
            continue

        #elif(Option == 5):
        #    qu.size()
        #    continue

        elif(Option == 5):
            break

        else:
            print("Wrong Option!\n")

