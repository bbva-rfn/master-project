import numpy as np


def compute_new_stats(a_count, a_mean, a_var, b_count, b_mean, b_var):
    new_count = a_count + b_count
    new_mean = (a_count * a_mean + b_count * b_mean) / new_count
    new_var = (a_count * a_var + b_count * b_var + a_count * (a_mean - new_mean) ** 2 + b_count * (
                b_mean - new_mean) ** 2) / new_count

    return new_count, new_mean, new_var


def calc_stats(array):
    count = len(array)
    mean = array.mean()
    var = array.var()

    return count, mean, var


a = np.array([3, 5, 1])
a_count, a_mean, a_var = calc_stats(a)

b = np.array([1, 2, 6, 8])
b_count, b_mean, b_var = calc_stats(b)

c_cout, c_mean, c_var = compute_new_stats(a_count, a_mean, a_var, b_count, b_mean, b_var)
# c_mean, c_var = parallel_variance(np.array([a_mean, b_mean]), np.array([a_var, b_var]), np.array([len(a), len(b)]),
#                                  len(a) + len(b))

c = np.r_[a, b]
print(c.mean(), c_mean)
print(c.var(), c_var)
