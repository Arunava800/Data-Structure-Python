"""
Algorithm:
1. Take a  number
2. For each number, divide it into equal parts
3. Add the numbers that are obtained by dividing the number
4. Divide the addition with the table size and obtain the remainder
Example:
    nums: `433-555-4601`
    Divide the number as (43, 35, 55, 46, 01)
    add the above given numbers 43+35+46+01= 210 and divide it with table size (210%11) to obtain remainder
    assign the number based on the obtained remainder
"""


class HashFolding:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size

    def _split_number(self, nums) -> int:
        num_list = str(nums)
        print(num_list)
        sum_add = 0
        length = len(num_list)
        for i in range(0, length, 2):
            sum_add += int(num_list[i:i+2])
        return sum_add

    def hash_insert(self, number: list):
        for i in range(len(number)):
            split_sum = self._split_number(number[i])
            remainder = split_sum % 11
            if self.slots[remainder] == number[i]:
                print("Collisions!!!!!!!!")
            self.slots[remainder] = number[i]
        print(self.slots)


hashing = HashFolding()
hashing.hash_insert([113, 117, 97, 100, 114, 108, 116, 105, 99])
