from functools import wraps
import timeit


def measure(func):
    @wraps(func)
    def time_it(*args, **kwargs):
        start = timeit.default_timer()
        try:
            return func(*args, **kwargs)
        finally:
            end = timeit.default_timer() - start
            print(f"Measured time: {end*(10**6):.2f} seconds")
    return time_it


@measure
def selection_sort(a_list: list) -> list:
    length = len(a_list)
    for num_pass in range(length - 1, 0, -1):
        max_pos = 0
        for i in range(1, num_pass+1):
            if a_list[max_pos] < a_list[i]:
                max_pos = i

        a_list[max_pos], a_list[num_pass] = a_list[num_pass], a_list[max_pos]

    return a_list


print(selection_sort([54, 26, 45, 56, 93, 76, 45, 100]))
