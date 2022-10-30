class StackUsingArray:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if(not self.isEmpty()):
            lastElement = self.stack[-1] 
            del(self.stack[-1]) 
            return lastElement
        else:
            return("Stack Already Empty")

    def peek(self):
        if (self.isEmpty()):
            return str(-self.stack -1) 
        return self.stack[len(self.stack) - 1]
        
    def isEmpty(self):
        return self.stack == []

    def printStack(self):
        print(self.stack)

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    s = StackUsingArray()
    print("\n**"" *** Stack Using Array *** ""**")
    while(True):
        option = int(input("\nSTACK OPERATIONS...!\n1 = Push\n2 = Pop\n3 = to check if it is Empty\n4 = to print Stack\n5 = top element\n6 = size of stack\n7 = exit\n\nSelect your choice: "))

        if(option == 1):
            item = input("Enter Element to push in stack\n")
            s.push(item)

        if(option == 2):
            print(s.pop())

        if(option == 3):
            print(s.isEmpty())

        if(option == 4):
            s.printStack()

        if(option == 5):
            print(s.peek())

        if(option == 6):
            print(s.size())

        if(option == 7):
            print("Exited...")
            break