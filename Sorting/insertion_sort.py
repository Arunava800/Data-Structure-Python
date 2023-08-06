import timeit
from functools import wraps


def measure(func):
    @wraps(func)
    def time_it(*args, **kwargs):
        start = timeit.default_timer()
        try:
            return func(*args, **kwargs)
        finally:
            end = timeit.default_timer()-start
            print(f'Measured time :{end*(10**6):.2f} seconds')
    return time_it


@measure
def insertion_sort(a_list: list) -> list:
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position-1] > current_value:
            a_list[position] = a_list[position-1]
            position = position - 1
        a_list[position] = current_value

    return a_list


print(insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
