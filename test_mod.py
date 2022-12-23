import timeit

from adv_11 import get_alternating_factor, get_positives

n = 1383838383821823838232342341324323423232233423234823883838^20
time_ = timeit.timeit()
n % 23
end = timeit.timeit()
print(end - time_)

time_ = timeit.timeit()
divmod(n, 23)
end = timeit.timeit()
print(end - time_)

time_ = timeit.timeit()
alternating = get_alternating_factor(23)
friendly_sum = get_positives(str(n), alternating)
end = timeit.timeit()
print(end - time_)