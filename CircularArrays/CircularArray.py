class Circular:
    def __init__(self):
        self.head = 0
        self.array_list = [None]
        self.tail = len(self.array_list)

    def add_elements(self, key):
        tail_size = self.tail-1
        if self.head == tail_size:
            self.array_list[0] = key

    def insert_front(self, key, n):
        length = len(self.array_list)
        if n == length:
            new_array = [None] * (2 * length)
            for i in range(length-1):
                new_array[i] = self.array_list[(self.head+i) % length]
            self.array_list = new_array
            self.head = 0
            self.tail = len(self.array_list)-1

        self.head = self.head - 1
        if self.head == -1:
            self.head = len(self.array_list) - 1
        self.array_list[self.head] = key

    def print_elements(self):
        print(self.array_list)


circular = Circular()
circular.add_elements(10)
circular.insert_front(10, 1)
circular.print_elements()
