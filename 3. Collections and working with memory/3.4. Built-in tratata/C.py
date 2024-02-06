from itertools import count

start, end, step = map(float, input().split())

for value in count(start, step):
    if value <= end:
        print(round(value, 2))
    else:
        break

# import numpy as np

# start, end, step = map(float, input().split())

# for val in np.arange(start, end + 0.01, step):
#     print("{0:.2f}".format(val))

# print(f'{start, end, step}')
    # round(val, 3))

# "{0:.2f}".format(70.12312312)
