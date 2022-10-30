class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class CDLL:
    def __init__(self):
        self.head1 = None
        self.head2 = None

    def add(self, val):
        if self.empty() is True:
            self.head1 = Node(val)
            self.head2 = self.head1
            self.head2.right = self.head1
            self.head1.left = self.head2
            print("== Head value created ==")
            return
        opt = int(input(
            "\n^^^^^ Insertion Operations ^^^^^ \nEnter 1 to add a Node at beginning\nEnter 2 to add a Node at end\nEnter 3 to add a Node before "
            " a node\nEnter 4 to add a Node after a node\n\nEnter your choice =  "))
        if opt == 1:
            a = Node(val)
            a.right = self.head1
            self.head1.left = a
            self.head2.right = a
            a.left = self.head2
            self.head1 = self.head1.left

        elif opt == 2:
            a = Node(val)
            self.head2.right = a
            a.left = self.head2
            a.right = self.head1
            self.head1.left = a
            self.head2 = self.head2.right

        elif opt == 3:
            pos = int(input("\nEnter the position ::"))
            i = 1
            n = self.head1.right
            flag = 0
            while n is not self.head1:
                if i == pos:
                    flag = 1
                    break
                n = n.right
                i = i + 1
            if flag == 1:
                a = Node(val)
                a.right = n
                n.left.right = a
                a.left = n.left
                n.left = a
            else:
                print("Position not found....!")

        elif opt == 4:
            pos = int(input("\nEnter the position :: "))
            i = 0
            n = self.head1
            flag = 0
            while n.right is not self.head1:
                if i == pos:
                    flag = 1
                    break
                n = n.right
                i = i + 1
            if flag == 1:
                a = Node(val)
                n.right.left = a
                a.right = n.right
                a.left = n
                n.right = a
            else:
                print("Position not found....!")
        else:
            print("Wrong option....!")

    def delete(self):
        if self.empty() is True:
            print("Linked List is empty....!")
            return
        elif self.head1.right is self.head2:
            self.head1 = None
            self.head2 = None
            return

        opt = int(input("\n ^^^^^ Deletion Operations ^^^^^ \nEnter 1 to delete the beginning element\nEnter 2 to delete the last element\nEnter 3 to "
                        "delete elements in between\n\nEnter your choice :: "))

        if opt == 1:
            self.head1 = self.head1.right
            self.head1.left = self.head2
            self.head2.right = self.head1

        elif opt == 2:
            self.head2 = self.head2.left
            self.head2.right = self.head1
            self.head1.left = self.head2

        else:
            op = int(input("\nEnter 1 to delete by position\nEnter 2 to delete by value\n\nEnter your choice :: "))
            if op == 1:
                pos = int(input("\nEnter the position :: "))
                i = 1
                n = self.head1.right
                flag = 0
                while n.right is not self.head1:
                    if i == pos:
                        flag = 1
                        break
                    i = i + 1
                    n = n.right
                if flag == 1:
                    n.left.right = n.right
                    n.right.left = n.left
                else:
                    print("Position not found....!")
                    return

            else:
                val = int(input("\nEnter the value you want to delete :: "))
                n = self.head1
                flag = 0
                while n.right is not self.head1:
                    if n.value == val:
                        flag = 1
                        break
                    n = n.right
                if flag == 1:
                    n.left.right = n.right
                    n.right.left = n.left
                else:
                    print("Value not found....!")
                    return

    def clear(self):
        self.head1 = None
        self.head2 = None
        print("Linked List cleared....!")

    def empty(self):
        if self.head1 is None:
            return True
        else:
            return False

    def display(self):
        if self.empty() is True:
            print("Linked List empty....!")
            return

        elif self.head1.right is self.head1:
            print("LINKED LIST")
            print(self.head1.value, "HEAD 1 & 2")
            print("Linked List ends....!")
            return

        o = int(input("\nEnter 1 to print in forward direction\nEnter 2 to print in backward direction\n\nenter:: "))
        print("\n *** LINKED LIST *** \n")

        if o == 1:
            print(self.head1.value, " <== HEAD 1")
            n = self.head1.right
            while n is not self.head2:
                print(n.value)
                n = n.right
            print(self.head2.value, " <== HEAD 2")
            print("\nLinked List ends....!")

        elif o == 2:
            print(self.head2.value, " <== HEAD 2")
            n = self.head2.left
            while n is not self.head1:
                print(n.value)
                n = n.left
            print(self.head1.value, " <== HEAD 1")
            print("Linked List ends....!")
            
        else:
            print("Wrong option....!")

LL = CDLL()
while True:
    option = int(input("\nEnter 1 = to add an element\nEnter 2 = to delete an element\nEnter 3 = to clear the Linked "
                       "List\nEnter 4 = to display the Linked List\nEnter 5 = to exit\n\nEnter your choice:  "))
    if option == 1:
        value = int(input("\nEnter the value you want to add = "))
        LL.add(value)
        continue
    elif option == 2:
        LL.delete()
        continue
    elif option == 3:
        LL.clear()
        continue
    elif option == 4:
        LL.display()
        continue
    elif option == 5:
        print("Exited....!")
        break
    elif option == 6:
        print(LL.empty())
    else:
        print("Wrong option....!")       