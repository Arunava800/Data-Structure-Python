import timeit
from functools import wraps


def measure(func):
    @wraps(func)
    def time_it(*args, **kwargs):
        start = timeit.default_timer()
        try:
            return func(*args, **kwargs)
        finally:
            end = timeit.default_timer() - start
            print(f"It took {end*(10**6):.2f} seconds")
    return time_it


@measure
def short_bubble(a_list: list) -> list:
    length = len(a_list)
    for num in range(length-1, 0, -1):
        count = 0
        for i in range(num):
            if a_list[i] > a_list[i+1]:
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]
                count += 1
        if count == 0:
            break
    return a_list


print(short_bubble([54, 26, 45, 56, 93, 76, 45, 100]))
