from functools import wraps
import timeit


def measure(func):
    @wraps(func)
    def time_it(*args, **kwargs):
        start = timeit.default_timer()
        try:
            return func(*args, **kwargs)
        finally:
            end = timeit.default_timer()-start
            print(f"Total execution time {end*(10**6)} microseconds")
    return time_it


@measure
def bubble_sort(a_list: list) -> list:
    length = len(a_list)
    for num in range(length-1, 0, -1):
        for i in range(num):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

    return a_list


print(bubble_sort([54, 26, 45, 56, 93, 76, 45, 100]))
