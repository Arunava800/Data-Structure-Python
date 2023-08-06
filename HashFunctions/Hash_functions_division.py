class HashBrute:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size

    def hash_insert(self, array):
        for i in range(len(array)):
            remainder = array[i] % self.size
            if self.slots[remainder] is None:
                self.slots[remainder] = array[i]
            else:
                print(f'The collision occurs and the value {array[i]} cannot be inserted at {remainder}')

    def display_hash(self):
        print(self.slots)

    def search_item(self, item):
        remainder = item % self.size
        if self.slots[remainder] is not None and self.slots[remainder] == item:
            print('The returned value is ', self.slots[remainder])
        else:
            print('The the value does not exists')


fun_hash = HashBrute()
fun_hash.hash_insert([113, 117, 97, 100, 114, 108, 116, 105, 99])
fun_hash.display_hash()
fun_hash.search_item(54)
