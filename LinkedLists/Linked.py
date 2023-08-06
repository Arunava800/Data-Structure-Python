class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

    def set_data(self, data):
        self.data = data

    def set_next(self, new_next):
        self.next = new_next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next


class SingleList:
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def find(self, element):
        current = self.head
        while current is not None:
            if current.get_data() == element:
                return True
            else:
                current = current.get_next()
        else:
            return False

    def insert(self, index, element):
        count = 0
        current = self.head
        previous = None
        temp = Node(element)
        if index < 0:
            print("please provide a positive index")
            return
        # Insertion at the begin of the list
        if index == 0:
            temp.set_next(self.head)
            self.head = temp
        # Insertion of element at the middle
        else:
            while current is not None:
                if count == index:
                    temp.set_next(current)
                    previous.set_next(temp)
                    return
                else:
                    count += 1
                    previous = current
                    current = current.get_next()
            # Insertion at the end of the list
            else:
                current = temp
                previous.set_next(current)

    def remove(self, index):
        current = self.head
        previous = None
        count = 0
        while current is not None:
            if count == index:
                previous.set_next(current.get_next())
                break
            else:
                count = count + 1
                previous = current
                current = current.get_next()

    def size(self):
        count = 0
        current = self.head
        if current is None:
            return "The list is empty"

        else:
            while current is not None:
                count += 1
                current = current.get_next()
        return count

    def view(self):
        current = self.head
        if self.head is None:
            print("None")
            return
        while current is not None:
            print(f"{current.get_data()}", end=" ")
            current = current.get_next()


obj = SingleList()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(1)
obj.insert(0, 5)
print("The size of the list is", obj.size())

obj.view()
obj.remove(3)
obj.view()
print("The size of the list is", obj.size())
